import config
from text import (invalid_format_warning, wrong_info, menu, greet, report_a_manual,
                  language_changed, report_b_manual, report_c_manual, click2copy, no_such_college)
from keys import TOKEN, REQUEST_KEYS
from reports import report_a_request, report_b_request
from apifunctions import generate_rep_id, get_chat_id, report_c_request, log_req
from helpingfunctions import change_language, language, log, report_log
import telebot


bot = telebot.TeleBot(TOKEN, threaded=False)


def start_handler(msg):
    chat_id = msg.chat.id
    lang = language(chat_id)
    bot.send_photo(chat_id, photo=open(greet[lang], 'rb'), caption=menu[lang], parse_mode="HTML")
    log(msg)


def menu_handler(msg):
    chat_id = msg.chat.id
    lang = language(chat_id)
    bot.send_message(chat_id, text=menu[lang], parse_mode="HTML")
    log(msg)


def change_language_handler(msg):
    chat_id = msg.chat.id
    bot.reply_to(msg, language_changed[change_language(chat_id)])
    log(msg)


def report_ab_handler(msg):
    log(msg)
    chat_id = msg.chat.id
    lang = language(chat_id)
    text = msg.text
    report = report_a_request(text, lang) if text.startswith('a') else report_b_request(text, lang)
    if report == -1:
        bot.reply_to(msg, text=invalid_format_warning[lang])
    elif report == -2:
        bot.reply_to(msg, text=wrong_info[lang])
    elif report == -3:
        bot.reply_to(msg, text=no_such_college[lang])
    else:
        bot.send_message(chat_id=chat_id, text=report, parse_mode="HTML")
        report_log(chat_id, report)


def report_c_handler(chat_id, lang):
    rep_id = generate_rep_id(chat_id)
    formatted_rep_id = f'{click2copy[lang]}\n`{rep_id}`'
    bot.send_message(chat_id=chat_id, text=formatted_rep_id, parse_mode='MarkdownV2')


def report_manual_handler(msg):
    chat_id = msg.chat.id
    lang = language(chat_id)
    if msg.text.endswith('c'):
        text = report_c_manual[lang]
        report_c_handler(chat_id, lang)
    else:
        text = report_a_manual[lang] if msg.text.endswith('a') else report_b_manual[lang]
    bot.send_message(chat_id=chat_id, text=text, parse_mode='HTML')


def api_report_request_handler(request_json):
    log_req(request_json)
    if request_json is None:
        return 400
    key = request_json.get('key')
    if key not in REQUEST_KEYS:
        return 'Your are not allowed to use this service', 403
    chat_id = get_chat_id(request_json.get('repid'))
    if chat_id is None:
        return 'rep_id invalid or expired', 400

    lang = language(chat_id)
    report = report_c_request(request_json, lang)
    if report == -1:
        unexpected_error(chat_id)
        return 'bad request', 400
    elif report == -2:
        bot.send_message(chat_id=chat_id, text=wrong_info[lang])
        report_c_handler(chat_id, lang)
        return 'wrong info', 400
    else:
        bot.send_message(chat_id=chat_id, text=report, parse_mode="HTML")
        report_log(chat_id, report)
    return 'report sent', 200


def about_handler(msg):
    chat_id = msg.chat.id
    lang = language(chat_id)
    bot.send_message(chat_id=chat_id, text=config.ABOUT[lang])
    log(msg)


def report_help_handler(msg):
    chat_id = msg.chat.id
    lang = language(chat_id)
    bot.send_photo(chat_id, photo=open(config.report_help_img[lang], 'rb'), caption=config.report_help[lang])
    log(msg)


def unexpected_error(chat_id):
    bot.send_message(chat_id=chat_id, text=config.error_message)
