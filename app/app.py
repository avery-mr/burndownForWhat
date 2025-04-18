import psycopg2
import os
from datetime import datetime
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
    if 'username' in session:                          # checks if there is a user currently 'logged in'
        return redirect(url_for('profile'))
    if request.method == 'POST':                          # this get run when the user clicks 'Log In'
        username = request.form['username'].strip()       # assign the entered name to username

        conn = get_connection()
        cur = conn.cursor()
        cur.execute('SELECT userid FROM "User" WHERE Username = %s;', (username,))     # check if username exists in the database
        result = cur.fetchone()

        
        cur.close()
        conn.close()

        if result:     
            session['userID'] = result[0]                                          # if username does exist in database, assign it to session and redirect to profile page
            session['username'] = username
            print("username: " + session['username'] + ", userID: " + str(session['userID']) )
            return redirect(url_for('profile'))
        else: 
            error = "User does not exist"                         # if username is not in db, return error message
            return render_template('login.html', error=error)

    return render_template('login.html')




@app.route('/profile')
def profile():
    if 'username' not in session:                      # this is at the beginning of each route.  
        return redirect(url_for('login'))              # basically just checks if a user is logged in, if not send to login page.  This way someone can't navigate manually do page with url wihtout signing in
    username = session.get('username')                 # get logged in username from session

    conn = get_connection()
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

    
@app.route('/events', methods=['GET', 'POST'])
def events():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    username = session.get('username')
    conn = get_connection()
    cur = conn.cursor()


    if request.method == 'POST':
        # insert event from form here
        eventHostID = session.get('userID')
        eventTitle = request.form['event-title']
        eventDate = request.form['event-date']
        eventLocation = request.form['event-location'].strip()
        eventCapacity = request.form['event-count']
        eventRegistered = 1

        cur.execute('''
            INSERT INTO "Event" 
            (HostID, DateTime, Location, Capacity, Registered, Notes) 
            VALUES (%s, %s, %s, %s, %s, %s);''', (eventHostID, eventDate, eventLocation, eventCapacity, eventRegistered, eventTitle,))

        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('events'))

    # cur.execute('''
    #     SELECT * FROM "Event"
                
    #             ''')
    
    # print(cur.fetchone())
    cur.execute('''
        SELECT * from "Event"
        WHERE DateTime >= %s
        ORDER BY DateTime ASC
                
                ;''', (datetime.now(),))

    # cur.execute('SELECT eventid, datetime FROM "Event" ORDER BY datetime;')
    
    
    events = cur.fetchall()  
    print(events)  

    # It would be cool here to find a way to let the user click the join event button to register
    # would be nice if clicking register would increase the registered count
    # would be extra nice if user couldn't join an event they've already joined (same for host, but host should be automatically joined when creating the event)
    # Also cool if the event entry turned a color when it was full
    # even cooler if it could turn another color if user is registered and maybe get rid of join button

    # future what if:  add an expansion info area or popup for additional event details
    #                  add host name and possibly registered attendees names
    #                  add specific time of event in addition to date
    #                  add more precise location, etc


    cur.close()
    conn.close()

    return render_template('events.html', events=events)





@app.route('/messages')
def messages():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    username = session.get('username')
    userID = session.get('userID')

    # POPULATE MESSAGE BUDDIES LIST
    # not quite sure how to tackle this
    # something like SELECT * FROM "Message" WHERE userid == SenderID or userid == ReceiverID
    # but then appendUnique every sender/recipient who isn't the user so we have a list of ids of unique friends that the user has messaged.
    # Get friend username from "User" for each unique friend user id for display

    # AND THEN we still have to display only the mesages between user and friend, and find a way to switch between friends by selecting from the site


    return render_template('messages.html')

@app.route('/locations')
def locations():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('locations.html')

@app.route('/directory')
def directory():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM "User" ORDER BY lastname;')

    users = cur.fetchall()

    return render_template('directory.html', users=users)

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

 
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('''INSERT INTO "User" (username, email, firstname, lastname, state, city, experience, bio)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);''', (username, userEmail, firstName, lastName, userState, userCity, userXP, bio))
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



