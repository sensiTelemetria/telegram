from ruuvitag_sensor.ruuvi import RuuviTagSensor
import os
import datetime
import time


# List of macs of sensors which data will be collected
# If list is empty, data will be collected for all found sensors
macs = ['D7:05:12:28:73:D9', 'F7:82:69:C1:8A:F9' ]
# get_data_for_sensors will look data for the duration of timeout_in_sec
timeout_in_sec = 10
while 1:
    datas = RuuviTagSensor.get_data_for_sensors(macs, timeout_in_sec)
    # Dictionary will have lates data for each sensor
    for mac in macs:
        try:
            tag = datas[mac]
            # print(datas['D7:05:12:28:73:D9'])
            for var in tag:
                print(var + " : " + str(tag[var]))

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
            print ('continua')

    time.sleep(5)