import psycopg2
import os

from flask import Flask, render_template, session, request, redirect, url_for

app = Flask(__name__)
# lets try using a simple session and cookies to store user data
app.secret_key = 'burndownforwhat'

DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    return psycopg2.connect(DATABASE_URL)

@app.route('/db_test')
def testing():
    conn = get_connection()
    conn.close()
    return "Database Connection Successful"

@app.route('/db_createUser')
def createUser():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('''
            DROP TABLE IF EXISTS "User";
        
            CREATE TABLE IF NOT EXISTS "User" (
            UserID SERIAL PRIMARY KEY,
            Username VARCHAR(45) NOT NULL UNIQUE,
            Email VARCHAR(45) NOT NULL UNIQUE,
            State VARCHAR(45) NOT NULL,
            City VARCHAR(45) NOT NULL,
            Experience INT NOT NULL,
            Bio TEXT
            );
            ''')
        conn.commit()
        return "User Table Successfully Created"
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()


@app.route('/db_createStyle')
def createStyle():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('''
            DROP TABLE IF EXISTS "Style";
        
            CREATE TABLE IF NOT EXISTS "Style" (
            StyleID SERIAL PRIMARY KEY,
            StyleName VARCHAR(45) NOT NULL UNIQUE
            );
            ''')
        conn.commit()
        return "Style Table Successfully Created"
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()


@app.route('/db_createLocation')
def createLocation():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('''
            DROP TABLE IF EXISTS "Location";
        
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
            );
            ''')
        conn.commit()
        return "Location Table Successfully Created"
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()


@app.route('/db_createUserStyle')
def createUserStyle():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('''
            DROP TABLE IF EXISTS "UserStyle";
        
            CREATE TABLE IF NOT EXISTS "UserStyle" (
            UserID INT NOT NULL,
            StyleID INT NOT NULL,
            PRIMARY KEY (UserID, StyleID),
            CONSTRAINT FK_user FOREIGN KEY (UserID) REFERENCES "User"(UserID),
            CONSTRAINT FK_style FOREIGN KEY (StyleID) REFERENCES "Style"(StyleID)
            );
            ''')
        conn.commit()
        return "UserStyle Table Successfully Created"
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()


@app.route('/db_createUserRating')
def createUserRating():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('''
            DROP TABLE IF EXISTS "UserRating";
        
            CREATE TABLE IF NOT EXISTS "UserRating" (
            RatingID SERIAL PRIMARY KEY,
            LocationID INT NOT NULL,
            UserID INT NOT NULL,
            Rating INT NOT NULL,
            CONSTRAINT FK_location FOREIGN KEY (LocationID) REFERENCES "Location"(LocationID),
            CONSTRAINT FK_user FOREIGN KEY (UserID) REFERENCES "User"(UserID)
            );
            ''')
        conn.commit()
        return "UserRating Table Successfully Created"
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()


@app.route('/db_createBuddy')
def createBuddy():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('''
            DROP TABLE IF EXISTS "Buddy";
            DROP TYPE IF EXISTS status_enum;
        
            CREATE TYPE status_enum AS ENUM ('pending', 'confirmed', 'declined');
            CREATE TABLE IF NOT EXISTS "Buddy" (
            UserID INT NOT NULL,
            FriendID INT NOT NULL,
            Status status_enum NOT NULL,
            PRIMARY KEY (UserID, FriendID),
            CONSTRAINT FK_userid FOREIGN KEY (UserID) REFERENCES "User"(UserID),
            CONSTRAINT FK_friendid FOREIGN KEY (FriendID) REFERENCES "User"(UserID)
            );
            ''')
        conn.commit()
        return "Buddy Table Successfully Created"
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()


@app.route('/db_createMessage')
def createMessage():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('''
            DROP TABLE IF EXISTS "Message";
    
            CREATE TABLE IF NOT EXISTS "Message" (
            MessageID SERIAL PRIMARY KEY,
            SenderID INT NOT NULL,
            ReceiverID INT NOT NULL,
            Text TEXT NOT NULL,
            Timestamp TIMESTAMP NOT NULL,
            CONSTRAINT FK_sender FOREIGN KEY (SenderID) REFERENCES "User"(UserID),
            CONSTRAINT FK_receiver FOREIGN KEY (ReceiverID) REFERENCES "User"(UserID)
            );
            ''')
        conn.commit()
        return "Message Table Successfully Created"
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()
        

@app.route('/db_createEvent')
def createEvent():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('''
            DROP TABLE IF EXISTS "Event";
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
            CONSTRAINT FK_location FOREIGN KEY (LocationID) REFERENCES Location(LocationID),
            CONSTRAINT FK_primstyle FOREIGN KEY (PrimaryStyleID) REFERENCES Style(StyleID),
            CONSTRAINT FK_secstyle FOREIGN KEY (SecondaryStyleID) REFERENCES Style(StyleID)
            );
            ''')
        conn.commit()
        return "Event Table Successfully Created"
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()
                

@app.route('/db_createTriggers')
def createTriggers():
    conn = get_connection()
    cur = conn.cursor()

    try:
        # dropping existing triggers if they exist
        cur.execute('DROP TRIGGER IF EXISTS userrating_after_insert ON "UserRating";')
        cur.execute('DROP TRIGGER IF EXISTS userrating_after_update ON "UserRating";')
        cur.execute('DROP TRIGGER IF EXISTS userrating_after_delete ON "UserRating";')
        cur.execute('DROP FUNCTION IF EXISTS update_location_avg_rating();')

        # creating the trigger function
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

        # After INSERT Trigger
        cur.execute('''
            CREATE TRIGGER userrating_after_insert
            AFTER INSERT ON "UserRating"
            FOR EACH ROW
            EXECUTE FUNCTION update_location_avg_rating();
        ''')

        # After UPDATE Trigger
        cur.execute('''
            CREATE TRIGGER userrating_after_update
            AFTER UPDATE ON "UserRating"
            FOR EACH ROW
            EXECUTE FUNCTION update_location_avg_rating();
        ''')

        # After DELETE Trigger - slightly different logic since we reference OLD
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

@app.route('/', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('profile'))
    if request.method == 'POST':
        username = request.form['username'].strip()

        session['username'] = username
        return redirect(url_for('profile'))
    return render_template('login.html')

@app.route('/profile')
def profile():
    if 'username' not in session:
        return redirect(url_for('login'))
    username = session.get('username')
    return render_template('profile.html', username=username)

@app.route('/events')
def events():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('events.html')

@app.route('/messages')
def messages():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('messages.html')

@app.route('/locations')
def locations():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('locations.html')

@app.route('/create_profile', methods=['GET', 'POST'])
def create_profile():
    if request.method == 'POST':
        username = request.form['username'].strip()

        session['username'] = username
        return redirect(url_for('profile'))
    return render_template('create_profile.html')

@app.route('/logout')
def logout():
    if 'username' not in session:
        return redirect(url_for('login'))
    session.pop('username', None)
    return render_template('logout.html')

if __name__ == '__main__':
    app.run(debug=True)
