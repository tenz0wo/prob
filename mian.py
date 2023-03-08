import eel, os, random
import sqlite3
from sqlite3 import Error


try:
    connection = sqlite3.connect('db.sqlite')
    print("Connection to SQLite DB successful")
    connection.row_factory = sqlite3.Row

except Error as e:
    print(f"The error '{e}' occurred")

sql = connection.cursor()


connection.commit()

eel.init('web')

@eel.expose
def auth(login, password):
    sql.execute("SELECT Login, Password FROM Employees")
    rows = sql.fetchall()
    for result in rows:
        if result['Login'] == login and result["Password"] == password:
            print(login, password)
        else:
            print("Invalid user!")


eel.start('reg.html', size=(600, 600))