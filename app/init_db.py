# init_db.py
import sqlite3
import sys



def create(db_filename):
    
    conn = sqlite3.connect(db_filename)
    cur = conn.cursor()

    # create user table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT NOT NULL,
        firstname TEXT NOT NULL,
        lastname TEXT NOT NULL,
        city TEXT,
        state TEXT,
        profilepicURL TEXT

    );
    """)

    # Create messages table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        messageID INTEGER PRIMARY KEY AUTOINCREMENT,
        sender TEXT NOT NULL,
        receiver TEXT NOT NULL,
        content TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Create friends table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS friends (
        user1 TEXT NOT NULL,
        user2 TEXT NOT NULL,
        PRIMARY KEY (user1, user2),
        FOREIGN KEY (user1) REFERENCES users(username),
        FOREIGN KEY (user2) REFERENCES users(username)
    );
    """)

    # Create events table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS events (
        eventID INTEGER PRIMARY KEY AUTOINCREMENT,
        eventTitle TEXT NOT NULL,
        eventDate TEXT NOT NULL,
        eventLocation TEXT NOT NULL,
        eventCapacity INTEGER NOT NULL,
        eventRegistered INTEGER NOT NULL                
    );    
    """)

    conn.commit()
    conn.close()

def fill(db_filename):
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    
    # insert existing into user table
    users = [
    ("user3308", "cspb3308@colorado.edu", "Alex", "Honnold", "Boulder", "CO", "https://example.com/profiles/alex.jpg"),
    ("climbchick42", "sara.mountains@gmail.com", "Sara", "Lopez", "Boulder", "CO", "https://example.com/profiles/sara.jpg"),
    ("grip_master", "devin.grip@climbmail.com", "Devin", "Kim", "Salt Lake City", "UT", "https://example.com/profiles/devin.png"),
    ("rockhound", "marco@cragmail.org", "Marco", "Diaz", "Flagstaff", "AZ", "https://example.com/profiles/marco.jpeg"),
    ("chalkedup", "lena123@peakmail.net", "Lena", "Chen", "Bishop", "CA", "https://example.com/profiles/lena.webp")
    ]

    c.executemany('''
    INSERT INTO users (username, email, firstname, lastname, city, state, profilepicURL)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', users)

    messages = [
    ("climbchick42", "grip_master", "Hey! Are you still up for climbing tomorrow at Clear Creek?", "2025-04-14 09:13:00"),
    ("grip_master", "climbchick42", "Totally! Let’s meet at the parking lot by 10?", "2025-04-14 09:15:22"),
    ("climbchick42", "grip_master", "Perfect. I’ll bring the rope.", "2025-04-14 09:16:10"),
    ("grip_master", "climbchick42", "Awesome. I’ve got the draws and snacks.", "2025-04-14 09:17:03"),
    ("user3308", "chalkedup", "Hey, any interest in climbing this weekend? Weather looks solid.", "2025-04-15 08:42:00"),
    ("chalkedup", "user3308", "Heck yes! I’ve been itching to get on real rock again. Shelf Road?", "2025-04-15 08:45:17"),
    ("user3308", "chalkedup", "Perfect. I’ll bring a rack and my new fancy algorithm for optimizing anchor placements 😉", "2025-04-15 08:48:02"),
    ("chalkedup", "user3308", "As long as it doesn't crash halfway up the wall like your last app 😂", "2025-04-15 08:49:30"),
    ("user3308", "chalkedup", "Low blow 😆 That was one segmentation fault, okay?", "2025-04-15 08:50:10"),
    ("chalkedup", "user3308", "I'll forgive you if you finally send that slab you bailed on last time 😎", "2025-04-15 08:52:21"),
    ("user3308", "chalkedup", "Deal. I’ve been training... mostly grip strength and emotional resilience.", "2025-04-15 08:55:45"),
    ("chalkedup", "user3308", "Haha, classic. Alright, I’ll pack snacks and moral support. Let’s send.", "2025-04-15 08:58:00")
    ]

    c.executemany('''
    INSERT INTO messages (sender, receiver, content, timestamp)
    VALUES (?, ?, ?, ?)
    ''', messages)

    friendPairs = [
    ("climbchick42", "grip_master"),
    ("climbchick42", "chalkedup"),
    ("climbchick42", "rockhound"),
    ("grip_master", "chalkedup"),
    ("grip_master", "rockhound"),
    ("chalkedup", "rockhound"),
    ("user3308", "climbchick42"),
    ("user3308", "grip_master"),
    ("user3308", "rockhound"),
    ("user3308", "chalkedup")
    ]

    c.executemany('''
    INSERT INTO friends (user1, user2)
    VALUES (?, ?)
    ''', friendPairs)

    events = [
    ("Spring Climb", "2025-04-20", "Shelf Road, CO", 6, 1),
    ("Moonlight Bouldering", "2025-05-03", "Flagstaff Boulders, AZ", 4, 1),
    ("Cali Meetup", "2025-04-27", "Bishop, CA", 8, 1),
    ("Beginner Practice", "2025-05-10", "Movement Climbing Gym, Denver", 6, 1),
    ("CSPB peeps", "2025-05-05", "CU Boulder CS Building", 5, 1),
    ("4 Wheeling / Climb", "2025-04-25", "Indian Creek, UT", 5, 1),
    ("Small Group", "2025-05-01", "Eldorado Canyon, CO", 2, 1)
    ]

    c.executemany('''
    INSERT INTO events (eventTitle, eventDate, eventLocation, eventCapacity, eventRegistered)
    VALUES (?, ?, ?, ?, ?)
    ''', events)




    conn.commit()
    conn.close()

def print_tables(db_filename):
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    
    # Get list of tables (list of tuples) in the dtabase
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print("\nTables:")
    tables = c.fetchall()
    for t in tables:
        table_name = t[0]
        print(f"Table: {table_name}")

        # Column info for each table
        c.execute(f"PRAGMA table_info({table_name});")
        columns = c.fetchall()
        
        print("\tColumns:")
        for column in columns:
            print(f"\t\t{column[1]} (type: {column[2]})")
            
            
        print("")
        
    conn.close()
    
def print_rows(db_filename):
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()

    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print("\nData")
    tables = c.fetchall()
    for t in tables:
        table_name = t[0]
        print(f"Table: {table_name}")

        c.execute(f"SELECT * FROM {table_name};")
        rows = c.fetchall()

        if not rows:
            print("\t\t(No Data)")
        else:
            for row in rows:
                print(f"\t\t{row}")
        print("")

    conn.close()

if __name__ == '__main__':
    db_name = "test.db"

    create(db_name)

    fill(db_name)

    print_tables(db_name)

    print_rows(db_name)

