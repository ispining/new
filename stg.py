from .settings import *
import random


def lang_stage(message, gid):
    chat_id = message.chat.id
    k = kmarkup()
    msg = lang_stg
    k.row(types.InlineKeyboardButton('English', callback_data=f"set_en_{str(gid)}"))
    k.row(types.InlineKeyboardButton('Русский', callback_data=f"set_ru_{str(gid)}"))
    send(chat_id, msg, reply_markup=k)

def start_message(message):
    chat_id = message.chat.id
    sql.execute("DELETE FROM our_group WHERE category ='None'")
    db.commit()
    sql.execute("DELETE FROM our_group WHERE place ='None'")
    db.commit()
    k = kmarkup()
    msg = welcome_msg
    k.row(types.InlineKeyboardButton(k_our_group, callback_data="our_group"))
    #k.row(types.InlineKeyboardButton(k_set_lang, callback_data="s_lang"))
    send(chat_id, msg, reply_markup=k)

# add_new_group
def ang(message):
    chat_id = message.chat.id
    d=False
    gid=None
    try:
        gid = int(message.text)
        try: 
            gid = bot.get_chat(gid).id
            d=True
        except:
            send(chat_id, 'Добавь бот в группу')
    except:
        send(chat_id, 'Разрешены только цифры')
    if d:
        r_id = random.randint(0, 99999999)
        sql.execute(f"INSERT INTO our_group VALUES('{str(r_id)}', '{str(gid)}', 'None', 'None')")
        db.commit()
        stages(chat_id, stages(chat_id) + '_' + str(r_id))
        k = kmarkup()
        msg = add_new_group_1
        k.row(btn(k_add_new, callback_data="add_place_"+str(gid)))
        for p in plist():
            try:
                k.row(btn(p['place'], callback_data=f"add_place_{str(gid)}_{str(p['id'])}"))
            except:
                pass
        k.row(back('our_group'))
        send(chat_id, msg, reply_markup=k)

def dels_stg(chat_id, gid):
    k = kmarkup()
    b1 = btn(k_service_msgs, callback_data=f"manage_{str(gid)}_dels_service")
    b2 = btn(k_commands, callback_data=f"manage_{str(gid)}_dels_command")
    msg = dels_stg_msg
    k.row(b1)
    k.row(b2)
    k.row(back(f"manage_{str(gid)}"))
    send(chat_id, msg, reply_markup=k)
    
def service_dels(chat_id, gid):
    #del_msgs_set_default(gid)
    k = kmarkup()
    msg = service_msgs.format(**{
        "join": get_msg_dels(gid)['join'],
        "exit": get_msg_dels(gid)['exit'],
        "photo": get_msg_dels(gid)['photo'],
        "title": get_msg_dels(gid)['title'],
        "pinned": get_msg_dels(gid)['pinned']
    })
    service_dels_keys(k, gid)
    k.row(back(f"manage_{str(gid)}_dels"))
    send(chat_id, msg, reply_markup=k)
    
def del_comms(gid, chat_id):
    
    k = kmarkup()
    status = "Деактивирован"
    
    if group_switch(gid, "delete_comms")["switch"]:
        status = "Активирован"
    msg = del_commands.format(**{
        "gtitle": bot.get_chat(gid).title,
        "status": status
        })
    k.row(btn("On", callback_data=f"manage_{str(gid)}_dels_commands_on"), btn("Off", callback_data=f"manage_{str(gid)}_dels_commands_off"))
    k.row(back(f"manage_{str(gid)}_dels"))
    send(chat_id, msg, reply_markup=k)
    
def setfucks(gid, chat_id):
    ns = "off"
    if group_switch(gid, "banned_words")["switch"]:
        ns = "on"
    group_switch(gid, "banned_words", new_state=ns)
    bw_stg(gid, chat_id)
    dm()

def manage(chat_id, gid):
    k = kmarkup()
    
    msg = mng_text.format(**{'title': bot.get_chat(int(gid)).title})
    close = btn(k_close, callback_data=f"close")
    del_msgs = btn(k_del_msgs, 
                callback_data=f"manage_{str(gid)}_dels")
    chat_lang = btn(k_chat_lang, callback_data=f"manage_{str(gid)}_lang")
    bw = btn(k_bw, callback_data=f"manage_{str(gid)}_bw")
    k.row(bw)
    k.row(del_msgs)
    k.row(chat_lang, close)
    send(chat_id, msg, reply_markup=k)

def bw_stg(gid, chat_id):
    k = kmarkup()
    msg = bw_msg.format(**{"gtitle": bot.get_chat(gid).title})
    k.row(btn(k_fuck, f"manage_{str(gid)}_bw_fuck"))
    k.row(btn(k_activate, callback_data=f"manage_{str(gid)}_bw_switch"))
    k.row(back(f"manage_{str(gid)}"))
    send(chat_id, msg, reply_markup=k)
