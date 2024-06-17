from flask import Flask, request
import telebot
from telebot import types
from config import(report_a_command, report_b_command, invalid_format_warning,wrong_info)
from keys import TOKEN, WEBHOOK, REQUEST_KEYS
from functions import(report_a_request, report_b_request, language, error_log, log, report_log,
                       add_to_arabic_users, remove_from_arabic_users)
from apifunctions import generate_rep_id, get_chat_id, report_c_request, log_req


bot = telebot.TeleBot(TOKEN, threaded=False)

app = Flask(__name__)


@app.route('/'+WEBHOOK, methods=["POST"])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@bot.message_handler(commands=['start', 'help'])
def start_command(msg):
    bot.send_message(msg.chat.id, f'Hey n *{msg.chat.first_name}*!', parse_mode='Markdown', reply_markup=types.ReplyKeyboardRemove())
    log(msg)


@bot.message_handler(commands=['ar'])
def change_lang_to_ar(msg):
    id = msg.chat.id
    add_to_arabic_users(id)
    bot.reply_to(msg, "لقد غيرت اللغة إلى العربية")
    log(msg)


@bot.message_handler(commands=['en'])
def change_lang_to_en(msg):
    id = msg.chat.id
    remove_from_arabic_users(id)
    bot.reply_to(msg, "Language changed to English")
    log(msg)


@bot.message_handler(regexp='^' + report_a_command)
def report_a(msg):
    try:
        log(msg)
        id = msg.chat.id
        lang = language(id)
        report = report_a_request(msg.text, lang)
        if report == -1:
            bot.reply_to(msg, text=invalid_format_warning[lang])
        elif report == -2:
            bot.reply_to(msg, text=wrong_info[lang])
        else:
            bot.send_message(chat_id=id, text=report)
            report_log(id, report)
    except Exception as e:
        bot.reply_to(msg, "An Error occurred")
        error_log(e)


@bot.message_handler(regexp='^' + report_b_command)
def report_b(msg):
    try:
        log(msg)
        id = msg.chat.id
        lang = language(id)
        report = report_b_request(msg.text, lang)
        if report == -1:
            bot.reply_to(msg, text=invalid_format_warning[lang])
        elif report == -2:
            bot.reply_to(msg, text=wrong_info[lang])
        else:
            bot.send_message(chat_id=id, text=report)
            report_log(id, report)
    except Exception as e:
        bot.reply_to(msg, "An Error occurred")
        error_log(e)


@bot.message_handler(commands=["reportc"])
def report_c(msg):
    chat_id = msg.chat.id
    rep_id = generate_rep_id(chat_id)
    bot.send_message(chat_id=chat_id, text=rep_id)


@app.route('/reportreq', methods=["POST"])
def repreq():
    data = request.json
    log_req(data)
    if data is None:
        return 400
    key = data.get('key')
    if key not in REQUEST_KEYS:
        return 'Your are not allowed to use this service', 403
    chat_id = get_chat_id(data.get('repid'))
    if chat_id is None:
        return 'rep_id invalid or expired', 400

    lang = language(chat_id)
    report = report_c_request(data, lang)
    if report == -1:
        bot.send_message(chat_id=chat_id, text='An unexpected error occurred')
        return 'bad request', 400
    elif report == -2:
        bot.send_message(chat_id=chat_id, text=wrong_info[lang])
        return 'wrong info', 400
    else:
        bot.send_message(chat_id=chat_id, text=report)
    return 'report sent', 200


if __name__ == '__main__':
    app.run(port=5000)
