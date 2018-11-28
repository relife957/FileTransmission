import psycopg2

conn = None
output = "123"
try:
    conn = psycopg2.connect(host='127.0.0.1', port='5432',
                            dbname='postgres' ,user='postgres' ,password='123456')
except psycopg2.OperationalError:
    output = '数据库连接失败！'
print(output)
cur = conn.cursor()
cur.execute("select * from api.todos")
rows = cur.fetchall()
for row in rows :
    print(str(row))
conn.close()