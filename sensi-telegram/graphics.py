import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
from settings import tempDir, dataBaseDjangoDir, dataBaseSensiDir
import sqlite3
import datetime

class Graphics:

    def getInfo(self):
        msg = ', aqui estão os gráficos de suas SensiTags do '
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
            querySet = "SELECT * FROM reg WHERE MAC = '" + tag[1] + "' order by id asc LIMIT " + str(numberRegs)
            cursorSensi.execute(querySet)
            connSensi.commit()
            querySensi = (cursorSensi.fetchall())
            for reg in querySensi:
                if len(reg) != 0:

                    mac = reg[1]
                    temperature.append(reg[3])
                    humidity.append(reg[4])
                    batery.append(float(reg[2]/1000))
                    date = datetime.datetime(reg[5], reg[6], reg[7], reg[8], reg[9], reg[10],)
                    time.append(date)
            # Data for plotting

            fig, ax = plt.subplots()
            ax.plot(time, temperature)
            ax.set(xlabel='tempo', ylabel='Temperatura (ºC)',
                   title= " Tag: " + mac + " - temperatura\nSensiTags")
            ax.grid()
            # rotate and align the tick labels so they look better
            fig.autofmt_xdate()
            fig.savefig(tempDir+mac + "_Temperatura.png")

            fig, ax = plt.subplots()
            ax.plot(time, humidity)
            ax.set(xlabel='tempo', ylabel='Umidade (%)',
                   title=" Tag: " + mac + " - Umidade.png")
            ax.grid()
            # rotate and align the tick labels so they look better
            fig.autofmt_xdate()
            fig.savefig(tempDir+mac + "_Umidade.png")

            fig, ax = plt.subplots()
            ax.plot(time, batery)
            ax.set(xlabel='tempo', ylabel='Bateria (V)',
                   title=" Tag: " + mac + " - Bateria.png")
            ax.grid()
            # rotate and align the tick labels so they look better
            fig.autofmt_xdate()
            fig.savefig(tempDir+mac + "_Bateria.png")
