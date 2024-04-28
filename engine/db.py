import sqlite3

conn = sqlite3.connect("assistant.db")

cursor = conn.cursor()
query = ("CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))")
cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'unity hub', 'C:\\Program Files\\Unity Hub\\Unity Hub.exe')"
# cursor.execute(query)
# conn.commit()

# query = "UPDATE web_command SET name = 'facebook' WHERE name = 'face book'"
# cursor.execute(query)
# conn.commit()


# query = "DELETE FROM web_command WHERE id = ?"
# command_name = (4 ,)  # Specify the command name you want to delete

# # Execute the query
# cursor.execute(query, command_name)

# # Commit the transaction
# conn.commit()

# query = ("CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))")
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'canva', 'https://www.canva.com/p')"
# cursor.execute(query)
# conn.commit()

# app_name = "unity app"
# cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
# results = cursor.fetchall()
# print(results[0][0])

