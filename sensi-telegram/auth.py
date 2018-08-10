import sqlite3
from settings import dataBaseDir
from help import Help
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

class Auth:
    name = ''
    chat_id = None
    authorize = False
    help = None
    def __init__(self, chat_id):
        conn = sqlite3.connect(dataBaseDir)
        cursor = conn.cursor()
        cursor.execute("""select * from usuarios_usuario""")
        conn.commit()
        query = (cursor.fetchall())
        for user in query:
            if user[4] == chat_id:
                self.name = user[1]
                self.authorize = True
                self.help = Help(chat_id)
        self.chat_id = chat_id



    def authUser(self):
        return not self.authorize

    def unauthorized(self, bot):
        conn = sqlite3.connect(dataBaseDir)
        cursor = conn.cursor()
        cursor.execute("""select * from usuarios_usuario""")
        conn.commit()
        query = (cursor.fetchall())

        msg = 'Ei, meu nome Sensi!\n'
        msg = msg + 'Infelizmente vc não tem permissão para acessar meus dados.\n'
        msg = msg + '\nEntre em contato com uma das pessoas abaixo para se cadastrar no sistema:\n\n'
        for user in query:
            msg = msg + '*->* '
            msg = msg + '*' + user[1]+ '* - *' + str(user[3]) +'*\n'
        msg = msg + '\nAvise eles que seu chat id é: *' + str(self.chat_id) +'*'
        bot.send_message(self.chat_id, msg, parse_mode="markdown")

    def infoUsers(self, bot):
        msg = 'Ei, ' + self.name + '!\n'
        msg = msg + 'Aqui está a lista de usuários do meu sistema:\n\n'

        conn = sqlite3.connect(dataBaseDir)
        cursor = conn.cursor()
        cursor.execute("""select * from usuarios_usuario""")
        conn.commit()
        query = (cursor.fetchall())

        for user in query:
            msg = msg + '*->* nome: *' + user[1] + '*\n'
            msg = msg + '     e-mail: *' + user[2] + '*\n'
            msg = msg + '     telefone: *' + str(user[3]) + '*\n'
            msg = msg + '     chat id: *' + str(user[4]) + '*\n\n'
        msg = msg + 'Precisando de mais alguma coisa? É só me chamar :)'
        bot.send_message(self.chat_id, msg, parse_mode="markdown")

    def getHelp(self, bot):
        bot.send_message(self.chat_id, self.help.helpMessage(), parse_mode="markdown")