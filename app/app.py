import psycopg2
import os

from flask import Flask, render_template, session, request, redirect, url_for
from .seed_data import seed_database
from .db_create import createAll
from .db_utils import get_connection

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
    if os.getenv("ENV") != "development":  # only usable in dev environment
        return "Unauthorized", 403
    return createAll()


@app.route('/seed', methods=['GET'])
def run_seed():
    if os.getenv("ENV") != "development":  # only usable in dev environment
        return "Unauthorized", 403
    return seed_database()
    

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
