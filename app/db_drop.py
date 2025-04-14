from .db_utils import get_connection, execute_query

def dropAll():
  """drop ALL the tables and types in reverse order from how they were created"""
  try:
    conn = get_connection()
    cur = conn.cursor()

    # dropping tables in reverse order to avoid foreign key constraints
    drop_statements = [
      '''DROP TABLE IF EXISTS "UserStyle" CASCADE;''',
      '''DROP TABLE IF EXISTS "UserRating" CASCADE;''',
      '''DROP TABLE IF EXISTS "Buddy" CASCADE;''',
      '''DROP TABLE IF EXISTS "Message" CASCADE;''',
      '''DROP TABLE IF EXISTS "Event" CASCADE;''',
      '''DROP TABLE IF EXISTS "Location" CASCADE;''',
      '''DROP TABLE IF EXISTS "User" CASCADE;''',
      '''DROP TABLE IF EXISTS "Style" CASCADE;''',
      '''DROP TYPE IF EXISTS status_enum CASCADE;''',
      '''DROP TYPE IF EXISTS status_enum2 CASCADE;'''
    ]

    results = []
    for sql in drop_statements:
      cur.execute(sql)
      results.append(f"Executed: {sql.strip()}")

    conn.commit()
    return "<br>".join(results) + "<br>All tables and types dropped successfully"
  except Exception as e:
    conn.rollback()
    return f"Error dropping tables: {str(e)}"
  finally:
    cur.close()
    conn.close()

if __name__ == "__main__":
  print(dropAll())



