import psycopg2

db = psycopg2.connect(
    port=5432,
    host='localhost',
    database="group_fucker",
    user="postgres",
    password="armageddon"
)
sql = db.cursor()

def preDB():
    sql.execute(f"""CREATE TABLE IF NOT EXISTS stages(
    user_id TEXT PRIMARY KEY,
    stage TEXT
    )""")
    db.commit()
    sql.execute(f"""CREATE TABLE IF NOT EXISTS staff(
    user_id TEXT PRIMARY KEY,
    status TEXT
    )""")
    db.commit()
    sql.execute(f"""CREATE TABLE IF NOT EXISTS lang(
    user_id TEXT PRIMARY KEY,
    lang TEXT
    )""")
    db.commit()
    sql.execute(f"""CREATE TABLE IF NOT EXISTS texts(
    id TEXT PRIMARY KEY,
    ru TEXT,
    en TEXT
    )""")
    db.commit()
    sql.execute(f"""CREATE TABLE IF NOT EXISTS buttons(
    id TEXT PRIMARY KEY,
    ru TEXT,
    en TEXT
    )""")
    db.commit()
    sql.execute(f"""CREATE TABLE IF NOT EXISTS our_group(
    id TEXT PRIMARY KEY,
    chat_id TEXT,
    category TEXT,
    place TEXT
    )""")
    db.commit()
    sql.execute(f"""CREATE TABLE IF NOT EXISTS msg_dels(
    gid TEXT PRIMARY KEY,
    gjoin TEXT,
    gexit TEXT,
    gphoto TEXT,
    gtitle TEXT,
    gpinned TEXT
    )""")
    db.commit()
    sql.execute(f"""CREATE TABLE IF NOT EXISTS delete_commands(
    gid TEXT PRIMARY KEY,
    status TEXT,
    fuck TEXT
    )""")
    db.commit()
    sql.execute(f"""CREATE TABLE IF NOT EXISTS fuck(
    gid TEXT PRIMARY KEY,
    f TEXT,
    fuck TEXT,
    until TEXT
    )""")
    db.commit()
    sql.execute(f"""CREATE TABLE IF NOT EXISTS gswitches(
    gid TEXT PRIMARY KEY,
    switch_name TEXT,
    switch TEXT,
    fuck TEXT,
    alert TEXT
    )""")
    db.commit()
    
    
    
    



preDB()