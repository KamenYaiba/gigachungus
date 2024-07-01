from flask import Flask, request
import telebot
from config import report_a_command, report_b_command
from keys import WEBHOOK
from helpingfunctions import error_log
from handlers import (bot, start_handler, change_language_handler, report_ab_handler, about_handler, menu_handler,
                      report_manual_handler, api_report_request_handler, unexpected_error, report_help_handler)


app = Flask(__name__)


@app.route('/'+WEBHOOK, methods=["POST"])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
    chat_id = update.message.chat.id
    try:
        bot.process_new_updates([update])
    except Exception as e:
        error_log(e)
        unexpected_error(chat_id)
    return "!", 200


@bot.message_handler(commands=['start'])
def start_command(msg):
    start_handler(msg)


@bot.message_handler(commands=['menu'])
def start_command(msg):
    menu_handler(msg)


@bot.message_handler(commands=['lang'])
def change_language(msg):
    change_language_handler(msg)


@bot.message_handler(regexp='^' + '['+report_a_command+report_b_command+']')
def report_a(msg):
    report_ab_handler(msg)


@bot.message_handler(commands=["reporta", "reportb", "reportc"])
def report_manual(msg):
    report_manual_handler(msg)


@bot.message_handler(commands=['about'])
def about(msg):
    about_handler(msg)


@bot.message_handler(commands=['reporthelp'])
def report_help(msg):
    report_help_handler(msg)


@app.route('/reportreq', methods=["POST"])
def api_report_request():
    return api_report_request_handler(request.json)


if __name__ == '__main__':
    app.run(port=5000)
