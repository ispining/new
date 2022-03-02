import random
import threading, texts, btns
from db import *
from bot_connect import bot, types
from posting_loop import *


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

def btn_url(button_name, url):
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
            sql.execute(f"UPDATE stages SET stage = '{str(new)}' WHERE user_id = '{str(user_id)}'")
            db.commit()
        else:
            sql.execute(f"SELECT * FROM stages")
            for i in sql.fetchone():
                if str(i[0]) == str(user_id):
                
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

def channels(user_id=None, chat_id=None, new=False):
    if chat_id != None:
        if new:
            sql.execute(f"SELECT * FROM ch WHERE ch_id = '{str(chat_id)}'")
            if sql.fetchone() is None:
                sql.execute(f"INSERT INTO ch VALUES('{str(random.randint(1, 99999999))}', '{chat_id}')")
                db.commit()
            else:
                return 404
        sql.execute(f"SELECT * FROM ch WHERE ch_id = '{str(chat_id)}'")
        if sql.fetchone() is None:
            return 404
        else:
            return True

    elif user_id != None:
        my_chats = []
        sql.execute(f"SELECT * FROM ch")
        if sql.fetchone() is None:
            pass
        else:
            sql.execute(f"SELECT * FROM ch")
            for i in sql.fetchall():
                if user_id not in g_admins(int(i[1])):
                    if i[1] not in my_chats:
                        my_chats.append(int(i[1]))
        return my_chats
    
def back(callback_data):
    return types.InlineKeyboardButton(btns.back, callback_data=callback_data)

def g_admins(chat_id):
    return bot.get_chat_administrators(chat_id)

th(the_loop)

