import psycopg2

db = psycopg2.connect(host='ec2-52-31-219-113.eu-west-1.compute.amazonaws.com',
    database='deb5j9pn5m7jmr',
    user='fdjvjwgulugmqg',
    password= '81ecbf3faa06cd7f95ad88ccf341cbbe5ca8d20df17d7ef337cb87f646ad3d09')
sql = db.cursor()



def preDB():
    sql.execute(f'''CREATE TABLE IF NOT EXISTS staff(
    user_id TEXT PRIMARY KEY,
    status TEXT
    )''')
    db.commit()
    sql.execute(f'''CREATE TABLE IF NOT EXISTS stages(
    user_id TEXT PRIMARY KEY,
    stage TEXT
    )''')
    db.commit()
    sql.execute(f'''CREATE TABLE IF NOT EXISTS ads(
    id TEXT PRIMARY KEY,
    user_id TEXT,
    media_type TEXT,
    media_id TEXT,
    caption TEXT,
    minutes TEXT,
    last_post TEXT
    )''')
    db.commit()
    sql.execute(f'''CREATE TABLE IF NOT EXISTS channels(
    msg_id TEXT PRIMARY KEY,
    channel_id TEXT
    )''')
    db.commit()
    sql.execute(f'''CREATE TABLE IF NOT EXISTS btn(
    msg_id TEXT PRIMARY KEY,
    btn_id TEXT,
    btn_name TEXT,
    btn_type TEXT,
    btn_link TEXT
    )''')
    db.commit()
    sql.execute(f'''CREATE TABLE IF NOT EXISTS timers(
    msg_id TEXT PRIMARY KEY,
    minutes TEXT
    )''')
    db.commit()
    sql.execute(f'''CREATE TABLE IF NOT EXISTS ch(
    random_id TEXT PRIMARY KEY,
    ch_id TEXT
    )''')
    db.commit()
    
    
preDB()