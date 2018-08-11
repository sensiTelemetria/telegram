import random
from settings import *

class Help:
    msghelp = None
    msgSystem = None
    chat_id = None

    def __init__(self, chat_id):
        self.chat_id = chat_id
        #todo lista padrao de ajuda do bot
        boasVindas = ["olá!", "olá! Aqui é a Sensi!", "Sensi aqui!", "Ei!", "Me chamou?"]
        msghelp = random.choice(boasVindas) + "\n" + "Não entendi oq vc disse... mas posso te ajudar: "
        msghelp = msghelp +"\n\n*->* /infoUsers -" + " Para saber mais sobre os usuários do sistema"
        msghelp = msghelp +"\n\n*->* /infoSystem -" + " Para saber mais sobre o seu sistema"
        msghelp = msghelp +"\n\n*->* /infoTags -" + " Para saber mais sobre as SensiTags instaladas no seu sistema"
        msghelp = msghelp +"\n\n*->* /lastReg -" + " Para obter os últimos registros de suas SensiTags"

        self.msghelp = msghelp

        #mensagem sobre info do sistema
        msgSystem = ", aqui estão as informações sobre o sistema Sensi de telemetria.\n\n "
        msgSystem = msgSystem + '*->* Fundadores:\n' + owners[1][0] + ' - ' + owners[1][1] + '\n' + owners[2][0] + ' - ' + owners[2][1] + '\n\n'
        msgSystem = msgSystem + ' *->* site da empresa: ' + site + '\n'
        self.msgSystem = msgSystem

    def helpMessage(self):
        return self.msghelp

    def infoSystem(self):
        return self.msgSystem

