from .db_utils import get_connection

def selectUser():
  try:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM "User";')
    records = cur.fetchall()
    cur.close()
    conn.close()
    return "<br>".join(str(record) for record in records) or "No records found."
  except Exception as e:
    return f"Error selecting User: {str(e)}"

def selectStyle():
  try:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM "Style";')
    records = cur.fetchall()
    cur.close()
    conn.close()
    return "<br>".join(str(record) for record in records) or "No records found."
  except Exception as e:
    return f"Error selecting User: {str(e)}"

def selectLocation():
  try:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM "Location";')
    records = cur.fetchall()
    cur.close()
    conn.close()
    return "<br>".join(str(record) for record in records) or "No records found."
  except Exception as e:
    return f"Error selecting User: {str(e)}"

def selectUserStyle():
  try:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM "UserStyle";')
    records = cur.fetchall()
    cur.close()
    conn.close()
    return "<br>".join(str(record) for record in records) or "No records found."
  except Exception as e:
    return f"Error selecting User: {str(e)}"

def selectUserRating():
  try:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM "UserRating";')
    records = cur.fetchall()
    cur.close()
    conn.close()
    return "<br>".join(str(record) for record in records) or "No records found."
  except Exception as e:
    return f"Error selecting User: {str(e)}"

def selectBuddy():
  try:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM "Buddy";')
    records = cur.fetchall()
    cur.close()
    conn.close()
    return "<br>".join(str(record) for record in records) or "No records found."
  except Exception as e:
    return f"Error selecting User: {str(e)}"

def selectMessage():
  try:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT MessageID, SenderID, ReceiverID, Text, TO_CHAR(Timestamp, \'YYYY-MM-DD HH24:MI:22\') AS Timestamp FROM "Message";')
    records = cur.fetchall()
    cur.close()
    conn.close()
    return "<br>".join(str(record) for record in records) or "No records found."
  except Exception as e:
    return f"Error selecting User: {str(e)}"

def selectEvent():
  try:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT EventID, HostID, ClimberID1, ClimberID2, ClimberID3, ClimberID4, ClimberID5, TO_CHAR(DateTime, \'YYYY-MM-DD HH24:MI:SS\') AS DateTime, LocationID, PrimaryStyleID, SecondaryStyleID, status, Notes FROM "Event";')
    records = cur.fetchall()
    cur.close()
    conn.close()
    return "<br>".join(str(record) for record in records) or "No records found."
  except Exception as e:
    return f"Error selecting User: {str(e)}"

if __name__ == "__main__":
    print("Testing select functions:")
    print("User:", selectUser())
    print("Style:", selectStyle())
    print("Location:", selectLocation())
    print("UserStyle:", selectUserStyle())
    print("UserRating:", selectUserRating())
    print("Buddy:", selectBuddy())
    print("Message:", selectMessage())
    print("Event:", selectEvent())
