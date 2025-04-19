import psycopg2
import os
from .db_utils import get_connection, execute_query


def createUser():
    sql = ''' 
            CREATE TABLE IF NOT EXISTS "User" (
            UserID SERIAL PRIMARY KEY,
            Username VARCHAR(45) NOT NULL UNIQUE,
            Email VARCHAR(45) NOT NULL UNIQUE,
            FirstName VARCHAR(45) NOT NULL,
            LastName VARCHAR(45) NOT NULL,
            State VARCHAR(45) NOT NULL,
            City VARCHAR(45) NOT NULL,
            Experience INT NOT NULL,
            Bio TEXT,
            Picture VARCHAR(45)
            ); '''
    return execute_query(sql, "User Table Successfully Created")

def createStyle():
    sql = '''         
            CREATE TABLE IF NOT EXISTS "Style" (
            StyleID SERIAL PRIMARY KEY,
            StyleName VARCHAR(45) NOT NULL UNIQUE
            ); '''
    return execute_query(sql, "Style Table Successfully Created")

def createLocation():
    sql = ''' 
            CREATE TABLE IF NOT EXISTS "Location" (
            LocationID SERIAL PRIMARY KEY,
            Name VARCHAR(45) NOT NULL,
            StyleID INT NOT NULL,
            State VARCHAR(45) NOT NULL,
            City VARCHAR(45) NOT NULL,
            Address VARCHAR(45) NOT NULL,
            AverageRating DECIMAL(3, 2) NOT NULL,
            UserRating INT NULL,
            Notes TEXT NULL,
            CONSTRAINT FK_style FOREIGN KEY (StyleID) REFERENCES "Style"(StyleID)
            ); '''
    return execute_query(sql, "Location Table Successfully Created")

def createUserStyle():
    sql = ''' 
            CREATE TABLE IF NOT EXISTS "UserStyle" (
            UserID INT NOT NULL,
            StyleID INT NOT NULL,
            PRIMARY KEY (UserID, StyleID),
            CONSTRAINT FK_user FOREIGN KEY (UserID) REFERENCES "User"(UserID),
            CONSTRAINT FK_style FOREIGN KEY (StyleID) REFERENCES "Style"(StyleID)
            ); '''
    return execute_query(sql, "UserStyle Table Successfully Created")

def createUserRating():
    sql = '''         
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
    sql = ''' 
            CREATE TABLE IF NOT EXISTS "Buddy" (
            UserID INT NOT NULL,
            FriendID INT NOT NULL,
            PRIMARY KEY (UserID, FriendID),
            CONSTRAINT FK_userid FOREIGN KEY (UserID) REFERENCES "User"(UserID),
            CONSTRAINT FK_friendid FOREIGN KEY (FriendID) REFERENCES "User"(UserID)
            CONSTRAINT no_self CHECK (UserID != FriendID)

            CREATE UNIQUE INDEX buddy_pair ON "Buddy" (
            LEAST(UserID, FriendID),
            GREATEST(UserID, FriendID)
            
            ); '''
    return execute_query(sql, "Buddy Table Successfully Created")

def createMessage():
    sql = '''     
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
    sql = ''' 
            CREATE TABLE IF NOT EXISTS "Event" (
            EventID SERIAL PRIMARY KEY,
            HostID INT NOT NULL,
            DateTime TIMESTAMP NOT NULL,
            Location VARCHAR(45) NOT NULL,
            Capacity INT NOT NULL,
            Registered INT NOT NULL,
            Notes TEXT,
            CONSTRAINT FK_host FOREIGN KEY (HostID) REFERENCES "User"(UserID)
            ); '''
    return execute_query(sql, "Event Table Successfully Created")

def createTriggers():
    try:
        conn = get_connection()
        cur = conn.cursor()

        sql_drop = '''
        DROP TRIGGER IF EXISTS userrating_after_insert ON "UserRating";
        DROP TRIGGER IF EXISTS userrating_after_update ON "UserRating";
        DROP TRIGGER IF EXISTS userrating_after_delete ON "UserRating";
        DROP FUNCTION IF EXISTS update_location_avg_rating();
        DROP FUNCTION IF EXISTS update_location_avg_rating_on_delete();
        '''
        cur.execute(sql_drop)

        sql_function = '''
        CREATE OR REPLACE FUNCTION update_location_avg_rating()
        RETURNS TRIGGER AS $$
        BEGIN
            UPDATE "Location"
            SET AverageRating = (
                SELECT ROUND(COALESCE(AVG(Rating), 0.00), 2)
                FROM "UserRating"
                WHERE LocationID = NEW.LocationID
            )
            WHERE LocationID = NEW.LocationID;
            RETURN NEW;
        END;
        $$ LANGUAGE plpgsql;

        CREATE TRIGGER userrating_after_insert
        AFTER INSERT ON "UserRating"
        FOR EACH ROW
        EXECUTE FUNCTION update_location_avg_rating();

        CREATE TRIGGER userrating_after_update
        AFTER UPDATE ON "UserRating"
        FOR EACH ROW
        EXECUTE FUNCTION update_location_avg_rating();

        CREATE OR REPLACE FUNCTION update_location_avg_rating_on_delete()
        RETURNS TRIGGER AS $$
        BEGIN
            UPDATE "Location"
            SET AverageRating = (
                SELECT ROUND(COALESCE(AVG(Rating), 0.00), 2)
                FROM "UserRating"
                WHERE LocationID = OLD.LocationID
            )
            WHERE LocationID = OLD.LocationID;
            RETURN OLD;
        END;
        $$ LANGUAGE plpgsql;

        CREATE TRIGGER userrating_after_delete
        AFTER DELETE ON "UserRating"
        FOR EACH ROW
        EXECUTE FUNCTION update_location_avg_rating_on_delete();
        '''
        cur.execute(sql_function)
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
