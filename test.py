import time, MySQLdb

conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="testdb", charset="utf8")
cursor = conn.cursor()

sql= " create table users( name varchar(50), created int);"
cursor.execute(sql)

sql = "insert into users(name, created) values(%s, %s)"
print sql
param = ("aaa", int(time.time()))
n = cursor.execute(sql, param)
print n

n = cursor.execute("select * from users")   
for row in cursor.fetchall():   
    for r in row:   
        print r   

conn.commit()

cursor.close()
conn.close()
