import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import sqlite3
from settings import dataBaseDjangoDir, dataBaseSensiDir,timeout_in_sec, tempDir, nameCompany, site, logoSensi
import os
import datetime
import matplotlib.dates as mdates
import time
from reportlab.lib.enums import TA_JUSTIFY,TA_CENTER
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm

class Reports:

    def makeReportOneDayAll(self, numberRegs):

        print('\ncomeçandooooooo\n')

        date = datetime.datetime.now()
        pdfName = "ReportOneDayAll"
        dir = tempDir + pdfName + ".pdf"
        print(dir)
        doc = SimpleDocTemplate(dir, pagesize=A4,
                                rightMargin=72, leftMargin=72,
                                topMargin=72, bottomMargin=18)
        # dados sensi para pdf
        Story = []
        dateNow = str(date.day) + "/" + str(date.month) + "/" + str(date.year) + " - " + str(
            date.hour) + ":" + str(date.minute)

        im = Image(logoSensi, 7 * cm, 7 * cm)
        Story.append(im)

        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
        styles.add(ParagraphStyle(name='center', alignment=TA_CENTER))

        # SENSI
        ptext = '<font size=14>%s</font>' % nameCompany
        Story.append(Paragraph(ptext, styles["center"]))
        Story.append(Spacer(1, 12))

        # SENSI site
        ptext = '<font size=14>%s</font>' % site
        Story.append(Paragraph(ptext, styles["center"]))
        Story.append(Spacer(1, 36))

        # DADOS RELATORIOS

        ptext = '<font size=14>Data: %s</font>' % dateNow
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))

        ptext = '<font size=14>Detalhe: Relatório completo de todas as SensiTags no període de 24 horas</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))

        conn = sqlite3.connect(dataBaseDjangoDir)
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM tags_tag""")
        conn.commit()
        query = (cursor.fetchall())
        # trata se não existir SensiTags
        if len(query) > 0:

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
                        batery.append(float(reg[2] / 1000))
                        date = datetime.datetime(reg[5], reg[6], reg[7], reg[8], reg[9], reg[10], )
                        time.append(date)
                # Data for plotting

                if len(querySensi) > 0:
                    # grfico de temperatura
                    fig, ax = plt.subplots()
                    plt.close('all')
                    ax.plot(time, temperature)
                    ax.set(ylabel='Temperatura (ºC)',
                           title="SensiTag: " + local + " - MAC: " + mac + "\nTemperatura")
                    ax.grid()
                    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%y - %H:%M'))
                    ax.xaxis.label.set_size(50)
                    # rotate and align the tick labels so they look better
                    fig.autofmt_xdate()
                    fig.savefig(tempDir + mac + "_Temperatura_reportAll1day.png")

                    # grfico de umidade
                    fig, ax = plt.subplots()
                    plt.close('all')
                    ax.plot(time, humidity)
                    ax.set(ylabel='Umidade (%)',
                           title="SensiTag: " + local + " - MAC: " + mac + "\nUmidade")
                    ax.grid()
                    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%y - %H:%M'))

                    # rotate and align the tick labels so they look better
                    fig.autofmt_xdate()
                    fig.savefig(tempDir + mac + "_Umidade_reportAll1day.png")

                    # grfico de bateria
                    fig, ax = plt.subplots()
                    plt.close('all')
                    ax.plot(time, batery)
                    ax.set(ylabel='Bateria (V)',
                           title="SensiTag: " + local + " - MAC: " + mac + "\nBateria")
                    ax.grid()
                    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%y - %H:%M'))
                    # rotate and align the tick labels so they look better
                    fig.autofmt_xdate()
                    fig.savefig(tempDir + mac + "_Bateria_reportAll1day.png")

                    # envio de gráficos por SensiTags
                    Story.append(PageBreak())
                    im = Image(tempDir + mac + "_Temperatura_reportAll1day.png", 20 * cm, 15 * cm)
                    Story.append(im)
                    # os.system("rm " + tempDir + str(mac) + "_Temperatura_reportAll1day.png")

                    Story.append(PageBreak())
                    im = Image(tempDir + str(mac) + "_Umidade_reportAll1day.png", 20 * cm, 15 * cm)
                    Story.append(im)
                    # os.system("rm " + tempDir + str(mac) + "_Umidade_reportAll1day.png")

                    Story.append(PageBreak())
                    im = Image(tempDir + str(mac) + "_Bateria_reportAll1day.png", 20 * cm, 15 * cm)
                    Story.append(im)
                    # os.system("rm " + tempDir + str(mac) + "_Bateria_reportAll1day.png") , 20 * cm, 15 * cm


                else:
                    pass
        else:
            print('\nNao existem TAGS!\n')

        print('\nmakeReportOneDayAll feito!\n')
        doc.build(Story)
        os.system("rm " + tempDir + "*.png")


    def sendReportOneDayAll(self, bot, chat_id):
        try:
            #self.makeReportOneDayAll(288)
            pdfName = "ReportOneDayAll"
            dir = tempDir + pdfName + ".pdf"
            bot.send_document(chat_id, open(dir, "rb"), timeout=40)
        except FileNotFoundError:
            msg = 'Ops!\nNão achei nenhum PDF para te enviar!'
            bot.send_message(chat_id, msg, parse_mode="markdown")
