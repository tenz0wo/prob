import eel, os, random
import sqlite3
from sqlite3 import Error


try:
    connection = sqlite3.connect('db.sqlite')
    print("Connection to SQLite DB successful")
    # connection.row_factory = sqlite3.Row

except Error as e:
    print(f"The error '{e}' occurred")

cursor = connection.cursor()


connection.commit()

eel.init('web')

@eel.expose
def auth(login, password):
    cursor.execute("SELECT Login, Password FROM Employees")
    rows = cursor.fetchall()
    for result in rows:
        if result['Login'] == login and result["Password"] == password:
            print(login, password)
        else:
            print("Invalid user!")

@eel.expose
def authenticate(login, password):
    cursor.execute("SELECT Login, Password FROM Employees WHERE Login = ? AND Password = ?", (login, password))
    result = cursor.fetchone()
    if result:
        eel.receiver("true")
    else:
        eel.receiver("false")

@eel.expose
def show_ticket():
    cursor.execute("""SELECT g.FirstName, g.LastName, g.RoomNumber, g.NumberOfGuests, g.PhoneNumber, b.CheckInDate, b.CheckOutDate
                    FROM Guests g INNER JOIN Bookings b ON
                    g.GuestID = b.GuestID;
                    """)
    result = cursor.fetchall()
    return result

if __name__ == "__main__":
    eel.start('index.html', size=(600, 600))