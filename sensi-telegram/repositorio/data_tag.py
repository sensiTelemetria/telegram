from ruuvitag_sensor.ruuvitag import RuuviTag
import os
import datetime
import sqlite3
import datetime
import time
i = 0

while 1:
    conn = sqlite3.connect('/home/pi/Desktop/Sensi/SensiTelegram/sensi.db')

    cursor = conn.cursor()

    mac = "D7:05:12:28:73:D9"
    sensor = RuuviTag(mac)


    # update state from the device
    state = sensor.update()

    # get latest state (does not get it from the device)
    state = sensor.state

    print("\n------------- NOVO REGISTRO ---------------")

    print(i)
    i = i + 1

    for var in state:
        print(var +" : " +str( state[var]) )

    date = datetime.datetime.now()

    print("Ano : " + str(date.year))
    print("Mes : " + str(date.month))
    print("dia : " + str(date.day))
    print("hora : " + str(date.hour))
    print("minuto : " + str(date.minute))
    print("segundo : " + str(date.second))


    TUPLA = (mac,
             state['battery'],
             state['temperature'],
             state['humidity'],
             int(date.year),
             int(date.month),
             int(date.day),
             int(date.hour),
             int(date.minute),
             int(date.second),
             )

    vetor = [TUPLA,]

    print("VETOR : ",vetor)

    cursor.executemany("""
    INSERT INTO reg (MAC, BATERIA, TEMPERATURA,UMIDADE,ANO,MES,DIA,HORA,MINUTO,SEGUNDO)
    VALUES (?,?,?,?,?,?,?,?,?,?)
    """, vetor )

    conn.commit()
    conn.close()

    time.sleep(5)