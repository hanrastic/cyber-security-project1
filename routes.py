import users
from app import app
import messages

from flask import render_template, request, redirect, session

@app.route("/")
def index():
    list = messages.get_all_messages_sql()
    return render_template("index.html", messages=list)


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
    #TO FIX FLAW 1 uncomment the line below
    #users.check_csrf()
    msg = request.form["message"]
    if messages.add_message_sql(msg):
        return redirect("/")
    else:
        return render_template("index.html")

@app.route("/result")
def search():
    query = request.args["query"]
    messages_found = messages.get_a_message_sql(query)
    if messages_found[0][0] == "No messages found":
        return render_template("error.html", message="No messages found")
    return render_template("result.html", messages=messages_found)
