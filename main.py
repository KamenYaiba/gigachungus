from flask import Flask, request
import telebot
from config import report_a_command, report_b_command
from keys import WEBHOOK
from functions import error_log
from handlers import (bot, start_handler, change_language_handler, report_ab_handler, report_c_handler,
                      report_manual_handler, api_report_request_handler)


app = Flask(__name__)


@app.route('/'+WEBHOOK, methods=["POST"])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@bot.message_handler(commands=['start', 'help', 'menu'])
def start_command(msg):
    try:
        start_handler(msg)
    except Exception as e:
        error_log(e)


@bot.message_handler(commands=['ar', 'en'])
def change_lang_to_ar(msg):
    try:
        change_language_handler(msg)
    except Exception as e:
        error_log(e)


@bot.message_handler(regexp='^' + report_a_command+'|'+report_b_command)
def report_a(msg):
    try:
        report_ab_handler(msg)
    except Exception as e:
        bot.reply_to(msg, "An Error occurred")
        error_log(e)


@bot.message_handler(commands=["reportc"])
def report_c(msg):
    try:
        report_c_handler(msg)
    except Exception as e:
        error_log(e)


@bot.message_handler(commands=["reporta", "reportb", "reportc"])
def report_manual(msg):
    try:
        report_manual_handler(msg)
    except Exception as e:
        error_log(e)


@app.route('/reportreq', methods=["POST"])
def api_report_request():
    try:
        api_report_request_handler(request.json)
    except Exception as e:
        error_log(e)


if __name__ == '__main__':
    app.run(port=5000)
