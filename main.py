import btns
from settings import *
from stg import *

@bot.message_handler(commands=['start'])
def startMsg(message):
    chat_id = message.chat.id
    if message.chat.type == 'private':
        k = markup()
        msg = texts.start
        k.row(btn(btns.channels, callback_data='channels'))
        k.row(btn(btns.messages, callback_data='ads'))
        k.row(btn(btns.wallet, callback_data='wallet'))
        send(chat_id, msg, reply_markup=k)
        try:
            stages(chat_id, 'None')
        except psycopg2.ProgrammingError:
            pass



@bot.message_handler(commands=['id'])
def idMsg(message):
    chat_id = message.chat.id
    if message.chat.type == 'private':
        msg = '<b>Ай-Ди пользователя:</b> <code>{user_id}</code>'.format(**{
            'user_id': str(chat_id)
        })
        send(chat_id, msg)
    elif message.chat.type != 'private':
        msg = '<b>Ай-Ди пользователя:</b> <code>{user_id}</code>\n<b>Ай-Ди группы:</b> <code>{ch_id}</code>'.format(**{
            'user_id': str(message.from_user.id),
            'ch_id': str(chat_id)
        })
        send(chat_id, msg)



@bot.message_handler(content_types=['text'])
def glob_text(message):
    chat_id = message.chat.id
    if message.chat.type == 'private':
        if stages(chat_id) == 'add_channel':
            ch_id = None
            try:
                ch_id = bot.get_chat(int(message.text)).id
            except:
                pass

            if ch_id != None:
                k = markup()
                msg = texts.add_channel_ok
                send(chat_id, msg)



                add_channel(chat_id)
                stages(message.from_user.id, 'None')



@bot.callback_query_handler(func= lambda m:True)
def gcall(call):
    chat_id = call.message.chat.id

    def dm():
        bot.delete_message(chat_id, call.message.message_id)

    if call.data == 'home':
        startMsg(call.message)
        #dm()
    elif call.data == 'channels':
        k = markup()
        msg = texts.channels
        k.row(btn(btns.add, 'add_channel'))
        k.row(back('home'))
        send(chat_id, msg, reply_markup=k)
        dm()
    elif call.data  == 'add_channel':
        add_channel(chat_id)
        dm()

    



bot.polling()
