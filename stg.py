from settings import *


def add_channel(chat_id):
        k = markup()
        msg = texts.add_channel
        k.row(back('channels'))
        send(chat_id, msg, reply_markup=k)
        stages(chat_id, 'add_channel')