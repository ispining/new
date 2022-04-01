from packs.settings import *
from packs.stg import *

@bot.message_handler(content_types=['new_chat_members'])
def del_joins_in_group(message):
    user_id = message.from_user.id
    gid = message.chat.id
    if gid in glist():
        if get_msg_dels(gid)["join"] == "on":
            bot.delete_message(message.chat.id, message.message_id)
    ab = anti_bots(message)
    if ab != None:
        bot.delete_message(ab.chat.id, ab.message_id)

@bot.message_handler(content_types=['left_chat_member'])
def del_exits_in_group(message):
    user_id = message.from_user.id
    gid = message.chat.id
    if gid in glist():
        if get_msg_dels(gid)["exit"] == "on":
            bot.delete_message(message.chat.id, message.message_id)

@bot.message_handler(content_types=["pinned_message"])
def del_pinned_in_group(message):
    user_id = message.from_user.id
    gid = message.chat.id
    if gid in glist():
        if get_msg_dels(gid)["pinned"] == "on":
            bot.delete_message(message.chat.id, message.message_id)
    
@bot.message_handler(content_types=["new_chat_title"])
def del_title_in_group(message):
    user_id = message.from_user.id
    gid = message.chat.id
    if gid in glist():
        if get_msg_dels(gid)["title"] == "on":
            bot.delete_message(message.chat.id, message.message_id)

@bot.message_handler(content_types=["new_chat_photo", "delete_chat_photo"])
def del_nw_photo_in_group(message):
    user_id = message.from_user.id
    gid = message.chat.id
    if gid in glist():
        if get_msg_dels(gid)["photo"] == "on":
            bot.delete_message(message.chat.id, message.message_id)





@bot.message_handler(commands=['start'])
def start_msg(message):
    chat_id = message.chat.id
    
    if message.chat.type == "private":
        start_message(message)
        stages(chat_id, 'None')


@bot.message_handler(content_types=['text'])
def gtext(message):
    chat_id = message.chat.id
    
    if message.chat.type == "private":
        if stages(chat_id).split('_')[0] == "add":
            toadd = stages(chat_id).split('_')[1]
            if toadd == "group":
                ang(message)
                stages(chat_id, 'None')
            elif toadd == "place":
                gid = stages(chat_id).split('_')[2]
                new_pl = message.text
                gsetplace(gid, new_pl)
                k = kmarkup()
                k.row(btn(k_add_new, callback_data="add_cat_" + str(gid)))
                for i in catlist():
                    k.row(btn(str(i['category']), callback_data=f'add_cat_{str(gid)}_{str(i["id"])}'))
                k.row(back('our_group'))
                msg = add_new_group_2
                send(chat_id, msg, reply_markup=k)
                #start_message(message)
                stages(chat_id, 'None')
            elif toadd == "cat":
                gid = stages(chat_id).split('_')[2]
                new_cat = message.text
                gsetcat(gid, new_cat)
                lang(gid, 'en')
                del_msgs_set_default(gid)
                start_message(message)
                stages(chat_id, 'None')
    
    else:
        if chat_id in glist():
            if 




