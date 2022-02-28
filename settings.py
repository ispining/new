from db import *
from bot_connect import bot, types

def staff(user_id, new=None):
    sql.execute(f"SELECT * FROM staff WHERE user_id = '{str(user_id)}'")
    if sql.fetchone() is None:
        if new != None:
            sql.execute(f"INSERT INTO staff VALUES('{str(user_id)}', '{str(new)}')")
            db.commit()
    else:
        if new != None:
            sql.execute(f"UPDATE staff SET status = '{str(new)}' WHERE user_id = '{str(user_id)}'")
            db.commit()
        sql.execute(f"SELECT * FROM staff WHERE user_id = '{str(user_id)}'")
        for i in sql.fetchall():
            return i[0]
    
def markup():
    return types.InlineKeyboardMarkup()

def button_url(button_name, url):
    return types.InlineKeyboardButton(button_name, url=url)
    
def btn(button_name, callback_data):
    return types.InlineKeyboardButton(button_name, callback_data=callback_data)
    
def stages(user_id, new=None):
    result = "None"
    sql.execute(f"SELECT * FROM stages WHERE user_id = '{str(user_id)}'")
    if sql.fetchone() is None:
        if new != None:
            sql.execute(f"INSERT INTO stages VALUES ('{str(user_id)}', '{str(new)}')")
            db.commit()
            
    else:
        if new != None:
            sql.execute(f"UPDATE stages SET stage = '{str(new)}' WHERE user_id = '{str(new)}'")
            db.commit()
        sql.execute(f"SELECT * FROM stages WHERE user_id = '{str(user_id)}'")
        for i in sql.fetchall():
            result = i[1]
            
    return result

def th(target):
    threading_thread = threading.Thread(target=target)
    threading_thread.deamon = True
    threading_thread.start()

def lang(user_id, new=None):
    result = 'None'
    sql.execute(f"SELECT * FROM langs WHERE user_id = '{str(user_id)}'")
    if sql.fetchone() is None:
        if new != None:
            sql.execute(f"INSERT INTO langs VALUES('{str(user_id)}', '{str(new)}')")
            db.commit()
    else:
        if new != None:
            sql.execute(f"UPDATE langs SET lang = '{str(new)}' WHERE user_id = '{str(user_id)}'")
            db.commit()
        sql.execute(f"SELECT * FROM langs WHERE user_id = '{str(user_id)}'")
        for i in sql.fetchall():
            result = i[1]
    return result

def send(chat_id, text, reply_markup=None, disable_notification=False):
        return bot.send_message(chat_id, text, 
        reply_markup=reply_markup, 
        disable_notification=disable_notification)

def channels(user_id=None, msg_id=None, new=None):
    if msg_id != None:
        already = []
        sql.execute(f"SELECT * FROM channels")
        for i in sql.fetchall():
            if i[1] == str(msg_id):
                if i[2] not in already:
                    already.append(i[2])
        return already
    
    elif user_id != None:
        already = []
        sql.execute(f"SELECT * FROM channels WHERE user_id = '{str(user_id)}'")
        for i in sql.fetchall():
            if i[2] not in already:
                already.append(i[2])
        return already
    

print(staff(1))