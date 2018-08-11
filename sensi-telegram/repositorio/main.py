#!/usr/bin/env python
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
#/home/pi/telegram_env365/bin/python3.6 /home/pi/Desktop/Sensi/SensiTelegram/main.py
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import sqlite3
from Ajuda import Ajuda
from Info import Info
from Tags import ultimoReg
import datetime
import time
import os
from uuid import uuid4
from telegram.utils.helpers import escape_markdown
from telegram import InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import logging


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
    ajuda = Ajuda()
    msg = ajuda.get_mensagem_Padrao()
    bot.send_message(update.message.chat_id, msg, parse_mode="markdown")


def msg_nao_reconhecida(bot, update):
    ajuda = Ajuda()
    msg = ajuda.get_mensagem_nao_reconhecida()
    bot.send_message(update.message.chat_id, msg, parse_mode="markdown")

def pdf(bot, update):
    bot.send_message(update.message.chat_id, "Enviando gráficos em pdf!", parse_mode="markdown")
    bot.send_document(update.message.chat_id, open("multipage.pdf", "rb"))
    bot.send_document(update.message.chat_id, open("form_letter.pdf", "rb"))


def info(bot, update):
    nomeCliente = "Banco de sangue HUCAM"
    numeroTags = 10
    nomeEmpresa = "Sensi telemetria"
    telefoneContato = "27 98983908"
    email = "talles.dsv@gmail.com"
    contato = "@tallesvaliatti"
    site = "www.sensitelemetria.com"

    infom = Info(nomeCliente, numeroTags, nomeEmpresa, telefoneContato,email,contato,site)

    bot.send_message(update.message.chat_id, infom.get_info() , parse_mode = "markdown")

def callback_minute(bot, job):
    bot.send_message(chat_id=452147385, text='One message every 6000 seconds')

def callback_daily(bot, job):
    bot.send_message(chat_id=452147385, text='One message every day')

#trata as menssagem
def echo(bot, update):
    msg_recebida = update.message.text.lower().split(" ")
    print(msg_recebida)
    print("\n\n\n---------------------------------------------------------------------------")
    print("Mensagem recebida --> ", msg_recebida)
    print("chat ID --> ", update.message.chat_id)
    print("chat ID type--> ", type( update.message.chat_id))

    # todo fazer tratamento de autorizacao
    if 1:
        #todo tratamento dos comandos
        if 0:
            pass

        #ajuda
        elif "ajuda" in msg_recebida  or "sensi" in msg_recebida :
            help(bot, update)

        # informaçãoes gerais
        elif "info" in msg_recebida or "informacoes" in msg_recebida:
            info(bot, update)

        #mensagem não reconhecida
        else:
            msg_nao_reconhecida(bot, update)
    else:
        bot.send_message(update.message.chat_id, "Ei, Meu nome é Sensi!\nInfelizmente vc não está autorizado para acessar esse sistema.\nDesculpe!")

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def SensiTag(bot, update):
    msg = "enviando ultimo registro da tag"
    bot.send_message(update.message.chat_id, msg, parse_mode="markdown")
    ultimoReg(bot,update)

def reboot(bot, update):
    msg = "reiniciando o sistema, já volto!"
    bot.send_message(update.message.chat_id, msg, parse_mode="markdown")
    os.system("sudo reboot")

def main():
    os.system('clear')
    """Start the bot."""
    print('iniciando boot...')
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("610394079:AAE_vKj4QludEXOu_A9yGicxS5rafOmUWVE")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    #repeticao de envio de menssagens
    j = updater.job_queue
    day = datetime.datetime.now() + datetime.timedelta(seconds=30)
    print(day.time())
    j.run_repeating(callback_minute, interval=6000, first=0)

    j.run_daily(callback_daily, day.time())

    os.system("/home/pi/telegram_env365/bin/python3.6 /home/pi/Desktop/Sensi/SensiTelegram/data_tag.py &")

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("info", info))
    dp.add_handler(CommandHandler("info", msg_nao_reconhecida))
    dp.add_handler(CommandHandler("pdf", pdf))
    dp.add_handler(CommandHandler("SensiTag", SensiTag))
    dp.add_handler(CommandHandler("reboot", reboot))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)



    # Start the Bot
    print('polling...')
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()