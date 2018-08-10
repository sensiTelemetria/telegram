import random
class Help:
    msgPadrao = None
    chat_id = None

    def __init__(self, chat_id):
        self.chat_id = chat_id
        #todo lista padrao de ajuda do bot

        boasVindas = ["olá!", "olá! Aqui é a Sensi!", "Sensi aqui!", "Ei!", "Me chamou?"]
        msgPadrao = random.choice(boasVindas) + "\n" + "Não entendi oq vc disse... mas posso te ajudar: "

        msgPadrao = msgPadrao +"\n\n*->* /infoUsers -" + " Para saber mais sobre os usuários do sistema"

        msgPadrao = msgPadrao + "\n\n*->* ultimo registro da SensiTag :"
        msgPadrao = msgPadrao + "/SensiTag"

        msgPadrao = msgPadrao + "\n\n*->* Reiniciar o sistema :"
        self.msgPadrao = msgPadrao + "/reboot"

    def helpMessage(self):
        return self.msgPadrao


    def get_mensagem_Padrao(self):
        boasVindas = ["olá!", "Sensi aqui!", "Ei!", "Me chamou?"]
        msg = random.choice(boasVindas) + "\nAcho que vc esta precisando de ajuda! Deixe-me ajudar vc:"
        msg = msg + self.msgPadrao
        return msg

    def get_mensagem_nao_reconhecida(self):
        boasVindas = ["olá!","olá! Aqui é a Sensi!", "Sensi aqui!", "Ei!", "Me chamou?"]
        msg = random.choice(boasVindas) + "\n" + "Não entendi oq vc disse... mas posso te ajudar: "
        msg = msg + self.msgPadrao
        return msg


