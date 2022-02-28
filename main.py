from settings import *

@bot.message_handler(commands=['start'])
def startMsg(message):
    chat_id = message.chat.id
    k = markup()
    msg = 'Добро Пожаловать в бот автопостинга в частных группах'
    k.row(btn('Каналы / Группы', callback_data='channels'))
    k.row(btn('Сообщения', callback_data='ads'))
    k.row(btn('Кошелек', callback_data='wallet'))
    send(chat_id, msg, reply_markup=k)
    

@bot.callback_query_handler(func: lambda m:True)
def gcall(call):
    if call.data == 'channels':
        
    
    





bot.polling()
