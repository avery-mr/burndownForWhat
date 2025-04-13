import psycopg2
import os

DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    return psycopg2.connect(DATABASE_URL)

def execute_query(sql: str, message: str):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        return message
    except Exception as e:
        print(f"Error: {e}")
        return f"Error: {e}"
    finally:
        cur.close()
        conn.close()
