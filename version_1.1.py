##Version 1.1##
import sqlite3, os, time, datetime

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

db = sqlite3.connect('version_1.1.db')
c = db.cursor()

class initialise:
    def totalTime(self):
        c.execute('CREATE TABLE IF NOT EXISTS totalTime(Id TEXT PRIMARY KEY, datestamp TEXT)')
        db.commit()

    def instanceCount(self):
        c.execute('CREATE TABLE IF NOT EXISTS instanceCount (Id TEXT PRIMARY KEY, Date/Time TEXT,ComputerBoot TEXT, LeagueClient TEXT, LeagueGame TEXT)')
        db.commit()  
        
    def currentTime(self):
        unix = time.time()
        date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
        return date
        
class computerBoot:
    def cB_time(self):
        return initialise.currentTime(self)
    #runs after if statement
    def cB_instance(self):
        c.execute('INSERT INTO instanceCount (Date/Time TEXT, ComputerBoot TEXT) VALUES (?, ?)',
        (initialise.currentTime(self)),"Booted")
        db.commit()
        
class leagueClient:
    def lC_time(self):
        return initialise.currentTime(self)
        
    def lC_instance(self):
        c.execute('INSERT INTO instanceCount(Date/Time TEXT, LeagueClient TEXT) VALUES (?, ?)',
        (initialise.currentTime(self)), "Booted")
        db.commit()

class leagueGame:
    def lG_time(self):
        return initialise.currentTime(self)

    def lG_instance(self):
        c.execute('INSERT INTO instanceCount (Date/Time TEXT, LeagueGame TEXT) VALUES (?, ?)',
        (initialise.currentTime(self)),"Booted")
        db.commit()

class Updation:
    pass


#####################################

'''
    while True:
    if "LeagueClient.exe" in (p.name() for p in psutil.process_iter()):
        league_opened()
        print("League Detected, Logged!")
        time.sleep(1)
    else:
        pass
'''