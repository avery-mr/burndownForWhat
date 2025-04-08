from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

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