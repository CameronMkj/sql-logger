##Version 1.4##

import sqlite3, os, time, datetime

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

db = sqlite3.connect('v1.4.db')
c = db.cursor()

def initialisation():
    def totalTime():
        c.execute('CREATE TABLE IF NOT EXISTS totalTime(Id TEXT PRIMARY KEY, datestamp TEXT)')
        db.commit()

    def instanceCount():
        c.execute('CREATE TABLE IF NOT EXISTS instanceCount (Id TEXT PRIMARY KEY, Date/Time TEXT,ComputerBoot TEXT, LeagueClient TEXT, LeagueGame TEXT)')
        db.commit()  
        

def currentTime():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    return date


def cB_time():
    return currentTime()


#runs after if statement
def cB_instance():
    c.execute('INSERT INTO instanceCount (Date/Time TEXT, ComputerBoot TEXT) VALUES (?, ?)',
    (currentTime()),"Booted")
    db.commit()


def lC_time():
    return currentTime()
    

def lC_instance():
    c.execute('INSERT INTO instanceCount(Date/Time TEXT, LeagueClient TEXT) VALUES (?, ?)',
    (currentTime()), "Booted")
    db.commit()


def lG_time():
    return currentTime()


def lG_instance():
    c.execute('INSERT INTO instanceCount (Date/Time TEXT, LeagueGame TEXT) VALUES (?, ?)',
    (currentTime()),"Booted")
    db.commit()

initialisation()