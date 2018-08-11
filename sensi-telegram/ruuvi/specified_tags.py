from ruuvitag_sensor.ruuvi import RuuviTagSensor
import os
import datetime
import time


# List of macs of sensors which data will be collected
# If list is empty, data will be collected for all found sensors
macs = ['D7:05:12:28:73:D9',]
# get_data_for_sensors will look data for the duration of timeout_in_sec
timeout_in_sec = 4
i=0
while 1:
    i=i+1
    print(i )
    datas = RuuviTagSensor.get_data_for_sensors(macs, timeout_in_sec)
    # Dictionary will have lates data for each sensor
    tags = datas['D7:05:12:28:73:D9']
    #print(datas['D7:05:12:28:73:D9'])
    for var in tags:
        print(var +" : " +str( tags[var]) )
    date = datetime.datetime.now()
    print("Ano : " + str(date.year))
    print("Mês : " + str(date.month))
    print("dia : " + str(date.day))
    print("hora : " + str(date.hour))
    print("minuto : " + str(date.minute))
    print("segundo : " + str(date.second))
    print("\n\n--------------------------\n\n")
    time.sleep(5)