from ruuvitag_sensor.ruuvitag import RuuviTag
import os
import datetime
import time

sensor = RuuviTag('D7:05:12:28:73:D9')
i = 0
while 1:
    print(i)
    i = i + 1
    # update state from the device
    state = sensor.update()

    # get latest state (does not get it from the device)
    state = sensor.state




    for var in state:
        print(var +" : " +str( state[var]) )

    date = datetime.datetime.now()
    print("Ano : " + str(date.year))
    print("Mês : " + str(date.month))
    print("dia : " + str(date.day))
    print("hora : " + str(date.hour))
    print("minuto : " + str(date.minute))
    print("segundo : " + str(date.second))
    print("\n\n--------------------------\n\n")


