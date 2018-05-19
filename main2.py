import sqlite3, time, datetime, os, psutil

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")


conn = sqlite3.connect('database.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS main(Id INT PRIMARY KEY,datestamp TEXT, keyword TEXT)')

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keywordOne = "Computer Boot"
    Id = 1
    c.execute("INSERT INTO main(Id, datestamp, keyword) VALUES (?, ?, ?)", (Id, date, keywordOne))
    conn.commit()

def league_opened():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%d-%m-%Y %H:%M:%S'))
    keywordOne = "League Opened"
    Id = 2
    c.execute("INSERT INTO main(Id, datestamp, keyword) VALUES(?, ?, ?)", (Id, date, keywordOne))
    conn.commit()

create_table()
dynamic_data_entry()
print ("Computer Uptime Logged!")


while True:
    if "LeagueClient.exe" in (p.name() for p in psutil.process_iter()):
        league_opened()
        print("League Detected, Logged!")
        time.sleep(1)
    else:
        pass

while True:
    c.execute("UPDATE main(datestamp, keyword) WHERE ")
