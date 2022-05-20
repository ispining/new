import datetime

from packs.settings import *
from packs.stg import *


@bot.message_handler(commands=['start'])
def startMessage(message):
    chat_id = message.chat.id
    if message.text == None:
        startMessageAfterLang(chat_id)
    else:
        if len(message.text.split()) == 1:
            if lang(chat_id) == None:
                setLangStage(chat_id)
            else:
                startMessageAfterLang(chat_id)


@bot.message_handler(commands=['block', 'ban'])
def Blocker(message):
    chat_id = message.chat.id

    if message.chat.type == 'private':
        if len(message.text.split()) == 2:
            del_user = None
            # with id
            try:
                del_user = int(message.text.split()[1])


            except:
                #with username
                try:
                    sql.execute(f"SELECT * FROM posts")
                    for i in sql.fetchall():
                        if '@' + str(bot.get_chat(int(i[0])).username) == message.text.split()[1]:
                            del_user = int(i[0])
                except:
                    #not found 404
                    pass



            if del_user != None:
                blocker(del_user, 'block')
                send(chat_id, 'user blocked')






@bot.message_handler(content_types=['text'])
def gtext(message):
    chat_id = message.chat.id
    caption = message.text
    if "add_content" in stages(chat_id):
        send(chat_id, txt(chat_id, 'only_with_media'))



@bot.message_handler(content_types=['photo'])
def gphoto(message):
    chat_id = message.chat.id
    caption = message.caption
    photo_id = message.photo[-1].file_id

    if "add_content" in stages(chat_id):
        lng = stages(chat_id).split('_')[2]
        sql.execute(f"SELECT * FROM posts WHERE user_id = '{str(chat_id)}'")
        if sql.fetchone() is None:
            if lng == 'ru':
                sq(f"INSERT INTO posts VALUES('{str(chat_id)}', 'photo', 'None', 'None', '{photo_id}', 'None', 'None', '{str(caption)}', 'None', 'None', 'None')")
            elif lng == 'en':
                sq(f"INSERT INTO posts VALUES('{str(chat_id)}', 'None', 'None', 'photo', 'None', 'None', '{photo_id}', 'None', 'None', '{str(caption)}', 'None')")
            elif lng == 'he':
                sq(f"INSERT INTO posts VALUES('{str(chat_id)}', 'None', 'photo', 'None', 'None', '{photo_id}', 'None', 'None', '{str(caption)}', 'None', 'None')")



            msg = txt(chat_id, 'post_added')
            send(chat_id, msg)


        else:
            if lng == 'ru':
                sq(f"UPDATE posts SET ru_caption = '{caption}' WHERE user_id = '{str(chat_id)}'")
                sq(f"UPDATE posts SET ru_media_id = '{photo_id}' WHERE user_id = '{str(chat_id)}'")
                sq(f"UPDATE posts SET ru_media_type = 'photo' WHERE user_id = '{str(chat_id)}'")
            elif lng == 'he':
                sq(f"UPDATE posts SET he_caption = '{caption}' WHERE user_id = '{str(chat_id)}'")
                sq(f"UPDATE posts SET he_media_id = '{photo_id}' WHERE user_id = '{str(chat_id)}'")
                sq(f"UPDATE posts SET he_media_type = 'photo' WHERE user_id = '{str(chat_id)}'")
            elif lng == 'en':
                sq(f"UPDATE posts SET en_caption = '{caption}' WHERE user_id = '{str(chat_id)}'")
                sq(f"UPDATE posts SET en_media_id = '{photo_id}' WHERE user_id = '{str(chat_id)}'")
                sq(f"UPDATE posts SET en_media_type = 'photo' WHERE user_id = '{str(chat_id)}'")




            msg = txt(chat_id, 'post_edited')
            send(chat_id, msg)

        startMessageAfterLang(chat_id)


@bot.message_handler(content_types=['video'])
def gvideo(message):
    chat_id = message.chat.id
    caption = message.caption
    data = message.video.file_id

    if "add_content" in stages(chat_id):
        lng = stages(chat_id).split('_')[2]
        sql.execute(f"SELECT * FROM posts WHERE user_id = '{str(chat_id)}'")
        if sql.fetchone() is None:
            if lng == 'ru':
                sq(f"INSERT INTO posts VALUES('{str(chat_id)}', 'video', 'None', 'None', '{data}', 'None', 'None', '{str(caption)}', 'None', 'None', 'None')")
            elif lng == 'en':
                sq(f"INSERT INTO posts VALUES('{str(chat_id)}', 'None', 'None', 'video', 'None', 'None', '{data}', 'None', 'None', '{str(caption)}', 'None')")
            elif lng == 'he':
                sq(f"INSERT INTO posts VALUES('{str(chat_id)}', 'None', 'video', 'None', 'None', '{data}', 'None', 'None', '{str(caption)}', 'None', 'None')")

            msg = txt(chat_id, 'post_added')
            send(chat_id, msg)


        else:
            if lng == 'ru':
                sq(f"UPDATE posts SET ru_caption = '{caption}' WHERE user_id = '{str(chat_id)}'")
                sq(f"UPDATE posts SET ru_media_id = '{data}' WHERE user_id = '{str(chat_id)}'")
                sq(f"UPDATE posts SET ru_media_type = 'video' WHERE user_id = '{str(chat_id)}'")
            elif lng == 'he':
                sq(f"UPDATE posts SET he_caption = '{caption}' WHERE user_id = '{str(chat_id)}'")
                sq(f"UPDATE posts SET he_media_id = '{data}' WHERE user_id = '{str(chat_id)}'")
                sq(f"UPDATE posts SET he_media_type = 'video' WHERE user_id = '{str(chat_id)}'")
            elif lng == 'en':
                sq(f"UPDATE posts SET en_caption = '{caption}' WHERE user_id = '{str(chat_id)}'")
                sq(f"UPDATE posts SET en_media_id = '{data}' WHERE user_id = '{str(chat_id)}'")
                sq(f"UPDATE posts SET en_media_type = 'video' WHERE user_id = '{str(chat_id)}'")

            msg = txt(chat_id, 'post_edited')
            send(chat_id, msg)

        startMessageAfterLang(chat_id)



