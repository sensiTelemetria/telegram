import random
class Ajuda ():

    #todo lista padrao de ajuda do bot
    msgPadrao = "\n\n*->* Para saber mais sobre o seu sistema instalado :"
    msgPadrao = msgPadrao + "/info"

    msgPadrao = msgPadrao + "\n\n*->* Para saber mais sobre o seu sistema instalado :"
    msgPadrao = msgPadrao + "/info"

    msgPadrao = msgPadrao + "\n\n*->* Para saber mais sobre o seu sistema instalado :"
    msgPadrao = msgPadrao + "/info"

    msgPadrao = msgPadrao + "\n\n*->* ultimo registro da SensiTag :"
    msgPadrao = msgPadrao + "/SensiTag"

    msgPadrao = msgPadrao + "\n\n*->* Reiniciar o sistema :"
    msgPadrao = msgPadrao + "/reboot"



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


