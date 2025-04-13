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

def createUser():
    sql = ''' DROP TABLE IF EXISTS "User";
        
            CREATE TABLE IF NOT EXISTS "User" (
            UserID SERIAL PRIMARY KEY,
            Username VARCHAR(45) NOT NULL UNIQUE,
            Email VARCHAR(45) NOT NULL UNIQUE,
            State VARCHAR(45) NOT NULL,
            City VARCHAR(45) NOT NULL,
            Experience INT NOT NULL,
            Bio TEXT
            ); '''
    return execute_query(sql, "User Table Successfully Created")

def createStyle():
    sql = ''' DROP TABLE IF EXISTS "Style";
        
            CREATE TABLE IF NOT EXISTS "Style" (
            StyleID SERIAL PRIMARY KEY,
            StyleName VARCHAR(45) NOT NULL UNIQUE
            ); '''
    return execute_query(sql, "Style Table Successfully Created")

def createLocation():
    sql = ''' DROP TABLE IF EXISTS "Location";
        
            CREATE TABLE IF NOT EXISTS "Location" (
            LocationID SERIAL PRIMARY KEY,
            Name VARCHAR(45) NOT NULL,
            Style INT NOT NULL,
            State VARCHAR(45) NOT NULL,
            City VARCHAR(45) NOT NULL,
            Address VARCHAR(45) NOT NULL,
            AverageRating DECIMAL(3, 2) NOT NULL,
            UserRating INT NULL,
            Notes TEXT NULL,
            CONSTRAINT FK_style FOREIGN KEY (Style) REFERENCES "Style"(StyleID)
            ); '''
    return execute_query(sql, "Location Table Successfully Created")

def createUserStyle():
    sql = ''' DROP TABLE IF EXISTS "UserStyle";
        
            CREATE TABLE IF NOT EXISTS "UserStyle" (
            UserID INT NOT NULL,
            StyleID INT NOT NULL,
            PRIMARY KEY (UserID, StyleID),
            CONSTRAINT FK_user FOREIGN KEY (UserID) REFERENCES "User"(UserID),
            CONSTRAINT FK_style FOREIGN KEY (StyleID) REFERENCES "Style"(StyleID)
            ); '''
    return execute_query(sql, "UserStyle Table Successfully Created")

def createUserRating():
    sql = ''' DROP TABLE IF EXISTS "UserRating";
        
            CREATE TABLE IF NOT EXISTS "UserRating" (
            RatingID SERIAL PRIMARY KEY,
            LocationID INT NOT NULL,
            UserID INT NOT NULL,
            Rating INT NOT NULL,
            CONSTRAINT FK_location FOREIGN KEY (LocationID) REFERENCES "Location"(LocationID),
            CONSTRAINT FK_user FOREIGN KEY (UserID) REFERENCES "User"(UserID)
            ); '''
    return execute_query(sql, "UserRating Table Successfully Created")

def createBuddy():
    sql = ''' DROP TABLE IF EXISTS "Buddy";
            DROP TYPE IF EXISTS status_enum;
        
            CREATE TYPE status_enum AS ENUM ('pending', 'confirmed', 'declined');
            CREATE TABLE IF NOT EXISTS "Buddy" (
            UserID INT NOT NULL,
            FriendID INT NOT NULL,
            Status status_enum NOT NULL,
            PRIMARY KEY (UserID, FriendID),
            CONSTRAINT FK_userid FOREIGN KEY (UserID) REFERENCES "User"(UserID),
            CONSTRAINT FK_friendid FOREIGN KEY (FriendID) REFERENCES "User"(UserID)
            ); '''
    return execute_query(sql, "Buddy Table Successfully Created")

def createMessage():
    sql = ''' DROP TABLE IF EXISTS "Message";
    
            CREATE TABLE IF NOT EXISTS "Message" (
            MessageID SERIAL PRIMARY KEY,
            SenderID INT NOT NULL,
            ReceiverID INT NOT NULL,
            Text TEXT NOT NULL,
            Timestamp TIMESTAMP NOT NULL,
            CONSTRAINT FK_sender FOREIGN KEY (SenderID) REFERENCES "User"(UserID),
            CONSTRAINT FK_receiver FOREIGN KEY (ReceiverID) REFERENCES "User"(UserID)
            ); '''
    return execute_query(sql, "Message Table Successfully Created")

