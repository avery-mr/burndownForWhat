import psycopg2
import os
import traceback

DATABASE_URL = "postgresql://belaybuddy_user:AtDkADwMJk9CGBWZdWxLvWS6IaVfksiq@dpg-cvti41be5dus73a9kcng-a/belaybuddy"

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
        print(f"Error executing query: {str(e)}")
        traceback.print_exc()
        return f"Error: {str(e)}"
    finally:
        cur.close()
        conn.close()
