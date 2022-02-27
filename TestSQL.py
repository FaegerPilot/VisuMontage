import sqlite3,csv

Connection = sqlite3.connect("Fahrzeug.db")
Cursor = Connection.cursor()

if False :
    Cursor.execute('CREATE TABLE Fahrzeug(date text, trans text, symbol text, qty text)')

    Cursor.execute("INSERT INTO Fahrzeug VALUES ('Piranaha','M+77624','DONE','2022-11-22 12:00:00')")

Input = input("Action: ")

with open('Fahrzeug.csv','w',newline='') as f:
    write = csv.writer(f)
    for Row in Cursor.execute('SELECT*FROM Fahrzeug'):  
        print(Row)
        write.writerow(Row)

Connection.commit()
Connection.close()