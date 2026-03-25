"""Render startup script with error capture and keep-alive."""
import logging
import os
import signal
import sys
import traceback

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("start")


def handle_signal(signum, frame):
    log.info("Received signal %s — shutting down gracefully", signum)
    sys.exit(0)


signal.signal(signal.SIGTERM, handle_signal)
signal.signal(signal.SIGINT, handle_signal)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "10000"))
    log.info("Starting uvicorn on port %d", port)
    try:
        import uvicorn

        log.info("uvicorn imported OK")
        from content_pipeline.web.app import app

        log.info("app imported OK — starting server")
        uvicorn.run(
            app,
            host="0.0.0.0",
            port=port,
            log_level="info",
            timeout_keep_alive=120,
        )
    except Exception:
        log.error("Fatal startup error:")
        traceback.print_exc()
        sys.exit(1)
