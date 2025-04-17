import psycopg2
import os
import traceback
import urllib.parse as urlparse

DATABASE_URL = "postgresql://belaybuddy_user:AtDkADwMJk9CGBWZdWxLvWS6IaVfksiq@dpg-cvti41be5dus73a9kcng-a/belaybuddy"

# def get_connection():
#     return psycopg2.connect(DATABASE_URL)

def get_connection():
    environment = os.getenv('FLASK_ENV', 'development')

    if environment == 'development':
        print("connecting to local db...")
        url = urlparse.urlparse("postgresql://belaybuddy_user:AtDkADwMJk9CGBWZdWxLvWS6IaVfksiq@dpg-cvti41be5dus73a9kcng-a.oregon-postgres.render.com/belaybuddy")
        return psycopg2.connect(
            dbname=url.path[1:], 
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port or 5432,
            sslmode='require'
        )
    else:
        print("conencting to production db...")
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
