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

def get_a_message_sql(query):
    
    #FLAW 3
    #TO FIX FLAW 3 UNCOMMENT THREE LINES BELOW
    #sql = "SELECT M.message, U.username, M.sent_at FROM messages M, users U " \
    #       "WHERE M.user_id=U.id AND M.message LIKE :query"
    #query_result = db.session.execute(sql, {"query": query})

    #FLAW 3
    #TO FIX FLAW 3 REMOVE THREE LINES BELOW
    sql = "SELECT M.message, U.username, M.sent_at FROM messages M, users U " \
            "WHERE M.user_id=U.id AND M.message LIKE \'%" + query + "%\'"
    query_result = db.session.execute(sql)
    
    messages = query_result.fetchall()
    if len(messages) == 0:
        messages = [("No messages found",), ]
        return messages
    return messages


def get_all_messages_sql():
    sql = """SELECT M.message, U.username, M.sent_at, U.is_admin  
            FROM messages M, users U 
            WHERE M.user_id=U.id 
            ORDER BY M.sent_at DESC""" 

    result = db.session.execute(sql)
    return result.fetchall()

