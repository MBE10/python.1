import sqlite3

connection = sqlite3.connect('example.db')

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS employess(
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     name text not null,
     position TEXT NOT NULL, 
     department TEXT NOT NULL,
     salary REAL
)
''')



connection.commit()

cursor.execute('''
    INSERT INTO employess(name, position, department, salary)
    VALUES (?, ?, ?, ?)          
    '''      , ('John Doe', 'Software Engineer', 'IT', 70000))

connection.commit()

cursor.execute('SELECT * FROM employess')

# rows = cursor.fetchball()
# for now in rows:
#     print(f"employess: {rows[0]}, WorkPlace: {row[1]}")


#     connection.close()