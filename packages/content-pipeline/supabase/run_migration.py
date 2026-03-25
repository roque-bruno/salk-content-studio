"""
Script para rodar a migration SQL no Supabase.

Uso:
    python supabase/run_migration.py <database_password>

Ou com connection string:
    python supabase/run_migration.py --uri "postgresql://postgres.uottkdywmxbwiogxzaqa:<password>@aws-0-sa-east-1.pooler.supabase.com:6543/postgres"
"""

import sys
from pathlib import Path

import psycopg2


PROJECT_REF = "uottkdywmxbwiogxzaqa"
MIGRATION_FILE = Path(__file__).parent / "migrations" / "001_initial_schema.sql"


def run_migration(conn_string: str) -> None:
    """Executa a migration SQL no Supabase."""
    sql = MIGRATION_FILE.read_text(encoding="utf-8")

    # Separar statements (psycopg2 não suporta executescript como sqlite)
    # Mas podemos rodar o script inteiro com execute se não tiver conflitos
    print(f"Conectando ao Supabase...")
    conn = psycopg2.connect(conn_string)
    conn.autocommit = True
    cur = conn.cursor()

    # Rodar cada statement separadamente para melhor error handling
    statements = []
    current = []
    for line in sql.split("\n"):
        stripped = line.strip()
        if stripped.startswith("--") or not stripped:
            continue
        current.append(line)
        if stripped.endswith(";"):
            statements.append("\n".join(current))
            current = []

    # Capturar statements multi-linha (funções com $$)
    if current:
        statements.append("\n".join(current))

    success = 0
    errors = 0
    for i, stmt in enumerate(statements, 1):
        stmt = stmt.strip()
        if not stmt:
            continue
        try:
            cur.execute(stmt)
            success += 1
            # Print first 60 chars of statement
            preview = stmt.replace("\n", " ")[:60]
            print(f"  [{i}/{len(statements)}] OK: {preview}...")
        except Exception as e:
            err_msg = str(e).strip()
            if "already exists" in err_msg:
                print(f"  [{i}/{len(statements)}] SKIP (already exists)")
                success += 1
            else:
                print(f"  [{i}/{len(statements)}] ERROR: {err_msg}")
                errors += 1

    cur.close()
    conn.close()
    print(f"\nMigration complete: {success} OK, {errors} errors")


def main():
    if len(sys.argv) < 2:
        print("Uso: python run_migration.py <database_password>")
        print("  ou: python run_migration.py --uri <connection_string>")
        sys.exit(1)

    if sys.argv[1] == "--uri":
        conn_string = sys.argv[2]
    else:
        password = sys.argv[1]
        conn_string = (
            f"postgresql://postgres.{PROJECT_REF}:{password}"
            f"@aws-0-sa-east-1.pooler.supabase.com:6543/postgres"
            f"?sslmode=require"
        )

    run_migration(conn_string)


if __name__ == "__main__":
    main()
