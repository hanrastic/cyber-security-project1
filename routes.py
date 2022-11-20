import hashlib
import users
from app import app

from flask import render_template, request, redirect, session

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        return redirect("/")

@app.route('/signup', methods=["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        hash_value = hashlib.md5(password.encode()).hexdigest()
        # users.register(username, hash_value)
        return redirect("/")


