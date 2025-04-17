import psycopg2
import os
from urllib.parse import urlparse

from flask import Flask, render_template, session, request, redirect, url_for
from .seed_data import seed_database
from .db_create import createAll
from .db_drop import dropAll
from .db_utils import get_connection
from .db_selectAll import (
    selectUser,
    selectStyle,
    selectLocation,
    selectUserStyle,
    selectUserRating,
    selectBuddy,
    selectMessage,
    selectEvent
    )

app = Flask(__name__)
# lets try using a simple session and cookies to store user data
#app.secret_key = 'burndownforwhat'
app.secret_key = os.getenv("SECRET_KEY", "burndownforwhat")

# to connect to postgresql db from local deployment
def local_db_connect():
    url = urlparse("postgresql://belaybuddy_user:AtDkADwMJk9CGBWZdWxLvWS6IaVfksiq@dpg-cvti41be5dus73a9kcng-a.oregon-postgres.render.com/belaybuddy")
    conn = psycopg2.connect(
        dbname=url.path[1:], 
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port or 5432,
        sslmode='require'
        )
    return conn

@app.route('/db_test')
def testing():
    try:
        conn = get_connection()
        conn.close()
        return "Database Connection Successful"
    except Exception as e:
        return f"Database Connection Failed: {str(e)}", 500

@app.route('/db_init', methods=['GET'])
def init_db():
    return createAll()

@app.route('/db_drop', methods=['GET'])
def drop_db():
    return dropAll()

@app.route('/seed', methods=['GET'])
def run_seed():
    return seed_database()

@app.route('/db_selectUser')
def selectUser_db():
    return selectUser()

@app.route('/db_selectStyle')
def selectStyle_db():
    return selectStyle()

@app.route('/db_selectLocation')
def selectLocation_db():
    return selectLocation()

@app.route('/db_selectUserStyle')
def selectUserStyle_db():
    return selectUserStyle()

@app.route('/db_selectUserRating')
def selectUserRating_db():
    return selectUserRating()

@app.route('/db_selectBuddy')
def selectBuddy_db():
    return selectBuddy()

@app.route('/db_selectMessage')
def selectMessage_db():
    return selectMessage()

@app.route('/db_selectEvent')
def selectEvent_db():
    return selectEvent()
        

@app.route('/', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('profile'))
    if request.method == 'POST':
        username = request.form['username'].strip()

        conn = get_connection()
        # conn = local_db_connect()
        cur = conn.cursor()
        cur.execute('SELECT 1 FROM "User" WHERE Username = %s;', (username,))
        result = cur.fetchone()

        
        cur.close()
        conn.close()

        if result:
            session['username'] = username
            return redirect(url_for('profile'))
        else: 
            error = "User does not exist"
            return render_template('login.html', error=error)

    return render_template('login.html')




@app.route('/profile')
def profile():
    if 'username' not in session:
        return redirect(url_for('login'))
    username = session.get('username')
    try:
        conn = get_connection()
        # conn = local_db_connect()
        cur = conn.cursor()
        cur.execute('''
            SELECT Username, Email, FirstName, LastName, State, City, Experience, Bio
            FROM "User" WHERE Username = %s;''', (username,))
        records = cur.fetchone()
        username, email, fname, lname, state, city, experience, bio = records 
        cur.close()
        conn.close()
        if records:
            return render_template('profile.html', username=username, fname=fname, lname=lname, email=email, state=state, city=city, experience=experience, bio=bio)
        return "User not found", 404
    except Exception as e:
        return f"Error selecting User: {str(e)}", 500
    
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
        userEmail = request.form['userEmail'].strip()
        firstName = request.form['firstName'].strip()
        lastName = request.form['lastName'].strip()
        userCity = request.form['userCity'].strip()
        userState = request.form['userState'].strip()
        userXP = request.form['userXP'].strip()
        bio = request.form['bio']
        profilePic = request.form['profilePic'].strip()

 
        conn = get_connection()
        # conn = local_db_connect()
        cur = conn.cursor()
        cur.execute('''INSERT INTO "User" (username, email, firstname, lastname, state, city, experience, bio, picture)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);''', (username, userEmail, firstName, lastName, userCity, userState, userXP, bio, profilePic,))
        conn.commit()
        cur.close()
        conn.close()           
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



