import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, filters
import logging
import json
import requests
import sys

TOKEN = "1441356682:AAGpv8nK7KfOTz_NDNXtt-oUUUWGixcZKno"

bot = telegram.Bot(token=TOKEN)
updater = Updater(token=TOKEN)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

dispatcher = updater.dispatcher
bot = telegram.Bot(token=TOKEN)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                     text="oleg romanchishin kooritb na perervee")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def shosb(update, context):
    try:
        msg = update.message.text
        
        context.bot.send_message(chat_id=update.effective_chat.id, text =(msg), parse_mode=telegram.ParseMode.MARKDOWN)

    except Exception as error:
        print('Caught this error: ' + repr(error))
        context.bot.send_message(chat_id=update.effective_chat.id, text =("error lol"), parse_mode=telegram.ParseMode.MARKDOWN)
        raise error.with_traceback(sys.exc_info()[2])

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

handler = MessageHandler(filters.Filters.text, shosb)
dispatcher.add_handler(handler)

updater.start_polling()
updater.idle()
