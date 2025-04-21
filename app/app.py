import psycopg2
import os
from datetime import datetime
from urllib.parse import urlparse

from flask import Flask, render_template, session, request, redirect, url_for, flash
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


# for displaying experience level names on page
experience_levels = {
        1: "Gumby",
        2: "Crag Tourist",
        3: "Gear Junkie",
        4: "Rope Gun",
        5: "Beta Whisperer",
        6: "Crag Legend"
    }


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

@app.route('/add_buddy', methods=['POST'])
def add_buddy():
    if "username" not in session:
        flash("Please log in to add a buddy.", "error")
        return redirect(url_for('login'))
        
    user_id = session['userID']
    friend_id = request.form['FriendID']

    #preventing adding self as buddy
    if str(user_id) == friend_id:
        flash("You silly goose! You cannot add yourself as a buddy.", "error")
        return redirect(url_for('directory'))

    try:
        conn = get_connection()
        cur = conn.cursor()

        #checking if buddy pair already exists (in either direction)
        cur.execute('''
            SELECT 1 FROM "Buddy"
            WHERE (UserID = %s AND FriendID = %s)
            OR (UserID = %s AND FriendID = %s)
            ''', (user_id, friend_id, friend_id, user_id))
        if cur.fetchone():
            flash("This user is already your buddy!", "error")
            cur.close()
            conn.close()
            return redirect(url_for('directory'))
            
        #inserting into Buddy table
        sql = 'INSERT INTO "Buddy" (UserID, FriendID) VALUES (%s, %s)'
        cur.execute(sql, (user_id, friend_id))
        conn.commit()

        flash("Buddy added successfully!", "success")
    except psycopg2.Error as e:
        flash(f"Error adding Buddy: {e}", "error")
    finally:
        cur.close()
        conn.close()

    return redirect(url_for('directory'))
        

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
    username, email, fname, lname, state, city, xp, bio = records 

    cur.close()
    conn.close()

    experience_levels = {
        1: "Gumby",
        2: "Crag Tourist",
        3: "Gear Junkie",
        4: "Rope Gun",
        5: "Beta Whisperer",
        6: "Crag Legend"
    }

    if records:
        return render_template('profile.html', username=username, fname=fname, lname=lname, email=email, state=state, city=city, experience=experience_levels[xp], bio=bio)
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

    # looking only for events that haven't expired yet
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





@app.route('/messages', methods=['GET', 'POST'])
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

    # AUTOSCROLL to bottom of chat/conversation so the most recent is displayed?

    conn = get_connection()
    cur = conn.cursor()

    #run through all rows in buddy list looking for any pair (user1, user2) that contains userID
    cur.execute('''
        SELECT FriendID FROM "Buddy" WHERE UserID = %s
        UNION
        SELECT UserID FROM "Buddy" WHERE FriendID = %s
        ''', (userID, userID))
    buddy_ids = {row[0] for row in cur.fetchall()}   # grab the id of each friend (from either side of friendship)
    # print("buddy_ids:")
    # print(buddy_ids)

    buddy_names =[]
    for id in buddy_ids:       # collect names of friend buddies
        cur.execute('SELECT userid, username from "User" where userid = %s;', (id,))
        buddy_names.append(cur.fetchone())
    
    # print(buddy_names[0])
    chat_buddy_id = None       # to store selected buddy for chat

    messages = []      # to store messages

    if request.method == "POST":
        if 'buddy-id' in request.form:
            chat_buddy_id = int(request.form.get('buddy-id'))        # set buddy id to selected buddy in list
            print('selected buddy: ' + str(chat_buddy_id))


        elif 'msg' in request.form:     # if there is a message in the send form box, insert it into the Message table
            print('button worked')
            chat_buddy_id = int(request.form.get('msg-buddy-id'))  # pull buddy id back from form - keeps getting set to None on page load
            message = request.form.get('msg').strip()
            timestamp = datetime.now()

            print("message: " + message)
            print("timestamp: " + str(timestamp))
            print("chat buddy: " + str(chat_buddy_id))

            cur.execute('''
                INSERT INTO "Message" (senderid, receiverid, text, timestamp)
                VALUES (%s, %s, %s, %s);''', (userID, chat_buddy_id, message, timestamp))
            conn.commit()

    

    # load messages after selecting buddy or sending message
    if chat_buddy_id:
        cur.execute('''
            SELECT text, timestamp, senderid, receiverid FROM "Message"
            WHERE (senderid = %s AND receiverid = %s) OR (receiverid = %s AND senderid = %s)
            ORDER BY timestamp ASC;''', (userID, chat_buddy_id, chat_buddy_id, userID))
        
        messages_raw = cur.fetchall()

        cur.execute('SELECT username FROM "User" WHERE userid = %s;', (chat_buddy_id,))
        chat_buddy_name = cur.fetchone()


        # map to determine sender and recipient user names
        user_map = {userID: "You", chat_buddy_id: chat_buddy_name}

        messages = []
        for message in messages_raw:
            text, timestamp, senderID, receiverID = message
            messages.append({
                "text" : text,
                "time" : timestamp.strftime('%Y-%m-%d %H:%M'),
                "sender": user_map.get(senderID, "Unknown"),
                "receiver": user_map.get(receiverID, "unkown"),
                "sent_by_user": senderID == userID          # test if user is sender, for styling ()
            })





    return render_template('messages.html', buddy_names=buddy_names, messages=messages, chat_buddy_id=chat_buddy_id, userID=userID)



@app.route('/locations')
def locations():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('locations.html')




@app.route('/directory')
def directory():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    username = session.get('username')
    userID = session.get('userID')
    
    conn = get_connection()
    cur = conn.cursor()
    #fetch all users
    cur.execute('SELECT userid, username, firstname, lastname, state, city, experience FROM "User" ORDER BY lastname;')
    allUsers = cur.fetchall()

    #fetch current user's buddies (in either direction)
    cur.execute('''
        SELECT FriendID FROM "Buddy" WHERE UserID = %s
        UNION
        SELECT UserID FROM "Buddy" WHERE FriendID = %s
        ''', (userID, userID))
    buddy_ids = {row[0] for row in cur.fetchall()}
    
    # here I'm appending all the fetched data to a new array 'users' and replacing experience int with string, then passing the new array to the template
    users = []
    for user in allUsers:
        userID_val, username_val, firstname, lastname, state, city, xp = user
        users.append({
            "userID": userID_val,
            "username": username_val,
            "firstname": firstname,
            "lastname": lastname,
            "state": state,
            "city": city,
            "experience": experience_levels.get(xp, "Experience Level Unknown"),
            "is_buddy": userID_val in buddy_ids

        })

    cur.close()
    conn.close()
    
    # now go through budy list and find all buddies of current user (by userID)
    
        # would be nice here to include an 'add friend' button next to all users who are not yet friends.  
    # clicking add friend would add an entry to 'buddies' table where user1 and user2 are friends
    # we would want to make sure that no duplicates occur, maybe by removing 'add friend' button for buddies that are already friends
    # also make sure that table rows aren't duplicated, e.g., user1, user2 is the same as user2, user1

    return render_template('directory.html', users=users, current_user_id=userID)





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



