import json
import string
import random
import config
from config import(
    MAX_GPA, TOTAL_HOURS, report_a_command, report_b_command, AR, EN,
    arabic_users_json, NUMBER_OF_SEMESTERS, COP_HOURS, HONORS, DEANS_LIST_MIN,
    hrs, advanced_by, late_by)
from functions import get_report
import pytz
from _datetime import datetime


def generate_rep_id(chat_id):
    with open('rep_ids.json', 'r') as file:
        ids = json.load(file)
    destroy_rep_id(ids, chat_id)
    rep_id = random_string()
    ids[rep_id] = chat_id
    with open('rep_ids.json', 'w') as file:
        json.dump(ids, file)
    return rep_id


def log_req(req):
    dt = datetime.now(pytz.timezone('Asia/Riyadh'))
    with open('api_req_logs.txt', 'a') as file:
        file.write(dt.strftime("%A %d %B %Y %H:%M") + '\t' + str(req) +'\n\n')


def get_chat_id(rep_id):
    with open('rep_ids.json', 'r') as file:
        ids = json.load(file)
    if rep_id not in ids:
        return None
    chat_id = ids.pop(rep_id)
    with open('rep_ids.json', 'w') as file:
        json.dump(ids, file)
    return chat_id


def destroy_rep_id(ids, chat_id):
    if chat_id in ids.values():
        for key in ids.keys():
            if ids[key] == chat_id:
                del ids[key]
                return True
    return False


def random_string():
    chars = string.ascii_letters + string.digits
    ranstr = ""
    for i in range(8):
        ranstr = ranstr + random.choice(chars)
    return ranstr


def report_c_request(data, lang):
    try:
        points = float(data.get('points'))
        passed_hours = int(data.get('passed_hours'))
        semester = int(data.get('semester'))
        max_points = passed_hours * MAX_GPA
        mj = 'cs'
        if any(var is None for var in(points, passed_hours, semester, max_points, mj)):
            return -1
        if (points > max_points or passed_hours > TOTAL_HOURS[mj] or
                semester > NUMBER_OF_SEMESTERS or points < passed_hours or mj not in TOTAL_HOURS):
            return -2
    except Exception as e:
        print(e)
        return -1
    return get_report(config.report_a, passed_hours, points, semester, lang, registered_hours=passed_hours, mj=mj)



