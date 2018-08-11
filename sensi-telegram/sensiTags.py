from settings import dataBaseDjangoDir
from ruuvitag_sensor.ruuvi import RuuviTagSensor
import os
import datetime
import time
import sqlite3

class SensiTags:

    def __init__(self):
        pass

    def getInfo(self):
        conn = sqlite3.connect(dataBaseDjangoDir)
        cursor = conn.cursor()
        cursor.execute("""select * from tags_tag""")
        conn.commit()
        query = (cursor.fetchall())
        msgTags = ", aqui estão as informações sobre as SensiTags.\n\n "
        for tag in query:
            msgTags = msgTags + '*->* MAC: ' + tag[1] + '\n'
            msgTags = msgTags + '     Localização: ' + tag[2] + '\n\n'
        return msgTags

    def getData(self):
        os.system('clear')
        macs = []
        conn = sqlite3.connect(dataBaseDjangoDir)
        cursor = conn.cursor()
        cursor.execute("""select * from tags_tag""")
        conn.commit()
        query = (cursor.fetchall())
        for tag in query:
            macs.append(tag[1])
        timeout_in_sec = 10
        datas = RuuviTagSensor.get_data_for_sensors(macs, timeout_in_sec)
        # Dictionary will have lates data for each sensor
        for mac in macs:
            try:
                tag = datas[mac]
                date = datetime.datetime.now()
                TUPLA = (mac,
                         tag['battery'],
                         tag['temperature'],
                         tag['humidity'],
                         int(date.year),
                         int(date.month),
                         int(date.day),
                         int(date.hour),
                         int(date.minute),
                         int(date.second),
                         )

                vetor = [TUPLA, ]
                print("VETOR : ", vetor)

            except KeyError:
                print ('tag n encontrada: ' + mac)