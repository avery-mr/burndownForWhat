import psycopg2
import urllib.parse as urlparse
from app.app import local_db_connect

def local_db_connect():
    url = urlparse.urlparse("postgresql://belaybuddy_user:AtDkADwMJk9CGBWZdWxLvWS6IaVfksiq@dpg-cvti41be5dus73a9kcng-a.oregon-postgres.render.com/belaybuddy")
    conn = psycopg2.connect(
        dbname=url.path[1:], 
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port or 5432,
        sslmode='require'
        )
    return conn

def test_db_connection():
    username = 'climbzRcool'
    try:
        # url = urlparse.urlparse("postgresql://belaybuddy_user:AtDkADwMJk9CGBWZdWxLvWS6IaVfksiq@dpg-cvti41be5dus73a9kcng-a.oregon-postgres.render.com/belaybuddy")

        # conn = psycopg2.connect(
        #     dbname=url.path[1:], 
        #     user=url.username,
        #     password=url.password,
        #     host=url.hostname,
        #     port=url.port or 5432,
        #     sslmode='require'
        # )
        conn = local_db_connect()

        cur = conn.cursor()
        cur.execute('SELECT Email, City, State FROM "User" where Username = %s;', (username,))
        records = cur.fetchone()
        
        print("✅ Connected to database successfully. Test query result:", records)

        cur.close()
        conn.close()

    except Exception as e:
        print("Database connection failed:", e)

# Only run the test when the script is executed directly
if __name__ == "__main__":
    test_db_connection()