import sqlite3, os, time, datetime

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

db = sqlite3.connect('programlog.db')
c = db.cursor()

def initialiseTables():
    c.execute('CREATE TABLE IF NOT EXISTS instanceLogger (Id TEXT PRIMARY KEY,datestamp TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS timeLogger (Id INT PRIMARY KEY,Minutes INT, Seconds INT)')
    
    #timeLogger
    ComputerBoot = "ComputerBoot"
    LeagueClient = "LeagueClient"
    LeagueGame = "LeagueGame"
    
    c.execute('INSERT INTO IF NOT EXISTS timeLogger(Id) VALUES(?)',
    ComputerBoot)
    c.execute('INSERT INTO IF NOT EXISTS timeLogger(Id) VALUES(?)',
    LeagueClient)
    c.execute('INSERT INTO IF NOT EXISTS timeLogger(Id) VALUES(?)',
    LeagueGame)
    
    
    db.commit()

def currentTime():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    return date

# table broken
def computerBoot():
    date = currentTime()
    keyword = "Computer Booted"
    c.execute('INSERT INTO computerBoot(datestamp, keyword) VALUES(?, ?)',
    (date, keyword))
    
##table broken
def leagueClient():
    date = currentTime()
    keyword = "Client Logged"
    c.execute('INSERT INTO leagueClient(datestamp, keyword) VALUES(?, ?)',
    (date, keyword))

##table broken
def leagueGame():
    date = currentTime()
    keyword = "League Game Logged"
    c.execute('INSERT INTO leagueGame(datestamp, keyword) VALUES(?, ?)'),
    (date, keyword)
    
initialiseTables()

class classComputerBoot:
    def computerBootInstance(self):
        date = currentTime()
        keyword = "Booted"
        c.execute('INSERT INTO instanceLogger(datestamp, keyword) VALUES(?, ?)',
        (date, keyword))
    
    ##will be in a while loop later
    def computerBootTime(self):
        c.execute('INSERT INTO timeLogger(')
        db.commit()
        time.sleep(60)
        # for (i = 0; i < 60; i++):