def createEvent():
    sql = ''' DROP TABLE IF EXISTS "Event";
            DROP TYPE IF EXISTS status_enum2;
        
            CREATE TYPE status_enum2 AS ENUM ('going', 'not going', 'full');
            CREATE TABLE IF NOT EXISTS "Event" (
            EventID SERIAL PRIMARY KEY,
            HostID INT NOT NULL,
            ClimberID1 INT,
            ClimberID2 INT,
            ClimberID3 INT,
            ClimberID4 INT,
            ClimberID5 INT,
            DateTime TIMESTAMP NOT NULL,
            LocationID INT NOT NULL,
            PrimaryStyleID INT,
            SecondaryStyleID INT,
            Status status_enum2 NOT NULL,
            Notes TEXT,
            CONSTRAINT FK_host FOREIGN KEY (HostID) REFERENCES "User"(UserID),
            CONSTRAINT FK_climber1 FOREIGN KEY (ClimberID1) REFERENCES "User"(UserID),
            CONSTRAINT FK_climber2 FOREIGN KEY (ClimberID2) REFERENCES "User"(UserID),
            CONSTRAINT FK_climber3 FOREIGN KEY (ClimberID3) REFERENCES "User"(UserID),
            CONSTRAINT FK_climber4 FOREIGN KEY (ClimberID4) REFERENCES "User"(UserID),
            CONSTRAINT FK_climber5 FOREIGN KEY (ClimberID5) REFERENCES "User"(UserID),
            CONSTRAINT FK_location FOREIGN KEY (LocationID) REFERENCES "Location"(LocationID),
            CONSTRAINT FK_primstyle FOREIGN KEY (PrimaryStyleID) REFERENCES "Style"(StyleID),
            CONSTRAINT FK_secstyle FOREIGN KEY (SecondaryStyleID) REFERENCES "Style"(StyleID)
            ); '''
    return execute_query(sql, "Event Table Successfully Created")

def createTriggers():
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute('DROP TRIGGER IF EXISTS userrating_after_insert ON "UserRating";')
        cur.execute('DROP TRIGGER IF EXISTS userrating_after_update ON "UserRating";')
        cur.execute('DROP TRIGGER IF EXISTS userrating_after_delete ON "UserRating";')
        cur.execute('DROP FUNCTION IF EXISTS update_location_avg_rating();')

        cur.execute('''
            CREATE OR REPLACE FUNCTION update_location_avg_rating()
            RETURNS TRIGGER AS $$
            BEGIN
                UPDATE "Location"
                SET "AverageRating" = (
                    SELECT ROUND(COALESCE(AVG("Rating"), 0.00), 2)
                    FROM "UserRating"
                    WHERE "LocationID" = NEW."LocationID"
                )
                WHERE "LocationID" = NEW."LocationID";

                RETURN NEW;
            END;
            $$ LANGUAGE plpgsql;
        ''')

        cur.execute('''
            CREATE TRIGGER userrating_after_insert
            AFTER INSERT ON "UserRating"
            FOR EACH ROW
            EXECUTE FUNCTION update_location_avg_rating();
        ''')

        cur.execute('''
            CREATE TRIGGER userrating_after_update
            AFTER UPDATE ON "UserRating"
            FOR EACH ROW
            EXECUTE FUNCTION update_location_avg_rating();
        ''')

        cur.execute('''
            CREATE OR REPLACE FUNCTION update_location_avg_rating_on_delete()
            RETURNS TRIGGER AS $$
            BEGIN
                UPDATE "Location"
                SET "AverageRating" = (
                    SELECT ROUND(COALESCE(AVG("Rating"), 0.00), 2)
                    FROM "UserRating"
                    WHERE "LocationID" = OLD."LocationID"
                )
                WHERE "LocationID" = OLD."LocationID";

                RETURN OLD;
            END;
            $$ LANGUAGE plpgsql;
        ''')

        cur.execute('''
            CREATE TRIGGER userrating_after_delete
            AFTER DELETE ON "UserRating"
            FOR EACH ROW
            EXECUTE FUNCTION update_location_avg_rating_on_delete();
        ''')

        conn.commit()
        return "Triggers successfully created!"
    except Exception as e:
        conn.rollback()
        return f"Error creating triggers: {str(e)}"
    finally:
        cur.close()
        conn.close()

def createAll():
    """Create all tables and triggers in the correct order."""
    results = []
    results.append(createStyle())  # Must be first due to foreign key dependencies
    results.append(createUser())
    results.append(createLocation())
    results.append(createUserStyle())
    results.append(createUserRating())
    results.append(createBuddy())
    results.append(createMessage())
    results.append(createEvent())
    results.append(createTriggers())
    return "<br>".join(results)

if __name__ == "__main__":
    print(createAll())
