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
    pass

preDB()