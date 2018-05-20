##Version 1.3##
import sqlite3, os, time, datetime, psutil

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

db = sqlite3.connect('version_1.3.db')
c = db.cursor()

def currentTime():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    return date

def initDb():
    c.execute('CREATE TABLE IF NOT EXISTS systemBoot(datestamp TEXT, msg TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS leagueTime(datestamp TEXT, msg TEXT)')
    db.commit()

def systemBoot():
    c.execute('INSERT INTO systemBoot(datestamp, msg) VALUES(?, ?)',
    (currentTime(), 'System Booted'))
    db.commit()

def leaugeClient():
    c.execute('INSERT INTO leagueTime(datestamp, msg) VALUES (?, ?)',
    (currentTime(), "Client Opened"))
    db.commit()

def leagueNewgame():
    c.execute('INSERT INTO leagueTime(datestamp, msg) VALUES(?, ?)',
    (currentTime(), "New Game!"))
    db.commit()

def leagueStillIngame():
    c.execute('INSERT INTO leagueTime(datestamp, msg) VALUES(?, ?)',
    (currentTime(), "Still Ingame!"))
    db.commit()

def leagueGameEnded():
    c.execute('INSERT INTO leagueTime(datestamp, msg) VALUES (?, ?)',
    (currentTime(), "Game Ended!"))
    db.commit()

def leagueCheck():
    while True:
      if "League of Legends.exe" in (p.name() for p in psutil.process_iter()):
          leagueNewgame()
          while "League of Legends.exe" in (p.name() for p in psutil.process_iter()):
              leagueStillIngame()
              if "League of Legends.exe" in (p.name() for p in psutil.process_iter()) != True:
                  leagueGameEnded()
                  return

    # if "League of Legends.exe" in (p.name() for p in psutil.process_iter()):
    #     ingame = 1
    #     leagueNewgame()
    #     while ingame:
    #         leagueStillIngame()
    #         if "League of Legends.exe" in (p.name() for p in psutil.process_iter() != True):
    #             leagueGameEnded()
    #             return


initDb()
systemBoot()
while True:
    leagueCheck()
# leaugeClient()
# leagueClientDetector()

print('Logged')