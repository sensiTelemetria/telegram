#!/telegram_env365/bin/
# -*- coding: utf-8 -*-

"""Simple Bot to reply to Telegram messages.
This program is dedicated to the public domain under the CC0 license.
This Bot uses the Updater class to handle the bot.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from modulos import autorizacao, info
from utilidades import ajuda
from dados import busca_valores
import os
from faz_graficos import faz_grafico
import time

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(bot, update):
    """Echo the user message."""
    
    msg_recebida = update.message.text
    print("\n---------------------------------------------------------------------------")
    print("Mensagem recebida --> ",msg_recebida)
    print("chat ID --> ",update.message.chat_id )
    
    msg_recebida = msg_recebida.split(" ")
    
    for i in range(len(msg_recebida)):
        msg_recebida[i] = msg_recebida[i].lower()
    
    
    if autorizacao(update.message.chat_id):
        
        if  msg_recebida[0].lower() == "reboot":
            os.system("sudo reboot")
            
        
        if msg_recebida[0].lower() == "ajuda" or msg_recebida[0].lower() == "help":
            bot.send_message(update.message.chat_id, ajuda(),parse_mode = "markdown")
        
##  MD4      
        elif   "md4" in msg_recebida[0] and "info" in msg_recebida and len(msg_recebida) == 2:
             bot.send_message(update.message.chat_id, info("md4"), parse_mode = "markdown")
        elif   "md4" in msg_recebida[0] and "fotos" in msg_recebida and len(msg_recebida) == 2:
            bot.send_message(update.message.chat_id,"Fotos do MD4 :")
            bot.send_photo(update.message.chat_id, open("fotos/MD4/MD4_1.jpg","rb"))
        elif   "md4" in msg_recebida[0] and "manual" in msg_recebida and len(msg_recebida) == 2:
            bot.send_document(update.message.chat_id, open("manuais/Manual_MD4.pdf","rb"))
        elif   "md4" in msg_recebida[0] and "dados" in msg_recebida and len(msg_recebida) == 2:
            bot.send_message(update.message.chat_id, busca_valores("md4"),parse_mode = "markdown")
            faz_grafico("md4","nivel")
            faz_grafico("md4","alcapao")
            faz_grafico("md4","presenca")
            faz_grafico("md4","motor1")
            faz_grafico("md4","motor2")
            bot.send_photo(update.message.chat_id, open("graficos/md4_motor1.png","rb"))
            bot.send_photo(update.message.chat_id, open("graficos/md4_motor2.png","rb"))
            bot.send_photo(update.message.chat_id, open("graficos/md4_nivel.png","rb"))
            bot.send_photo(update.message.chat_id, open("graficos/md4_alcapao.png","rb"))
            bot.send_photo(update.message.chat_id, open("graficos/md4_presenca.png","rb"))
            
##            os.system("rm graficos/md4_motor_1.png")

##    MD2
        elif   "md2" in msg_recebida[0] and "info" in msg_recebida and len(msg_recebida) == 2:
            bot.send_message(update.message.chat_id, info("md2"), parse_mode = "markdown")
        elif   "md2" in msg_recebida[0] and "fotos" in msg_recebida and len(msg_recebida) == 2:
            bot.send_message(update.message.chat_id,"Fotos do MD2:")
            bot.send_photo(update.message.chat_id, open("fotos/MD2/MD2_1.png","rb"))
            bot.send_photo(update.message.chat_id, open("fotos/MD2/MD2_2.jpg","rb"))
            bot.send_photo(update.message.chat_id, open("fotos/MD2/MD2_5.JPG","rb"))
            bot.send_photo(update.message.chat_id, open("fotos/MD2/MD2_3.JPG","rb"))
            bot.send_photo(update.message.chat_id, open("fotos/MD2/MD2_4.JPG","rb"))
            bot.send_photo(update.message.chat_id, open("fotos/MD2/MD2_6.JPG","rb"))
            bot.send_photo(update.message.chat_id, open("fotos/MD2/MD2_7.jpeg","rb"))
            bot.send_photo(update.message.chat_id, open("fotos/MD2/MD2_8.png","rb"))
            
        elif   "md2" in msg_recebida[0] and "manual" in msg_recebida and len(msg_recebida) == 2:
            bot.send_document(update.message.chat_id, open("manuais/Manual_MD2.pdf","rb"))
        elif   "md2" in msg_recebida[0] and "dados" in msg_recebida and len(msg_recebida) == 2:
            bot.send_photo(update.message.chat_id, open("graficos/test1.png","rb"))    
        else:
            bot.send_message(update.message.chat_id, "Comando nao reconhecido!\nDigite *AJUDA* para mais informacoes.",parse_mode = "markdown")  
        
    else:
        bot.send_message(update.message.chat_id, "Voce nao tem autorizacao para utilizar esse comando!\nContate o SIF para cadastro.")  
        
    
    

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    """Start the bot."""
    os.system("clear")
    print("Starting boot!\n")
    os.system("python busca_periodica.py & ")
  
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("533154007:AAFm9Oou0s2zwCODMsi_r1MHfFzQfxwNgRE")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
