import sqlite3
from datetime import datetime


conn = sqlite3.connect("test_results.db", check_same_thread=False)
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS test_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    module_name TEXT NOT NULL,
    status TEXT CHECK(status IN ('pass', 'fail')) NOT NULL,
    timestamp TEXT NOT NULL
)
""")

conn.commit()


def insert_test_result(module_name, status, timestamp=None):
    if not timestamp:
        timestamp = datetime.now().isoformat()
    cursor.execute(
        "INSERT INTO test_results (module_name, status, timestamp) VALUES (?, ?, ?)",
        (module_name, status, timestamp)
    )
    conn.commit()
    return cursor.lastrowid

def get_all_results():
    cursor.execute("SELECT * FROM test_results")
    return cursor.fetchall()

def update_test_status(test_id, new_status):
    cursor.execute(
        "UPDATE test_results SET status = ? WHERE id = ?",
        (new_status, test_id)
    )
    conn.commit()
    return cursor.rowcount

def get_summary():
    cursor.execute("""
        SELECT 
            COUNT(*) as total,
            SUM(CASE WHEN status = 'pass' THEN 1 ELSE 0 END) as passed,
            SUM(CASE WHEN status = 'fail' THEN 1 ELSE 0 END) as failed
        FROM test_results
    """)
    return cursor.fetchone()


if __name__ == "__main__":
  
    insert_test_result("Module_1", "pass")
    results = get_all_results()
    print("Current entries in test_results table:")
    for row in results:
        print(row)