@bot.callback_query_handler(func=lambda m: True)
def globalcalls(call):
    chat_id = call.message.chat.id

    def dm():
        try:
            bot.delete_message(chat_id, call.message.message_id)
        except:
            pass

    if call.message.chat.type == 'private':
        if blocker(chat_id):
            if call.data in ["ru", 'en', 'he']:
                lang(chat_id, call.data)
                startMessageAfterLang(chat_id)
                dm()
            elif call.data == "home":
                startMessageAfterLang(chat_id)
                dm()
            elif "add_content" in call.data:
                lng = call.data.split('_')[2]
                add_content_stg(call, lng)
                dm()
            elif call.data == "change_lang":
                setLangStage(chat_id)
                dm()
            elif call.data == 'post_now':
                pn = post_now(chat_id, call=call)
                if pn:
                    k = kmarkup()
                    k.row(back(chat_id, 'home'))
                    msg = txt(chat_id, 'ad_posted').format({'time': str(datetime.datetime.now()).split('.')[0]})
                    send(chat_id, msg, reply_markup=k)
                    dm()
            elif 'view_content' in call.data:
                lng = call.data.split('_')[2]
                infos = user_ad_with_lang(chat_id, lng)

                if infos['media_type'] != 'None':
                    media_type = infos['media_type']
                    media_id = infos['media_id']
                    caption = infos['caption']
                    k = kmarkup()
                    k.row(add_button(chat_id, 'remove_content_'+lng))
                    k.row(back(chat_id, 'home'))
                    if media_type == 'photo':
                        bot.send_photo(chat_id=chat_id, photo=media_id, caption=caption, reply_markup=k)
                    elif media_type == 'video':
                        bot.send_video(chat_id=chat_id, video=media_id, caption=caption, reply_markup=k)
                else:
                    bot.answer_callback_query(call.id, txt(chat_id, 'no_selected_ad'), show_alert=True)
            elif 'remove_content' in call.data:
                lng = call.data.split('_')[2]
                if lng == 'ru':
                    sq(f"UPDATE posts SET ru_media_type = 'None' WHERE user_id = '{str(chat_id)}'")
                    sq(f"UPDATE posts SET ru_media_id = 'None' WHERE user_id = '{str(chat_id)}'")
                    sq(f"UPDATE posts SET ru_caption = 'None' WHERE user_id = '{str(chat_id)}'")
                elif lng == 'he':
                    sq(f"UPDATE posts SET he_media_type = 'None' WHERE user_id = '{str(chat_id)}'")
                    sq(f"UPDATE posts SET he_media_id = 'None' WHERE user_id = '{str(chat_id)}'")
                    sq(f"UPDATE posts SET he_caption = 'None' WHERE user_id = '{str(chat_id)}'")
                elif lng == 'en':
                    sq(f"UPDATE posts SET en_media_type = 'None' WHERE user_id = '{str(chat_id)}'")
                    sq(f"UPDATE posts SET en_media_id = 'None' WHERE user_id = '{str(chat_id)}'")
                    sq(f"UPDATE posts SET en_caption = 'None' WHERE user_id = '{str(chat_id)}'")
                bot.answer_callback_query(call.id, txt(chat_id, 'selected_removed'), show_alert=True)
                startMessageAfterLang(chat_id)
                dm()
            elif call.data == "our_g":
                k = kmarkup()
                msg = txt(chat_id, "our_g")
                k.row(types.InlineKeyboardButton(buttons(chat_id, "in_russian"), url=bot.export_chat_invite_link(int(db_settings("ru_g")))))
                k.row(types.InlineKeyboardButton(buttons(chat_id, "in_hebrew"), url=bot.export_chat_invite_link(int(db_settings("he_g")))))
                k.row(types.InlineKeyboardButton(buttons(chat_id, "in_english"), url=bot.export_chat_invite_link(int(db_settings("en_g")))))
                k.row(back(chat_id, "home"))
                send(chat_id, msg, reply_markup=k)
                dm()

while True:
    try:
        bot.polling()
    except Exception as ex:
        print(ex)