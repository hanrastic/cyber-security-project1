import os
import hashlib
from db import db
from flask import request, session, abort
from werkzeug.security import check_password_hash, generate_password_hash

def signup(username, password):

    hash_value = hashlib.sha1(password.encode()).hexdigest()

    #FLAW 2
    #TO FIX FLAW 2 UNCOMMENT THE LINE BELOW
    #hash_value = generate_password_hash(password)
    
    try:
        sql = """INSERT INTO users (username, password)
                VALUES (:username, :password)""" 
        db.session.execute(sql, {"username":username, "password": hash_value})
        db.session.commit()
    except:
        return False

    return login(username, password)


def login(username, password):
    sql = "SELECT id, password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()
    if not user:
        return False
        
    #FLAW 2 & 4
    #TO FIX FLAW 2 and 4 UNCOMMENT TWO LINES BELOW
    #if not check_password_hash(user[1], password):
    #    return False
    
    session['username'] = username
    session['user_id'] = user[0]
    #FLAW 1
    session['csrf_token'] = os.urandom(16).hex()

    return True

def get_user_id():
    return session.get("user_id", 0)

def logout():
    del session['user_id']
    del session['username']
    del session['csrf_token']

#FLAW 1
def check_csrf():
     if session['csrf_token'] != request.form['csrf_token']:
           abort(403)

