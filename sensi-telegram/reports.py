import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import sqlite3
from settings import dataBaseDjangoDir, dataBaseSensiDir,timeout_in_sec, tempDir, nameCompany, site, logoSensi,DataInterval
import os
import datetime
import matplotlib.dates as mdates
import time
from reportlab.lib.enums import TA_JUSTIFY,TA_CENTER
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
import numpy as np

class Reports:


    def makeReportAll(self, bot, chat_id, numberRegs, numberDays):
        date = datetime.datetime.now()
        pdfName = ''
        if numberDays == 1:
            pdfName = "ReportOneDayAll"
        if numberDays == 3:
            pdfName = "Report3DaysAll"
        if numberDays == 7:
            pdfName = "Report7DaysAll"

        dir = tempDir + pdfName + ".pdf"
        print(dir)
        doc = SimpleDocTemplate(dir, pagesize=A4,
                                rightMargin=72, leftMargin=72,
                                topMargin=72, bottomMargin=18)
        # dados sensi para pdf
        Story = []

        dateNow = date.strftime('%d/%m/%y - %H:%M')
        #dateNow = str(date.day) + "/" + str(date.month) + "/" + str(date.year) + " - " + str(date.hour) + "H" + str(date.minute)

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

        ptext = ''
        if numberDays == 1:
            ptext = '<font size=14>Detalhe: Relatório completo de todas as SensiTags no período de 24 horas</font>'
        if numberDays == 3:
            ptext = '<font size=14>Detalhe: Relatório completo de todas as SensiTags no período de 48 horas</font>'
        if numberDays == 7:
            ptext = '<font size=14>Detalhe: Relatório completo de todas as SensiTags no período de 72 horas</font>'

        ptext = '<font size=14>%s</font>'% ptext
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
                    matplotlib.rc('xtick', labelsize=10)

                    fig, ax = plt.subplots()
                    plt.close('all')
                    ax.plot(time, temperature)
                    ax.set(ylabel='Temperatura (ºC)')
                    ax.grid()
                    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%y - %H:%M'))
                    # rotate and align the tick labels so they look better
                    fig.autofmt_xdate()
                    fig.savefig(tempDir + mac + "_Temperatura_reportAll.png")

                    # grfico de umidade
                    fig, ax = plt.subplots()
                    plt.close('all')
                    ax.plot(time, humidity)
                    ax.set(ylabel='Umidade (%)')

                    ax.grid()
                    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%y - %H:%M'))

                    # rotate and align the tick labels so they look better
                    fig.autofmt_xdate()
                    fig.savefig(tempDir + mac + "_Umidade_reportAll.png")

                    # grfico de bateria
                    fig, ax = plt.subplots()
                    plt.close('all')
                    ax.plot(time, batery)
                    ax.set(ylabel='Bateria (V)')
                    ax.grid()
                    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%y - %H:%M'))
                    # rotate and align the tick labels so they look better
                    fig.autofmt_xdate()
                    fig.savefig(tempDir + mac + "_Bateria_reportAll.png")

                    # envio de gráficos por SensiTags
                    Story.append(PageBreak())
                    im = Image(tempDir + mac + "_Temperatura_reportAll.png", 20 * cm, 15 * cm)
                    Story.append(im)

                    #dados temperatura
                    Story.append(Spacer(1, 12))
                    ptext = '<font size=14>MAC: %s</font>' % mac
                    Story.append(Paragraph(ptext, styles["Justify"]))
                    Story.append(Spacer(1, 12))

                    ptext = '<font size=14>Localização: %s</font>' % local
                    Story.append(Paragraph(ptext, styles["Justify"]))
                    Story.append(Spacer(1, 12))

                    getDateTime = 'realizada a cada ' + str(DataInterval)+ ' segundos'
                    ptext = '<font size=14>Coleta de dados: %s</font>' % getDateTime
                    Story.append(Paragraph(ptext, styles["Justify"]))
                    Story.append(Spacer(1, 12))

                    #estatisticas
                    average =  float(sum(temperature) / float(len(temperature)))
                    average = round(average, 2)

                    variance = np.var(temperature)
                    variance.round(decimals=2)

                    std = np.std(temperature)
                    std.round(decimals=2)

                    maxValue = (max(temperature))
                    minValue = (min(temperature))

                    ptext = '<font size=14>Média: %s</font>' % str(average)
                    Story.append(Paragraph(ptext, styles["Justify"]))
                    Story.append(Spacer(1, 12))

                    ptext = '<font size=14>Variância: %s</font>' % str(variance)
                    Story.append(Paragraph(ptext, styles["Justify"]))
                    Story.append(Spacer(1, 12))

                    ptext = '<font size=14>Desvio padrão: %s</font>' % str(std)
                    Story.append(Paragraph(ptext, styles["Justify"]))
                    Story.append(Spacer(1, 12))

                    ptext = '<font size=14>Valor máximo: %s</font>' % str(maxValue)
                    Story.append(Paragraph(ptext, styles["Justify"]))
                    Story.append(Spacer(1, 12))

                    maxTimeIndex = temperature.index(min(temperature))
                    maxTime = time[maxTimeIndex]
                    maxTime = maxTime.strftime('%d/%m/%y - %H:%M')
                    ptext = '<font size=14>Valor máximo em: %s</font>' % str(maxTime)
                    Story.append(Paragraph(ptext, styles["Justify"]))
                    Story.append(Spacer(1, 12))

                    ptext = '<font size=14>Valor mínimo: %s</font>' % str(minValue)
                    Story.append(Paragraph(ptext, styles["Justify"]))
                    Story.append(Spacer(1, 12))

                    minTimeIndex = temperature.index(min(temperature))
                    minTime = time[minTimeIndex]
                    minTime = minTime.strftime('%d/%m/%y - %H:%M')
                    ptext = '<font size=14>Valor mínimo em: %s</font>' % str(minTime)
                    Story.append(Paragraph(ptext, styles["Justify"]))
                    Story.append(Spacer(1, 12))

                    # dados Umidade
                    Story.append(PageBreak())
                    im = Image(tempDir + str(mac) + "_Umidade_reportAll.png", 20 * cm, 15 * cm)
                    Story.append(im)
                    Story.append(Spacer(1, 12))
                    ptext = '<font size=14>MAC: %s</font>' % mac
                    Story.append(Paragraph(ptext, styles["Justify"]))
                    Story.append(Spacer(1, 12))

                    ptext = '<font size=14>Localização: %s</font>' % local
                    Story.append(Paragraph(ptext, styles["Justify"]))
                    Story.append(Spacer(1, 12))

                    getDateTime = 'realizada a cada ' + str(DataInterval) + ' segundos'
                    ptext = '<font size=14>Coleta de dados: %s</font>' % getDateTime
                    Story.append(Paragraph(ptext, styles["Justify"]))
                    Story.append(Spacer(1, 12))

                    # estatisticas
                    average = float(sum(humidity) / float(len(humidity)))
                    average = round(average, 2)

                    variance = np.var(humidity)
                    variance.round(decimals=2)

                    std = np.std(humidity)
                    std.round(decimals=2)

                    maxValue = (max(humidity))
                    minValue = (min(humidity))

                    ptext = '<font size=14>Média: %s</font>' % str(average)
                    Story.append(Paragraph(ptext, styles["Justify"]))
                    Story.append(Spacer(1, 12))

                    ptext = '<font size=14>Variância: %s</font>' % str(variance)
                    Story.append(Paragraph(ptext, styles["Justify"]))
                    Story.append(Spacer(1, 12))

                    ptext = '<font size=14>Desvio padrão: %s</font>' % str(std)
                    Story.append(Paragraph(ptext, styles["Justify"]))
                    Story.append(Spacer(1, 12))

                    ptext = '<font size=14>Valor máximo: %s</font>' % str(maxValue)
                    Story.append(Paragraph(ptext, styles["Justify"]))
                    Story.append(Spacer(1, 12))

                    maxTimeIndex = humidity.index(min(humidity))
                    maxTime = time[maxTimeIndex]
                    maxTime = maxTime.strftime('%d/%m/%y - %H:%M')
                    ptext = '<font size=14>Valor máximo em: %s</font>' % str(maxTime)
                    Story.append(Paragraph(ptext, styles["Justify"]))
                    Story.append(Spacer(1, 12))

                    ptext = '<font size=14>Valor mínimo: %s</font>' % str(minValue)
                    Story.append(Paragraph(ptext, styles["Justify"]))
                    Story.append(Spacer(1, 12))

                    minTimeIndex = humidity.index(min(humidity))
                    minTime = time[minTimeIndex]
                    minTime = minTime.strftime('%d/%m/%y - %H:%M')
                    ptext = '<font size=14>Valor mínimo em: %s</font>' % str(minTime)
                    Story.append(Paragraph(ptext, styles["Justify"]))
                    Story.append(Spacer(1, 12))

                    # dados bateria
                    Story.append(PageBreak())
                    im = Image(tempDir + str(mac) + "_Bateria_reportAll.png", 20 * cm, 15 * cm)
                    Story.append(im)

                    Story.append(Spacer(1, 12))
                    ptext = '<font size=14>MAC: %s</font>' % mac
                    Story.append(Paragraph(ptext, styles["Justify"]))
                    Story.append(Spacer(1, 12))

                    ptext = '<font size=14>Localização: %s</font>' % local
                    Story.append(Paragraph(ptext, styles["Justify"]))
                    Story.append(Spacer(1, 12))

                    getDateTime = 'realizada a cada ' + str(DataInterval) + ' segundos'
                    ptext = '<font size=14>Coleta de dados: %s</font>' % getDateTime
                    Story.append(Paragraph(ptext, styles["Justify"]))
                    Story.append(Spacer(1, 12))

                    # estatisticas
                    average = float(sum(batery) / float(len(batery)))
                    average = round(average, 2)

                    variance = np.var(batery)
                    variance.round(decimals=2)

                    std = np.std(batery)
                    std.round(decimals=2)

                    maxValue = (max(batery))
                    minValue = (min(batery))

                    ptext = '<font size=14>Média: %s</font>' % str(average)
                    Story.append(Paragraph(ptext, styles["Justify"]))
                    Story.append(Spacer(1, 12))

                    ptext = '<font size=14>Variância: %s</font>' % str(variance)
                    Story.append(Paragraph(ptext, styles["Justify"]))
                    Story.append(Spacer(1, 12))

                    ptext = '<font size=14>Desvio padrão: %s</font>' % str(std)
                    Story.append(Paragraph(ptext, styles["Justify"]))
                    Story.append(Spacer(1, 12))


                    ptext = '<font size=14>Valor mínimo: %s</font>' % str(minValue)
                    Story.append(Paragraph(ptext, styles["Justify"]))
                    Story.append(Spacer(1, 12))

                    minTimeIndex = batery.index(min(batery))
                    minTime = time[minTimeIndex]
                    minTime = minTime.strftime('%d/%m/%y - %H:%M')
                    ptext = '<font size=14>Valor mínimo em: %s</font>' % str(minTime)
                    Story.append(Paragraph(ptext, styles["Justify"]))
                    Story.append(Spacer(1, 12))

                    ptext = '<font size=14>Valor máximo: %s</font>' % str(maxValue)
                    Story.append(Paragraph(ptext, styles["Justify"]))
                    Story.append(Spacer(1, 12))

                    maxTimeIndex = batery.index(min(batery))
                    maxTime = time[maxTimeIndex]
                    maxTime = maxTime.strftime('%d/%m/%y - %H:%M')
                    ptext = '<font size=14>Valor máximo em: %s</font>' % str(maxTime)
                    Story.append(Paragraph(ptext, styles["Justify"]))
                    Story.append(Spacer(1, 12))

                else:
                    msgTag = "Ei, não achei registros da SensiTag: *" + local + "* com MAC: *" + mac + "*."
                    bot.send_message(chat_id, msgTag, parse_mode="markdown")

        doc.build(Story)
        os.system("rm " + tempDir + "*.png")


    def sendReportOneDayAll(self, bot, chat_id):
        try:
            self.makeReportAll(bot, chat_id, 288, 1)
            pdfName = "ReportOneDayAll"
            dir = tempDir + pdfName + ".pdf"
            bot.send_document(chat_id, open(dir, "rb"), timeout=40)
        except FileNotFoundError:
            msg = 'Ops!\nNão achei nenhum PDF para te enviar!'
            bot.send_message(chat_id, msg, parse_mode="markdown")

    def sendReport3DaysAll(self, bot, chat_id):
        try:
            self.makeReportAll(bot, chat_id, 864, 3)
            pdfName = "Report3DaysAll"
            dir = tempDir + pdfName + ".pdf"
            bot.send_document(chat_id, open(dir, "rb"), timeout=40)
        except FileNotFoundError:
            msg = 'Ops!\nNão achei nenhum PDF para te enviar!'
            bot.send_message(chat_id, msg, parse_mode="markdown")

    def sendReport7DaysAll(self, bot, chat_id):
        try:
            self.makeReportAll(bot, chat_id, 2016, 7)
            pdfName = "Report7DaysAll"
            dir = tempDir + pdfName + ".pdf"
            bot.send_document(chat_id, open(dir, "rb"), timeout=40)
        except FileNotFoundError:
            msg = 'Ops!\nNão achei nenhum PDF para te enviar!'
            bot.send_message(chat_id, msg, parse_mode="markdown")