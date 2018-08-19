import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
from settings import tempDir, dataBaseDjangoDir, dataBaseSensiDir
import sqlite3
import datetime
import matplotlib.dates as mdates

class Graphics:

    def getInfo(self):
        msg = ', vou te enviar os gráficos de suas SensiTags '
        return  msg

    def getSensiTags(self):
        conn = sqlite3.connect(dataBaseDjangoDir)
        cursor = conn.cursor()
        cursor.execute("""select * from tags_tag""")
        conn.commit()
        query = (cursor.fetchall())
        return query

    def makeGraphicAll(self, numberRegs):

        conn = sqlite3.connect(dataBaseDjangoDir)
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM tags_tag""")
        conn.commit()
        query = (cursor.fetchall())
        for tag in query:

            time = []
            batery = []
            humidity = []
            temperature = []
            mac = ''

            connSensi = sqlite3.connect(dataBaseSensiDir)
            cursorSensi = connSensi.cursor()
            # querySet = "SELECT * FROM reg WHERE MAC = '" + tag[1]+ "' order by id desc LIMIT 1"
            querySet = "SELECT * FROM reg WHERE MAC = '" + tag[1] + "' order by id desc LIMIT " + str(numberRegs)
            cursorSensi.execute(querySet)
            connSensi.commit()
            querySensi = (cursorSensi.fetchall())

            mac = tag[1]
            local = tag[2]

            for reg in querySensi:
                if len(reg) != 0:
                    temperature.append(reg[3])
                    humidity.append(reg[4])
                    batery.append(float(reg[2]/1000))
                    date = datetime.datetime(reg[5], reg[6], reg[7], reg[8], reg[9], reg[10],)
                    time.append(date)
            # Data for plotting

            if len(querySensi) > 0:
                fig, ax = plt.subplots()
                ax.plot(time, temperature)
                ax.set( ylabel='Temperatura (ºC)',
                       title= "SensiTag: " + local + " - MAC: " + mac + "\nTemperatura")
                ax.grid()
                ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%y - %H:%M'))
                # rotate and align the tick labels so they look better
                fig.autofmt_xdate()
                fig.savefig(tempDir+mac + "_Temperatura.png")

                fig, ax = plt.subplots()
                ax.plot(time, humidity)
                ax.set( ylabel='Umidade (%)',
                       title="SensiTag: " + local + " - MAC: " + mac + "\nUmidade")
                ax.grid()
                ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%y - %H:%M'))
                # rotate and align the tick labels so they look better
                fig.autofmt_xdate()
                fig.savefig(tempDir+mac + "_Umidade.png")

                fig, ax = plt.subplots()
                ax.plot(time, batery)
                ax.set(ylabel='Bateria (V)',
                       title="SensiTag: " + local + " - MAC: " + mac + "\nBateria")
                ax.grid()
                ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%y - %H:%M'))
                # rotate and align the tick labels so they look better
                fig.autofmt_xdate()
                fig.savefig(tempDir+mac + "_Bateria.png")
