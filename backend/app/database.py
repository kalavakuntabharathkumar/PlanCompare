import sqlite3
from pathlib import Path
DB_PATH = Path(__file__).resolve().parent.parent / "plans.db"
def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection
def initialize():
    with get_connection() as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS plans (
            id INTEGER PRIMARY KEY, name TEXT NOT NULL, carrier TEXT NOT NULL,
            annual_premium REAL NOT NULL, deductible REAL NOT NULL, copay REAL NOT NULL,
            coverage_percent REAL NOT NULL CHECK(coverage_percent BETWEEN 0 AND 100)
        )""")
        count = conn.execute("SELECT COUNT(*) FROM plans").fetchone()[0]
        if count == 0:
            from .data import PLANS
            conn.executemany("INSERT INTO plans VALUES (:id,:name,:carrier,:annual_premium,:deductible,:copay,:coverage_percent)", PLANS)
def list_plans():
    with get_connection() as conn:
        return [dict(row) for row in conn.execute("SELECT * FROM plans ORDER BY annual_premium")]
def get_plan(plan_id: int):
    with get_connection() as conn:
        row = conn.execute("SELECT * FROM plans WHERE id=?", (plan_id,)).fetchone()
        return dict(row) if row else None
