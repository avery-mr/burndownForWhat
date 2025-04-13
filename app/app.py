import psycopg2

from flask import Flask, render_template, session, request, redirect, url_for

app = Flask(__name__)
# lets try using a simple session and cookies to store user data
app.secret_key = 'burndownforwhat'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://belaybuddy_user:AtDkADwMJk9CGBWZdWxLvWS6IaVfksiq@dpg-cvti41be5dus73a9kcng-a/belaybuddy")
    conn.close()
    return "Database Connection Successful"

@app.route('/db_createUser')
def createUser():
    conn = psycopg2.connect("postgresql://belaybuddy_user:AtDkADwMJk9CGBWZdWxLvWS6IaVfksiq@dpg-cvti41be5dus73a9kcng-a/belaybuddy")
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
    cur.close()
    conn.close()
    return "User Table Successfully Created"

@app.route('/db_createBuddy')
def createBuddy():
    conn = psycopg2.connect("postgresql://belaybuddy_user:AtDkADwMJk9CGBWZdWxLvWS6IaVfksiq@dpg-cvti41be5dus73a9kcng-a/belaybuddy")
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
    cur.close()
    conn.close()
    return "Buddy Table Successfully Created"

@app.route('/db_createMessage')
def createUser():
    conn = psycopg2.connect("postgresql://belaybuddy_user:AtDkADwMJk9CGBWZdWxLvWS6IaVfksiq@dpg-cvti41be5dus73a9kcng-a/belaybuddy")
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE IF EXISTS "Message";
        
        CREATE TABLE IF NOT EXISTS "Message" (
        MessageID SERIAL PRIMARY KEY,
        SenderID INT NOT NULL,
        ReceiverID INT NOT NULL,
        Text TEXT NOT NULL,
        Timestamp DATETIME NOT NULL
        CONSTRAINT FK_sender FOREIGN KEY (SenderID) REFERENCES "User"(UserID),
        CONSTRAINT FK_receiver FOREIGN KEY (ReceiverID) REFERENCES "User"(UserID)
        );
        ''')
    conn.commit()
    cur.close()
    conn.close()
    return "Message Table Successfully Created"

@app.route('/db_createStyle')
def createUser():
    conn = psycopg2.connect("postgresql://belaybuddy_user:AtDkADwMJk9CGBWZdWxLvWS6IaVfksiq@dpg-cvti41be5dus73a9kcng-a/belaybuddy")
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE IF EXISTS "Style";
        
        CREATE TABLE IF NOT EXISTS "Style" (
        StyleID SERIAL PRIMARY KEY,
        StyleName VARCHAR(45) NOT NULL UNIQUE;
        );
        ''')
    conn.commit()
    cur.close()
    conn.close()
    return "Style Table Successfully Created"

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
