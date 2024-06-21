import telebot
from config import(report_a_command, report_b_command, invalid_format_warning,wrong_info,
                   menu, greet, report_a_manual)
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