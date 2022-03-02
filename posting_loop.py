import datetime
from db import *


def str_to_time(str_time):
    return datetime.datetime.strptime(str(str_time), '%Y-%m-%d %H:%M:%S.%f')


def timer(msg_id, new_mins=None, new_last_time=None):
    result = None

    sql.execute(f"SELECT * FROM ads WHERE id = '{str(msg_id)}'")
    if sql.fetchone() is None:
        pass
    else:
        if new_mins != None:
            sql.execute(f"""UPDATE ads SET minutes = '{str(new_mins)}' id = '{str(msg_id)}'""")
            db.commit()
        if new_last_time != None:
            sql.execute(f"""UPDATE ads SET last_time = '{str(new_last_time)}' WHERE id = '{str(msg_id)}'""")
            db.commit()
        sql.execute(f"SELECT * FROM ads WHERE id = '{str(msg_id)}'")
        for i in sql.fetchall():
            if i[6] == 'None' and i[5] != 'None':
                result = {'minutes': i[5], 'last_post': None}
            elif i[5] == 'None' and i[6] != 'None':
                result = {'minutes': None, 'last_post': str_to_time(i[6])}
            elif i[5] != 'None' and i[6] != 'None':
                result = {'minutes': i[5], 'last_post': str_to_time(i[6])}
            else:
                result = {'minutes': None, 'last_post': None}

    return result


def wallet_action(user_id):
    pass


def msg_k(msg_id):
    k = markup()
    sql.execute(f"SELECT * FROM btn WHERE msg_id = '{str(msg_id)}'")
    if sql.fetchone() is None:
        pass
    else:
        sql.execute(f"SELECT * FROM btn WHERE msg_id = '{str(msg_id)}'")
        for i in sql.fetchall():
            b = None
            if i[3] == "call":
                k.row(btn(i[2], i[4]))
            elif i[3] == 'url':
                k.row(btn_url(i[2], i[4]))
    return k


def the_ad(msg_id):
    sql.execute(f"SELECT * FROM ads WHERE id = '{str(msg_id)}'")
    for i in sql.fetchall():
        chat = None
        sql.execute(f"SELECT * FROM channels WHERE msg_id = '{str(msg_id)}'")
        for i in sql.fetchall():
            chat = int(i[1])
        media_type = i[2]
        media = i[3]
        text = i[4]
        user_id = int(i[1])
        try:
            if media_type == 'photo':
                bot.send_photo(
                    chat_id = chat,
                    photo = media,
                    caption = text,
                    reply_markup = msg_k(msg_id)
                    )
            elif media_type == "video":
                bot.send_video(
                    chat_id = chat,
                    data = media,
                    caption = text,
                    reply_markup = msg_k(msg_id)
                    )
            wallet_action(user_id)
        except:
            pass


def the_loop():
    while True:
        try:
            sql.execute(f"SELECT * FROM ads")
            if sql.fetchone() is None:
               pass
            else:
               sql.execute(f"SELECT * FROM ads")
               for i in sql.fetchall():
                    mins = timer(int(i[0]))['minutes']
                    last_post = timer(int(i[0]))['last_post']
                    next_post = last_post + datetime.timedelta(minutes=mins)
                    if next_post < datetime.datetime.now():
                        the_ad(int(i[0]))
        except:
            pass
            
            