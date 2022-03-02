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
            if i[5] == 'None' and i[4] != 'None':
                result = {'minutes': i[4], 'last_post': None}
            elif i[4] == 'None' and i[5] != 'None':
                result = {'minutes': None, 'last_post': str_to_time(i[5])}
            elif i[4] != 'None' and i[5] != 'None':
                result = {'minutes': i[4], 'last_post': str_to_time(i[5])}
            else:
                result = {'minutes': None, 'last_post': None}

    return result


def the_loop():
    pass