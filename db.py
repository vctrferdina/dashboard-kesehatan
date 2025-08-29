import mysql.connector
import pandas as pd

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sisihat_db"
    )

def get_users():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, username, role FROM users")
    result = cursor.fetchall()
    conn.close()
    return pd.DataFrame(result)