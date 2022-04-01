from .DB_connector import *
from .bot_connector import *
from .langs import *
import threading, random


def th(target):
    thread = threading.Thread(target=target, daemon=True)
    thread.start()
    
def send(chat_id, msg, reply_markup=None, disable_notification=False):
    bot.send_message(chat_id, msg, reply_markup=reply_markup, disable_notification=disable_notification, parse_mode='HTML')

def kmarkup():
    return types.InlineKeyboardMarkup()

def down_file(file_id, name):
    file_info = bot.get_file(file_id)

    downloaded_file = bot.download_file(file_info.file_path)


    with open(name, 'wb') as new_file:
        new_file.write(downloaded_file)
    return {'file_id': file_id,
            'status': 200}

def btn(name, callback_data=None, url=None):
    if callback_data!=None:
        return types.InlineKeyboardButton(name, callback_data=callback_data)
    elif url!=None:
        return types.InlineKeyboardButton(name, url=url)

def back(callback_data):
    return types.InlineKeyboardButton('Назад', callback_data=callback_data)

def staff(user_id, status=None, remove=False):
    
    if status == None:
        if remove == False:
            s = None
            sql.execute(f"SELECT * FROM staff WHERE user_id = '{str(user_id)}'")
            if sql.fetchone() is None:
                pass
            else:
                sql.execute(f"SELECT * FROM staff WHERE user_id = '{str(user_id)}'")
                for i in sql.fetchall():
                    s = i[1]
            return s
        elif remove == True:
            sql.execute(f"SELECT * FROM staff WHERE user_id = '{str(user_id)}'")
            if sql.fetchone() is None:
                pass
            else:
                sql.execute(f"DELETE FROM staff WHERE user_id = '{str(user_id)}'")
                db.commit()
    elif status != None:
        sql.execute(f"SELECT * FROM staff WHERE user_id = '{str(user_id)}'")
        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO staff VALUES('{str(user_id)}','{str(status)}')")
            db.commit()
        else:
            sql.execute(f"UPDATE staff SET status = '{str(status)}' WHERE user_id = '{str(user_id)}'")
            db.commit()

def stages(user_id, stage=None):
    sql.execute(f"""CREATE TABLE IF NOT EXISTS stages(
    user_id TEXT,
    stage TEXT
    )""")
    db.commit()
    if stage == None:
        s = "None"
        sql.execute(f"SELECT * FROM stages WHERE user_id = '{str(user_id)}'")
        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO stages VALUES('{str(user_id)}','{s}')")
            db.commit()
        else:
            sql.execute(f"SELECT * FROM stages WHERE user_id = '{str(user_id)}'")
            for i in sql.fetchall():
                s = i[1]
        return s

    elif stage != None:
        sql.execute(f"SELECT * FROM stages WHERE user_id = '{str(user_id)}'")
        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO stages VALUES('{str(user_id)}','{str(stage)}')")
            db.commit()
        else:
            sql.execute(f"UPDATE stages SET stage = '{str(stage)}' WHERE user_id = '{str(user_id)}'")
            db.commit()

def add_button(user_id, button_id, callback_data=None, url=None):
    if callback_data == None and url == None:
        return types.InlineKeyboardButton(buttons(user_id, str(button_id)), callback_data=button_id)
    elif callback_data != None and url == None:
        return types.InlineKeyboardButton(buttons(user_id, str(button_id)), callback_data=callback_data)
    elif callback_data == None and url != None:
        return types.InlineKeyboardButton(buttons(user_id, str(button_id)), url=str(url))

def plist():
    result = []
    sql.execute(f"SELECT * FROM our_group")
    if sql.fetchone() is None:
        pass
    else:
        sql.execute(f"SELECT * FROM our_group")
        for i in sql.fetchall():
            if str(i[2]) not in result:
                if str(i[2]) != 'None':
                    result.append({'place':str(i[3]),
                                'id':int(i[0])})
    return result

def glist():
    result = []
    sql.execute(f"SELECT * FROM our_group")
    if sql.fetchone() is None:
        pass
    else:
        sql.execute(f"SELECT * FROM our_group")
        for i in sql.fetchall():
            result.append(int(i[1]))
    return result

def catlist():
    result = []
    for gid in glist():
        category = ginfo(gid)['category']
        tid = ginfo(gid)['id']
        if category not in result:
            if category != "None":
                result.append({
                    'id': tid,
                    'category': category
                })
    return result

def ginfo(gid):
    sql.execute(f"SELECT * FROM our_group WHERE chat_id = '{str(gid)}'")
    if sql.fetchone() is None:
        return None
    else:
        sql.execute(f"SELECT * FROM our_group WHERE chat_id = '{str(gid)}'")
        for i in sql.fetchall():
            return {
                'id': int(i[0]),
                "gid":int(i[1]), 
                "category":i[2], 
                "place":i[3]
            }

def gsetcat(gid, category):
    sql.execute(f"SELECT * FROM our_group WHERE chat_id = '{str(gid)}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO our_group VALUES('{str(random.randint(0, 99999999))}', {str(gid)}', '{str(category)}', 'None')")
        db.commit()
            
    else:
        sql.execute(f"UPDATE our_group SET category = '{str(category)}' WHERE chat_id = '{str(gid)}'")
        db.commit()

def gsetplace(gid, place):
    sql.execute(f"SELECT * FROM our_group WHERE chat_id = '{str(gid)}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO our_group VALUES('{str(random.randint(0, 99999999))}', '{str(gid)}', 'None', '{str(place)}')")
        db.commit()
            
    else:
        sql.execute(f"UPDATE our_group SET place = '{str(place)}' WHERE chat_id = '{str(gid)}'")
        db.commit()

