from flask import Flask, request, render_template, redirect, url_for
from server import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(f"Login Attempt: {username}")
        if correct_credentials(username, password):
            return redirect(url_for('main'))
        else:
            return {'error' : 'Incorrect Credentials'}
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        name = request.form.get("name")
        new(username, name, email, password)
        return redirect(url_for('main'))
    return render_template('signup.html')

@app.route('/main', methods=['GET', 'POST'])
def main():
    return render_template('main.html')

@app.route('/stox/tickers', methods=['GET', 'POST'])
def stox():
    if request.method == 'POST':
        comapany_ticker = request.form.ticker('ticker')
        

if __name__ == "__main__":
    app.run(debug=True)