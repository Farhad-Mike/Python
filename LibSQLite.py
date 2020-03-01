import sqlite3


db = sqlite3.connect(':memory:') # Create a database in RAM
db = sqlite3.connect('C:/Users/FRDevelop/Desktop/data.db')
db.row_factory = sqlite3.Row # Позволяет потом преобразовать объект так как нам удобно. Не обязательно указывать но рекомендуется.
db.execute('drop table if exists test')
db.execute('create table test (t1 text, i1 int)')
db.execute('insert into test (t1, i1) values (?, ?)', ('one', 1))
db.execute('insert into test (t1, i1) values (?, ?)', ('two', 2))
db.execute('insert into test (t1, i1) values (?, ?)', ('three', 3))
db.commit()
cursor = db.execute('select * from test order by t1')
cursor = db.execute('select i1, t1 from test order by i1') # by i1 mean sort by i1
for row in cursor:
    print(row) # Without sqlite3.Row
for row in cursor:
    print(dict(row)) # With sqlite3.Row. Also can be used tuple(row), set(row), list(row)

db.close() # Close after working with database

cursor.fetchone() #retrieve the first row 