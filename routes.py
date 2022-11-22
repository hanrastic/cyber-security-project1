import users
from app import app
import messages

from flask import render_template, request, redirect, session

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.signup(username, password):
            return redirect("/")
        else:
            return redirect("/login")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not users.login(username, password):
            return render_template("error.html", message="Wrong username or password")
        return redirect('/')

@app.route('/logout')
def logout():
    users.logout()
    return redirect('/')


@app.route("/createmessage")
def createmessage():
    return render_template("createmessage.html")

@app.route("/sendmessage", methods =['POST'])
def sendmessage():
    msg = request.form["message"]
    if messages.add_message_sql(msg):
        return redirect("/")
    else:
        return render_template("index.html")