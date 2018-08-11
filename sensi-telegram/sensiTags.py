from settings import dataBaseDjangoDir
from ruuvitag_sensor.ruuvi import RuuviTagSensor
import os
import datetime
import time
class SensiTags:

    def __init__(self):
        pass

    def getInfo(self):
        conn = sqlite3.connect(dataBaseDjangoDir)
        cursor = conn.cursor()
        cursor.execute("""select * from tags_tag""")
        conn.commit()
        query = (cursor.fetchall())
        return query

    def getData(self):
        macs = ['D7:05:12:28:73:D9', 'F7:82:69:C1:8A:F9']
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