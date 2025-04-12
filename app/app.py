from flask import Flask, render_template, session, request, redirect, url_for

app = Flask(__name__)
# lets try using a simple session and cookies to store user data
app.secret_key = 'burndownforwhat'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].strip()

        session['username'] = username
        return redirect(url_for('profile'))
    return render_template('login.html')

@app.route('/profile')
def profile():
    username = session.get('username')
    return render_template('profile.html', username=username)

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/messages')
def messages():
    return render_template('messages.html')

@app.route('/locations')
def locations():
    return render_template('locations.html')

@app.route('/create_profle')
def create_profile():
    return render_template('create_profile.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

if __name__ == '__main__':
    app.run(debug=True)