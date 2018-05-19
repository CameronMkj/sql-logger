import sqlite3, os, time, datetime

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

db = sqlite3.connect('programlog.db')
c = db.cursor()

def initialiseTables():
    c.execute('CREATE TABLE IF NOT EXISTS leagueClient (Id INT PRIMARY KEY,datestamp TEXT, keyword TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS computerBoot (Id INT PRIMARY KEY,datestamp TEXT, keyword TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS leagueGame (Id INT PRIMARY KEY,datestamp TEXT, keyword TEXT)')
    
    db.commit()
'''
def initialiseRecords():
    c.execute('')
'''
def currentTime():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    return date

def computerBoot():
    date = currentTime()
    keyword = "Computer Booted"
    c.execute('INSERT INTO computerBoot(datestamp, keyword) VALUES(?, ?)',
    (date, keyword))
    
def leagueClient():
    date = currentTime()
    keyword = "Client Logged"
    c.execute('INSERT INTO leagueClient(datestamp, keyword) VALUES(?, ?)',
    (date, keyword))

def leagueGame():
    date = currentTime()
    keyword = "League Game Logged"
    c.execute('INSERT INTO leagueGame(datestamp, keyword) VALUES(?, ?)'),
    (date, keyword)

initialiseTables()






