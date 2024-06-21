import telebot
from config import(report_a_command, report_b_command, invalid_format_warning,wrong_info,
                   menu, greet, report_a_manual, language_changed)
from keys import TOKEN, REQUEST_KEYS
from functions import(report_a_request, report_b_request, language, error_log, log, report_log,
                       add_to_arabic_users, remove_from_arabic_users)
from apifunctions import generate_rep_id, get_chat_id, report_c_request, log_req


bot = telebot.TeleBot(TOKEN, threaded=False)


def start_handler(msg):
    id = msg.chat.id
    lang = language(id)
    bot.send_photo(id, photo=open(greet[lang], 'rb'), caption=menu[lang])
    log(msg)


def change_language_handler(msg):
    lang = 0 if msg.text.strip('/') == 'ar' else 1
    id = msg.chat.id
    if lang == 0:
        add_to_arabic_users(id)
    else:
        remove_from_arabic_users(id)
    bot.reply_to(msg, language_changed[lang])