def ginfo_with_id(id_in_db):
    sql.execute(f"SELECT * FROM our_group WHERE id = '{str(id_in_db)}'")
    if sql.fetchone() is None:
        return None
    else:
        sql.execute(f"SELECT * FROM our_group WHERE id = '{str(id_in_db)}'")
        for i in sql.fetchall():
            return {
                'id': int(i[0]),
                "gid":int(i[1]), 
                "category":i[2], 
                "place":i[3]
            }

def del_msgs_set_default(gid):
    sql.execute(f"""INSERT INTO msg_dels VALUES(
        '{str(gid)}',
        'on',
        'on',
        'on',
        'on',
        'off'
        )""")
    db.commit()

def get_msg_dels(gid):
    sql.execute(f"SELECT * FROM msg_dels WHERE gid = '{str(gid)}'")
    for i in sql.fetchall():
        return {
            "chat_id": int(i[0]),
            "join": str(i[1]),
            "exit": str(i[2]),
            'photo': str(i[3]),
            "title": str(i[4]),
            "pinned": str(i[5])
        }

def service_dels_keys(k, gid):
    join = btn('Join', callback_data=f"g")
    join_on = btn('✔️', callback_data=f"set_g_{str(gid)}_del_join_on")
    join_off = btn('✖️', callback_data=f"set_g_{str(gid)}_del_join_off")
    exit = btn('Exit', callback_data=f"j")
    exit_on = btn('✔️', callback_data=f"set_g_{str(gid)}_del_exit_on")
    exit_off = btn('✖️', callback_data=f"set_g_{str(gid)}_del_exit_off")
    photo = btn('New Photo', callback_data="s")
    photo_on = btn('✔️', callback_data=f"set_g_{str(gid)}_del_photo_on")
    photo_off = btn('✖️', callback_data=f"set_g_{str(gid)}_del_photo_off")
    title = btn('New Title', callback_data=f"l")
    title_on = btn('✔️', callback_data=f"set_g_{str(gid)}_del_title_on")
    title_off = btn('✖️', callback_data=f"set_g_{str(gid)}_del_title_off")
    pinned = btn('Pinned', callback_data=f"q")
    pinned_on = btn('✔️', callback_data=f"set_g_{str(gid)}_del_pinned_on")
    pinned_off = btn('✖️', callback_data=f"set_g_{str(gid)}_del_pinned_off")
    k.row(join, join_on, join_off)
    k.row(exit, exit_on, exit_off)
    k.row(photo, photo_on, photo_off)
    k.row(title, title_on, title_off)
    k.row(pinned, pinned_on, pinned_off)

def fuck(message, todo, until=None):
    gid = message.chat.id
    user_id = message.from_user.id
    comm = todo.split('||')
    sql.execute(f"SELECT * FROM fuck WHERE gid = '{str(gid)}'")
    if sql.fetchone() is None:
        pass
    else:
            if "mute" in comm:
                if until == None:
                    try:
                        bot.restrict_chat_member(gid, user_id)
                    except:
                        pass
                elif until != None:
                    try:
                        bot.restrict_chat_member(gid, 
                                            user_id, 
                                            until_date=until)
                    except:
                        pass
                    
            elif "ban" in comm:
                try:
                    bot.kick_chat_member(gid, user_id)
                except:
                    pass

            elif "delete" in comm:
                try:
                    bot.delete_message(chat_id, message.message_id)
                except:
                    pass
    
            elif "kick" in comm:
                try:
                    bot.kick_chat_member(gid, user_id)
                except:
                    pass

def group_switch(gid, switch_name, new_state=None, new_fuck=None, new_alert=None):
    com = f"SELECT * FROM gswitches WHERE gid = '{str(gid)}' AND switch_name = '{str(switch_name)}'"
    sql.execute(com)
    if sql.fetchone() is None:
        sql.execute(f"""INSERT INTO gswitches VALUES(
            '{str(gid)}', 
            '{str(switch_name)}',
            'True',
            'None',
            'False'
            )""")
        db.commit()
    if new_state != None:
        sql.execute(f"""UPDATE gswitches 
        SET switch = '{str(new_state)}' 
        WHERE gid = '{str(gid)}' 
        AND switch_name = '{str(switch_name)}'""")
        db.commit()
    if new_fuck != None:
        sql.execute(f"""UPDATE gswitches 
        SET fuck = '{str(new_fuck)}' 
        WHERE gid = '{str(gid)}' 
        AND switch_name = '{str(switch_name)}'""")
        db.commit()
    if new_alert != None:
        sql.execute(f"""UPDATE gswitches 
        SET alert = '{str(new_alert)}' 
        WHERE gid = '{str(gid)}' 
        AND switch_name = '{str(switch_name)}'""")
        db.commit()
    sql.execute(com)
    for i in sql.fetchall():
        return {
            "gid": int(i[0]),
            "switch_name": i[1],
            "switch": i[2].lower() in ['true', 'on'],
            "fuck": i[3],
            "alert": i[4].lower() in ['true', 'off']
        }

def anti_bots(message):
    gid = message.chat.id
    user_id = message.from_user.id
    username = message.chat.username
    
    if message.chat.type != "private":
        if username != None:
            ulast = username[:3].lower()
            ufirst = username[len(username)-3:].lower()
            if ufirst == "bot":
                ### IF SWITCH ###
                if group_switch(gid, "delete_bots")["switch"]:
                    return bot.kick_chat_member(chat_id, user_id)


