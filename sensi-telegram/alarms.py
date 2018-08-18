import sqlite3
from settings import dataBaseDjangoDir, dataBaseSensiDir,timeout_in_sec
class Alarms:

    bot = None
    alarms = []

    def __init__(self, bot):
        conn = sqlite3.connect(dataBaseDjangoDir)
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM alarmes_alarme""")
        conn.commit()
        query = (cursor.fetchall())
        self.alarms = query
        self.bot = bot

    def updateAlarms(self):
        conn = sqlite3.connect(dataBaseDjangoDir)
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM alarmes_alarme""")
        conn.commit()
        query = (cursor.fetchall())
        self.alarms = query

    def getInfo(self):
        return self.alarms