@bot.callback_query_handler(func=lambda m:True)
def globalCall(call):
    chat_id = call.message.chat.id
    def dm():
        try:
            bot.delete_message(chat_id, call.message.message_id)
        except:
            pass
    
    if call.data == "home":
        start_message(call.message)
        dm()
    elif call.data == "our_group":
        k = kmarkup()
        msg = msg_our_group
        k.row(btn("Добавить Группу", callback_data="add_group"))
        for i in plist():
            b = types.InlineKeyboardButton(i['place'], callback_data="select_place_"+str(i['id']))
            k.row(b)
        k.row(back('home'))
        send(chat_id, msg, reply_markup=k)
        dm()
    elif call.data == "close":
        dm()
    
    elif "set" in call.data:
        toset = call.data.split('_')[1]
        if toset == "ru" or toset== "en":
            gid = call.data.split('_')[2]
            lang(gid, toset)
            manage(chat_id, gid)
        elif toset == "g":
            gid = int(call.data.split('_')[2])
            com = call.data.split('_')[3]
            if com == 'del':
                stater = call.data.split('_')[4]
                stat = call.data.split('_')[5]
                
                sql.execute(f"UPDATE msg_dels SET g{stater} = '{stat}' WHERE gid = '{str(gid)}'")
                db.commit()
                service_dels(chat_id, gid)

        dm()
    elif "add" in call.data:
        toadd = call.data.split('_')[1]
        
        if toadd == 'group':
            k = kmarkup()
            msg = add_new_group
            k.row(back('home'))
            send(chat_id, msg, reply_markup=k)
            stages(chat_id, 'add_group')
        elif toadd == 'place':
            if len(call.data.split('_')) == 3:
                gid = call.data.split('_')[2]
                k = kmarkup()
                msg = add_new_group_1
                k.row(back('home'))
                send(chat_id, msg, reply_markup=k)
                stages(chat_id, 'add_place_'+ str(gid))
            else:
                gid = call.data.split('_')[2]
                place_id = call.data.split('_')[3]
                plc = ginfo_with_id(place_id)['place']
                sql.execute(f"UPDATE our_group SET place = '{str(plc)}' WHERE chat_id = '{str(gid)}'")
                db.commit()
                k = kmarkup()
                k.row(btn(k_add_new, callback_data="add_cat_" + str(gid)))
                for i in catlist():
                    k.row(btn(str(i['category']), callback_data=f'add_cat_{str(gid)}_{str(i["id"])}'))
                k.row(back('our_group'))
                msg = add_new_group_2
                send(chat_id, msg, reply_markup=k)
        elif toadd == 'cat':
            if len(call.data.split('_')) == 3:
                # Добавить категорию
                gid = call.data.split('_')[2]
                k = kmarkup()
                msg = add_new_cat
                k.row(back('our_group'))
                send(chat_id, msg, reply_markup=k)
                stages(chat_id, f'add_cat_{str(gid)}')
                
            else:
                # Выбрать категорию
                gid = call.data.split('_')[2]
                new_cat_id = call.data.split('_')[3]
                ctg = ginfo_with_id(new_cat_id)['category']
                gsetcat(gid, ctg)
                del_msgs_set_default(gid)
                start_message(message)
            
        
                
                
        dm()
    elif "select" in call.data:
        selector = call.data.split('_')[1]
        if selector == "place":
            place_id = call.data.split('_')[2]
            if len(call.data.split('_')) == 3:
                place = ginfo_with_id(place_id)['place']
                k = kmarkup()
                sql.execute(f"SELECT * FROM our_group WHERE place = '{str(place)}'")
                if sql.fetchone() is None:
                    pass
                else:
                    cats =[]
                    sql.execute(f"SELECT * FROM our_group WHERE place = '{str(place)}'")
                    for i in sql.fetchall():
                        if i[2] not in cats:
                            k.row(btn(i[2], 
                            callback_data=f"select_place_{str(place_id)}_{str(i[0])}"))
                msg = select_cat.format(**{"place": place})
                k.row(back(f"our_group"))
                send(chat_id, msg, reply_markup=k)
            else:
                place = ginfo_with_id(place_id)['place']
                category_id = call.data.split('_')[3]
                cat = ginfo_with_id(category_id)['category']
                k = kmarkup()
                msg = select_group.format(**{
                    "place": place,
                    "cat": cat
                })
                command = f"""SELECT * FROM our_group
                WHERE place = '{str(place)}' 
                AND category = '{str(cat)}'
                """
                sql.execute(command)
                for i in sql.fetchall():
                    k.row(btn(bot.get_chat(int(i[1])).title, callback_data=f"manage_{str(i[1])}"))
                k.row(back(f"select_place_{str(place_id)}"))
                send(chat_id, msg, reply_markup=k)
        
        dm()
    elif "manage" in call.data:
        gid = int(call.data.split('_')[1])
        if len(call.data.split('_')) == 2:
            manage(chat_id, gid)
            dm()
    
        elif len(call.data.split('_')) == 3:
            command = call.data.split('_')[2]
            # Удаление сообщений
            if command == "dels":
                dels_stg(chat_id, gid)
                dm()
            elif command  == "lang":
                lang_stage(call.message, gid)
                dm()
            elif command == "bw":
                bw_stg(gid, chat_id)
                dm()
                
        elif len(call.data.split('_')) == 4:
            command = call.data.split('_')[2]
            command1 = call.data.split('_')[3]
            if command == "dels":
                if command1 == "service":
                    service_dels(chat_id, gid)
                elif command1 == "command":
                    del_comms(gid, chat_id)
            if command == "bw":
                if command1 == "switch":
                    setfucks(gid, chat_id)
                elif command1 == "change_fuck":
                    stat =  group_switch(gid, "banned_words")["fuck"]
                    if stat == 'None':
                        stat = "kick"
                    elif stat == "kick":
                        stat = "mute"
                    elif stat == "mute":
                        stat = "ban"
                    elif stat == "ban":
                        stat = "None"
                    group_switch(gid, "banned_words", new_fuck=stat)
                    bw_stg(gid, chat_id)
                    
            dm()
        elif len(call.data.split('_')) == 5:
            command = call.data.split('_')[2]
            command1 = call.data.split('_')[3]
            news = call.data.split('_')[4]
            
            if command == "dels":
                if command1 == "commands":
                    group_switch(gid, "delete_comms", new_state=news)
                    del_comms(gid, chat_id)
                    
            dm()
                    
bot.polling()