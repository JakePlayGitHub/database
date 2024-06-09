# app.py

from flask import Flask, render_template, request, url_for, redirect, session
import database

app = Flask(__name__)
app.secret_key = 'sessionkey'

@app.route('/')
def start_page():
    return render_template('index.html')

@app.route('/home')
def home():
    username = session.get('username')
    if username:
        return render_template('home.html', username=username)
    else:
        return redirect(url_for('login_page'))

@app.route('/login', methods=["POST", "GET"])
def login_page():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        if database.login_user(username, password):
            session['username'] = username
            return redirect(url_for('home'))
        else:
            error = "Invalid username or password"
            return render_template('login.html', error=error)
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('start_page'))

@app.route('/register', methods=["POST", "GET"])
def register():

    if request.method == "POST":

        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')

        database.create_user(username, password, email)

    return render_template('register.html')

if __name__ == "__main__":
    app.run(debug=True, host='192.168.0.220')
