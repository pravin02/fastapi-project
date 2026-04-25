import sqlite3
SQLITE_DB_PATH = "C:/Users/Hp/AppData/Roaming/DBeaverData/workspace6/.metadata/sample-database-sqlite-1/Chinook.db"
connection =sqlite3.connect(SQLITE_DB_PATH)

cursor = connection.cursor();
cursor.execute("SELECT * FROM Album")

for row in cursor.fetchall():
    print(row[1])

connection.close()

