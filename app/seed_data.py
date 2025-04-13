import os
import psycopg2

DATABASE_URL = os.getenv("DATABASE_URL")

def seed_database():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()

    try:
        # Check User table
        cur.execute('SELECT 1 FROM "user" WHERE "Username" = %s;', ('climbzRcool',))
        if cur.fetchone():
            print("Database already seeded, skipping.")
            return "Database already seeded, skipping."
        
        # Insert Styles
        cur.execute("""
        INSERT INTO "Style" (StyleName) VALUES
            ('Bouldering'), 
            ('Sport'), 
            ('Trad'), 
            ('Top-Rope'), 
            ('Indoor'), 
            ('Lead'), 
            ('Alpine'), 
            ('Aid'), 
            ('Mixed');
        """)

        # Insert Users
        cur.execute("""
        INSERT INTO "User" (Username, Email, State, City, Experience, Bio) VALUES
            ('climbzRcool', 'cool@climb.com', 'Colorado', 'Boulder', 5, 'Lover of granite'),
            ('chalkup', 'grip@protonmail.com', 'California', 'San Diego', 3, 'Sandstone specialist'),
            ('belayqueen', 'ropequeen@cruxmail.com', 'Utah', 'Moab', 7, 'Trad and tacos'),
            ('cruxjunkie', 'beta@stone.net', 'Nevada', 'Las Vegas', 4, 'Chasing the send in Red Rock'),
            ('dynoDan', 'hopskip@jumpmail.com', 'Oregon', 'Portland', 2, 'Boulders and beers'),
            ('racknrope', 'tradster@cragmail.com', 'Washington', 'Seattle', 6, 'Big walls and big coffee');
        """)

        # Insert Locations
        cur.execute("""
        INSERT INTO "Location" (Name, Style, State, City, Address, AverageRating, UserRating, Notes) VALUES
            ('Eldorado Canyon', 3, 'Colorado', 'Eldorado Springs', 'Eldorado Canyon State Park', 0.00, NULL, 'Classic trad routes'),
            ('Mission Cliffs Gym', 5, 'California', 'San Francisco', '2295 Harrison St', 0.00, NULL, 'Great indoor setting'),
            ('Indian Creek', 3, 'Utah', 'Moab', 'County Road 211', 0.00, NULL, 'Splitter cracks galore'),
            ('Red Rock Canyon', 3, 'Nevada', 'Las Vegas', 'Scenic Loop Dr', 0.00, NULL, 'Desert trad wonderland'),
            ('Planet Granite', 5, 'Oregon', 'Portland', '1405 NW 14th Ave', 0.00, NULL, 'Modern indoor bouldering and sport'),
            ('Index Town Wall', 3, 'Washington', 'Index', 'Index-Galena Rd', 0.00, NULL, 'Granite trad lines and runouts');
        """)

        # Insert Messages
        cur.execute("""
        INSERT INTO "Message" (SenderID, ReceiverID, Text, Timestamp) VALUES
            (1, 2, 'Hey! Climbing at The Spot this weekend?', NOW() - INTERVAL '2 days'),
            (2, 1, 'Sounds good! I''ll bring my gear.', NOW() - INTERVAL '1 day'),
            (3, 1, 'Up for a mission on El Cap?', NOW() - INTERVAL '5 days'),
            (1, 3, 'Absolutely Let''s do the Nose.', NOW() - INTERVAL '4 days'),
            (2, 3, 'Want to meet up in Moab for some cracks?', NOW() - INTERVAL '3 days'),
            (3, 2, 'I''m in. Been itching to climb that route!', NOW() - INTERVAL '2 days');
        """)

        # Insert Ratings
        cur.execute("""
        INSERT INTO "UserRating" (LocationID, UserID, Rating) VALUES
            (1, 1, 5), 
            (1, 2, 4), 
            (1, 3, 5),
            (2, 1, 3), 
            (2, 2, 5), 
            (2, 3, 4),
            (3, 1, 5), 
            (3, 2, 4), 
            (3, 3, 5);
        """)

        # Insert Events
        cur.execute("""
        INSERT INTO "Event" (HostID, DateTime, LocationID, PrimaryStyleID, SecondaryStyleID, Status, Notes) VALUES
            (1, '2025-04-15 09:00:00', 1, 1, NULL, 'going', 'Morning session at the local gym'),
            (2, '2025-04-16 18:30:00', 2, 2, 4, 'full', 'After-work climb, bring snacks!'),
            (3, '2025-04-17 14:00:00', 3, 3, NULL, 'not going', 'Weekend warm-up on the slab routes'),
            (1, '2025-04-18 10:00:00', 2, 4, 2, 'going', 'Trying some new routes today'),
            (2, '2025-04-19 08:00:00', 1, 1, NULL, 'not going', 'Weather turned bad — rescheduling'),
            (3, '2025-04-20 13:00:00', 3, 6, 9, 'full', 'Mixed styles today — all levels welcome');
        """)

        # Insert Buddy relationships
        cur.execute("""
        INSERT INTO "Buddy" (UserID, FriendID, Status) VALUES
            (1, 2, 'confirmed'), 
            (1, 3, 'pending'), 
            (2, 4, 'confirmed'), 
            (3, 1, 'declined'),
            (4, 5, 'confirmed'), 
            (5, 2, 'pending'), 
            (6, 1, 'confirmed'),
            (3, 6, 'confirmed'), 
            (2, 6, 'pending'), 
            (5, 3, 'declined');
        """)

        # Insert UserStyle
        cur.execute("""
        INSERT INTO "UserStyle" (UserID, StyleID) VALUES
            (1, 1),    -- climbzRcool, Bouldering
            (1, 3),    -- climbzRcool, Trad
            (2, 2),    -- chalkup, Sport
            (3, 3);    -- belayqueen, Trad
        """)

        conn.commit()
        print("Seed data inserted successfully!")
        return "Seed data inserted successfully!"

    except Exception as e:
        conn.rollback()
        print(f"Error inserting seed data: {e}")
        return f"Error inserting seed data: {e}"

    finally:
        cur.close()
        conn.close()
