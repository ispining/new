
from .DB_connector import *



def lang(user_id, new=None):
    result = None
    sql.execute(f"SELECT * FROM lang WHERE user_id = '{str(user_id)}'")
    if sql.fetchone() is None:
        if new != None:
            sql.execute(f"INSERT INTO lang VALUES ('{str(user_id)}', '{str(new)}')")
            db.commit()
            return new
    else:
        if new != None:
            sql.execute(f"UPDATE lang SET lang = '{str(new)}' WHERE user_id = '{str(user_id)}'")
            db.commit()
        sql.execute(f"SELECT * FROM lang WHERE user_id = '{str(user_id)}'")
        for i in sql.fetchall():
            result = i[1]

    return result


def txt(user_id, txt_id):
    sql.execute(f"SELECT * FROM texts WHERE id = '{str(txt_id)}'")
    for i in sql.fetchall():
        if lang(user_id) == 'ru':
            return i[1]
        elif lang(user_id) == 'en':
            return i[2]


def buttons(user_id, btn_id):
    sql.execute(f"SELECT * FROM buttons WHERE id = '{str(btn_id)}'")
    for i in sql.fetchall():
        if lang(user_id) == 'ru':
            return i[1]
        elif lang(user_id) == 'en':
            return i[2]
            

############ ТЕКСТ ############
lang_stg = """
<b>Select your lang:</b>

<b>Выберите язык:</b>

"""

welcome_msg = """
Добро пожаловать, Босс
"""
msg_our_group = """
<b>Выберите страну</b>

"""
add_new_group = """
<b>Добавление группы</b>

Отправь Идентификатор группы, которую требуется добавить
"""
add_new_group_1 = """
<b>Добавление группы</b>

В какой стране группа находится? 
Выбери Страну из существующих,  или добавь новую.

"""
add_new_group_2 = """
<b>Добавление группы</b>

Выбери кaтугорию из существующих, или добавь новую.
"""
add_new_cat = """
<b>Добавление категории</b>

Введите название новой категории
"""
select_cat = """
<b>Выберите категорию</b>

<u>Выбранная страна:</u> {place}
"""
select_group= """
<b>Выберите группу</b>

<u>Выбранная страна:</u> {place}
<u>Выбранная категория:</u> {cat}
"""

mng_text = """
<b>Менеджмент группы</b>

Выбранная группа: {title}
"""
service_msgs = """
<b>Сервисные сообщения</b>

Join: {join}
Exit: {exit}
New Photo: {photo}
New Title: {title}
Pinned messages: {pinned}
"""

dels_stg_msg = """
<b>Удаление сообщений</b>
"""

del_commands="""
<b>Удаление комманд</b>

Группа: {gtitle}
Статус: {status}
"""
bw_msg = """
<b>Запрещенные слова</b>

<b>Группа:</b> {gtitle}
<b>Наказание:</b> {gfuck}
<b>Статус:</b> {gstat}
<b>Удаление:</b> {gdelmsg}

"""
############ КНОПКИ ############
k_our_group = "Группы"
k_set_lang = "Язык группы"
k_add_new = "Добавить"
k_close = "Закрыть"
k_del_msgs = "Удаление сообщений"
k_service_msgs= "Системные сообщения"
k_chat_lang = "Язык"
k_commands = "Команды"
k_bw = "Запрещенные слова"
k_fuck = "Наказание"
k_delete = "Удалять сообщение"
k_activate = "Вкл. / Выкл."

