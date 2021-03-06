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
        msgAlarms = ', tudo bem?\nAqui estão os detalhes dos alarmes armados do seu sistema!:\n\n'
        for al in self.alarms:
            msgAlarms = msgAlarms + '*->* Nome: *' + al[1] + '*\n\n'
            msgAlarms = msgAlarms + '     Trigger: *' + str(al[2]) + 'V*\n\n'

        return msgAlarms