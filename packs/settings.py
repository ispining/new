from .DB_connector import *
from .bot_connector import *
from .langs import *


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


def back(user_id, callback_data):
    return types.InlineKeyboardButton(buttons(user_id, 'back'), callback_data=callback_data)


def staff(user_id, status=None, remove=False):
    sql.execute(f"""CREATE TABLE IF NOT EXISTS staff(
       user_id TEXT,
       status TEXT
       )""")
    db.commit()
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


