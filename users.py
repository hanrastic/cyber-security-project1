import os
import hashlib
from db import db
from flask import request, session, abort
from werkzeug.security import check_password_hash, generate_password_hash

def signup(username, password):

    #hash_value = hashlib.md5(password.encode()).hexdigest()

    hash_value = generate_password_hash(password)
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
    if not check_password_hash(user[1], password):
        return False
    
    session['username'] = username
    session['user_id'] = user[0]
    session['csrf_token'] = os.urandom(16).hex()

    return True