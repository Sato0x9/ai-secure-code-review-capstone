import sqlite3

def get_user(username):
    conn = sqlite3.connect("users.db")
    return conn.execute(
        "SELECT * FROM users WHERE name = ?",
        (username,)
    ).fetchall()
