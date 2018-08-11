from settings import dataBaseDjangoDir, dataBaseSensiDir
from ruuvitag_sensor.ruuvi import RuuviTagSensor
import os
import datetime
import time
import sqlite3

class SensiTags:

    def __init__(self):
        pass

    def lastReg(self):
        msgLastReg = ', aqui estão os últimos registros das suas SensiTags.\n\n'
        conn = sqlite3.connect(dataBaseDjangoDir)
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM tags_tag""")
        conn.commit()
        query = (cursor.fetchall())
        for tag in query:
            connSensi = sqlite3.connect(dataBaseSensiDir)
            cursorSensi = conn.cursor()
            querySet = "SELECT * FROM reg order by id desc LIMIT 1 WHERE MAC = " + tag[1]
            print(querySet)
            cursorSensi.execute(querySet)
            connSensi.commit()
            querySensi = (cursorSensi.fetchall())
            print(querySensi)

        return msgLastReg


    def getInfo(self):
        conn = sqlite3.connect(dataBaseDjangoDir)
        cursor = conn.cursor()
        cursor.execute("""select * from tags_tag""")
        conn.commit()
        query = (cursor.fetchall())
        msgTags = ", aqui estão as informações sobre as suas SensiTags.\n\n "
        for tag in query:
            msgTags = msgTags + '*->* MAC: *' + tag[1] + '*\n'
            msgTags = msgTags + '     Localização: *' + tag[2] + '*\n\n'
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

                try:
                    conn = sqlite3.connect(dataBaseSensiDir)
                    cursor = conn.cursor()
                    cursor.executemany("""
                        INSERT INTO reg (MAC, BATERIA, TEMPERATURA,UMIDADE,ANO,MES,DIA,HORA,MINUTO,SEGUNDO)
                        VALUES (?,?,?,?,?,?,?,?,?,?)
                        """, vetor)
                    conn.commit()
                    conn.close()
                except KeyError:
                    print ('erro do banco')

            except KeyError:
                print ('tag n encontrada: ' + mac)