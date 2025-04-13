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
