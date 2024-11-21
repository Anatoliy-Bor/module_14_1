import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

#for i in range(10):
#	c = i+1
#	eg = (i+1)*10
#	blnc = 1000
#	cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?) ", (f"newuser{c}", f"example{c}ex@mail.ru", f"{eg}",f"{blnc}"))

c = 0
cursor.execute("SELECT * FROM Users")
users = cursor.fetchall()
#for user in users:
#	c += 1
#	if c % 2 != 0:
#		 cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, f"newuser{c}"))


#cursor.execute("DELETE FROM Users WHERE id % 3 = 1")


cursor.execute("SELECT * FROM Users WHERE age != ?", (60,))
users = cursor.fetchall()
for data in users:
    print(f" Имя: {data[1]} | Почта: {data[2]} | Возраст: {data[3]} | Баланс: {data[4]}")
		

connection.commit()
connection.close()
