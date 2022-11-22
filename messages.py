import users
from db import db


def add_message_sql(msg):
    user_id = users.get_user_id()

    if user_id == 0:
        return False

    sql = """INSERT INTO messages (message, user_id, sent_at) 
            VALUES (:message, :user_id, NOW()::timestamp(0))"""

    db.session.execute(sql, {"message": msg, "user_id": user_id})
    db.session.commit()

    return True

def get_message():
    return True

def get_all_messages():
    sql = """SELECT M.message, U.username, M.sent_at 
            FROM messages M, users U 
            WHERE M.user_id=U.id 
            ORDER BY M.sent_at DESC""" 

    result = db.session.execute(sql)
    return result.fetchall()

