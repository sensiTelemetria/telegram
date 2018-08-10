from distutils.command.install_data import install_data
import sqlite3
def ultimoReg(bot,update):

    conn = sqlite3.connect('/home/pi/Desktop/Sensi/SensiTelegram/sensi.db')
    cursor = conn.cursor()
    ##
    ##
    #cursor.execute("PRAGMA TABLE_INFO(registros)")
    ##cursor.execute("DESC INFORMATION_SCHEMA.TABLES;")
    ##print(cursor.fetchall())
    ##
    ##t = ("md4","motor_1")



    #ORDER BY id DESC LIMIT 1
    cursor.execute("""SELECT * FROM reg ORDER BY id DESC LIMIT 1;""")

    ##cursor.execute("SELECT * FROM sqlite_master WHERE type='table';")

    ##cursor.execute(" DELETE FROM registros where variavel ='nivel' and valor =0  order by id desc limit 1;" )

    ##cursor.execute("""DROP TABLE registros""" )
    conn.commit()
    msg = ''
    query = (cursor.fetchall())
    for reg in query:
        msg = msg + "Registro : " + str(reg[0]) + "\n"
        msg = msg + "MAC : " + reg[1] + "\n"
        msg = msg + "Bateria : " + str(float(reg[2] / 1000)) + " V" + "\n"
        msg = msg + "temperatura : " + str(reg[3]) + "\n"
        msg = msg + "Umidade : " + str(reg[4]) + "\n"
        msg = msg + "Date : " + str(reg[7]) + "/" + str(reg[6]) + "/" + str(reg[5]) + "\n"
        msg = msg + "Hora : " + str(reg[8]) + "h" + str(reg[9]) + "m" + str(reg[10]) +"s"+ "\n"

        bot.send_message(update.message.chat_id, msg, parse_mode="markdown")


