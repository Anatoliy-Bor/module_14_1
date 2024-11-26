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

for i in range(10):
	cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?) ", (f"newuser{i+1}", f"example{i+1}ex@mail.ru", f"{(i+1)*10}", "1000"))

cursor.execute("DELETE FROM Users WHERE id % 3 = 1")

for i in range(1, 11,  2):
		 cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, f"newuser{i}"))

cursor.execute("SELECT * FROM Users WHERE age != ?", (60,))
users = cursor.fetchall()

for data in users:
    print(f" Имя: {data[1]} | Почта: {data[2]} | Возраст: {data[3]} | Баланс: {data[4]}")
		
connection.commit()
connection.close()
