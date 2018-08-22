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

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from auth import Auth
import os
from sensiTags import SensiTags
import sqlite3
from sensiTags import SensiTags
from settings import dataBaseDjangoDir
from settings import DataInterval, reportOneDayAllInterval
from reports import Reports
import os

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def systemInit(bot, job):
    conn = sqlite3.connect(dataBaseDjangoDir)
    cursor = conn.cursor()
    cursor.execute("""select * from usuarios_usuario""")
    conn.commit()
    query = (cursor.fetchall())

    for user in query:
        msg = "Sistema no ar!\nBem-vindo de volta *" +user[1]+ "*"
        bot.send_message(user[4], msg, parse_mode="markdown")


def start(bot, update):
    conn = sqlite3.connect(dataBaseDjangoDir)
    cursor = conn.cursor()
    cursor.execute("""select * from usuarios_usuario""")
    conn.commit()
    query = (cursor.fetchall())

    msg = 'Ei, meu nome *Sensi*!\n'
    msg = msg + '\nEntre em contato com uma das pessoas abaixo para se cadastrar no sistema:\n\n'
    for user in query:
        msg = msg + '*->* '
        msg = msg + '*' + user[1] + '* - *' + str(user[3]) + '*\n'
    msg = msg + '\nEnvie seu *nome*, *email*, *telefone* e avise que seu chat id é: *' + str(update.message.chat_id) + '*'
    bot.send_message(update.message.chat_id, msg, parse_mode="markdown")


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(bot, update):
    user = Auth(update.message.chat_id, bot)
    if user.authUser():
        user.getHelp(bot)
    else:
        user.unauthorized(bot)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    bot.send_message(update.message.chat_id, "Ops!\nParece que tivemos um probleminha!\nTente Denovo!", parse_mode="markdown")
    logger.warning('Update "%s" caused error "%s"', update, error)

def infoUsers(bot, update):
    user = Auth(update.message.chat_id, bot)
    if user.authUser():
        user.infoUsers(bot)
    else:
        user.unauthorized(bot)

def infoSystem(bot, update):
    user = Auth(update.message.chat_id, bot)
    if user.authUser():
        user.infoSystem(bot)
    else:
        user.unauthorized(bot)

def infoTags(bot, update):
    user = Auth(update.message.chat_id, bot)
    if user.authUser():
        user.infoTags(bot)
    else:
        user.unauthorized(bot)

def lastReg(bot, update):
    user = Auth(update.message.chat_id, bot)
    if user.authUser():
        user.lastReg(bot)
    else:
        user.unauthorized(bot)

def reportOneDay(bot, update):
    user = Auth(update.message.chat_id, bot)
    if user.authUser():
        user.reportOneDayAll(bot)
    else:
        user.unauthorized(bot)

def report3Days(bot, update):
    user = Auth(update.message.chat_id, bot)
    if user.authUser():
        user.report3DaysAll(bot)
    else:
        user.unauthorized(bot)

def report7Days(bot, update):
    user = Auth(update.message.chat_id, bot)
    if user.authUser():
        user.report7DaysAll(bot)
    else:
        user.unauthorized(bot)

def graphicsOneDay(bot, update):
    user = Auth(update.message.chat_id, bot)
    if user.authUser():
        user.graphicsOneDay(bot)
    else:
        user.unauthorized(bot)

def graphics3Day(bot, update):
    user = Auth(update.message.chat_id, bot)
    if user.authUser():
        user.graphics3Day(bot)
    else:
        user.unauthorized(bot)

def graphicsOneWeek(bot, update):
    user = Auth(update.message.chat_id, bot)
    if user.authUser():
        user.graphicsOneWeek(bot)
    else:
        user.unauthorized(bot)


def reboot(bot, update):
    user = Auth(update.message.chat_id, bot)
    if user.authUser():
        user.reboot(bot)
    else:
        user.unauthorized(bot)

def alarmsInfo(bot, update):
    user = Auth(update.message.chat_id, bot)
    if user.authUser():
        user.alarmsInfo(bot)
    else:
        user.unauthorized(bot)

def getData(bot, job):
    sensiTags = SensiTags(bot)
    sensiTags.getData()


def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("658797821:AAHWt2NeY4vm2OhaBxqIVmFXj87Zp60FNp8")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("infoUsers", infoUsers))
    dp.add_handler(CommandHandler("infoSystem", infoSystem))
    dp.add_handler(CommandHandler("infoTags", infoTags))
    dp.add_handler(CommandHandler("lastReg", lastReg))
    dp.add_handler(CommandHandler("graphicsOneDay", graphicsOneDay))
    dp.add_handler(CommandHandler("graphics3Day", graphics3Day))
    dp.add_handler(CommandHandler("graphicsOneWeek", graphicsOneWeek))
    dp.add_handler(CommandHandler("alarmsInfo", alarmsInfo))
    dp.add_handler(CommandHandler("reportOneDay", reportOneDay))
    dp.add_handler(CommandHandler("report3Days", report3Days))
    dp.add_handler(CommandHandler("report7Days", report7Days))
    dp.add_handler(CommandHandler("reboot", reboot))



    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))


    j = updater.job_queue
    j.run_once(systemInit, 0)
    j.run_repeating(getData, interval=DataInterval, first=0)




   # os.system('/home/pi/sensi/bin/python3.6 /home/pi/Desktop/telegram/sensi-telegram/specified_tags.py & ')
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