"""Render startup — diagnostic mode that captures errors via HTTP."""
import json
import logging
import os
import signal
import sys
import traceback
from http.server import HTTPServer, BaseHTTPRequestHandler

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    stream=sys.stdout,
)
log = logging.getLogger("start")

PORT = int(os.environ.get("PORT", "10000"))

# Global error capture
_startup_error = None
_startup_status = "starting"


class DiagHandler(BaseHTTPRequestHandler):
    """Serves health + diagnostic info."""

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        body = {
            "status": _startup_status,
            "version": "2.0.0",
            "error": _startup_error,
            "python": sys.version,
            "cwd": os.getcwd(),
            "port": PORT,
        }
        self.wfile.write(json.dumps(body).encode())

    def log_message(self, fmt, *args):
        pass  # suppress access logs


def handle_signal(signum, frame):
    log.info("Signal %s — exit", signum)
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGTERM, handle_signal)
    signal.signal(signal.SIGINT, handle_signal)

    log.info("Diagnostic mode — port %d", PORT)

    # Step 1: Test basic imports
    try:
        log.info("Step 1: importing uvicorn...")
        import uvicorn
        log.info("Step 1: OK")
    except Exception as e:
        _startup_error = f"uvicorn import: {traceback.format_exc()}"
        _startup_status = "error"
        log.error(_startup_error)
        server = HTTPServer(("0.0.0.0", PORT), DiagHandler)
        server.serve_forever()
        sys.exit(0)

    # Step 2: Test app import
    try:
        log.info("Step 2: importing app...")
        from content_pipeline.web.app import app
        log.info("Step 2: OK")
    except Exception as e:
        _startup_error = f"app import: {traceback.format_exc()}"
        _startup_status = "error"
        log.error(_startup_error)
        server = HTTPServer(("0.0.0.0", PORT), DiagHandler)
        server.serve_forever()
        sys.exit(0)

    # Step 3: Run uvicorn
    _startup_status = "running"
    log.info("Step 3: starting uvicorn...")
    try:
        uvicorn.run(app, host="0.0.0.0", port=PORT, log_level="info")
    except Exception:
        _startup_error = f"uvicorn run: {traceback.format_exc()}"
        _startup_status = "error"
        log.error(_startup_error)
        server = HTTPServer(("0.0.0.0", PORT), DiagHandler)
        server.serve_forever()
