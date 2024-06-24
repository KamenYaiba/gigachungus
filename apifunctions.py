import json
import string
import random
import text
from text import(AR, EN, hrs, advanced_by, late_by)
from config import (MAX_GPA, TOTAL_HOURS, report_a_command, report_b_command, arabic_users_json,
                    NUMBER_OF_SEMESTERS, COP_HOURS, HONORS, DEANS_LIST_MIN)
from helpingfunctions import (round_to_nearest_quarter, add_to_arabic_users, remove_from_arabic_users, language,
                              get_lost_points, get_exact_gpa, get_gpa, in_deans_list, with_honors,
                              get_max_possible_gpa, get_avg_remaining_hours, get_remaining_hours,
                              get_remaining_semesters, get_rank_estimation, get_hours_percentage,
                              is_on_plan, get_max_boost, error_log, log, report_log, get_lost_points_wgpa)
from reports import get_report, in_deans_list
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
        registered_hours = data.get('registered_hours')
        passed_hours = int(data.get('passed_hours'))
        semester = int(data.get('semester'))
        max_points = passed_hours * MAX_GPA
        mj = data.get('college')
        sem_GPA = float(data.get('sem_GPA'))
        next_sem_hours = int(data.get('next_sem_hours'))

        if any(var is None for var in(points, registered_hours, passed_hours, semester, mj, sem_GPA, next_sem_hours)):
            return -1
        if (points > max_points or semester > NUMBER_OF_SEMESTERS or passed_hours > TOTAL_HOURS[mj]
                or passed_hours > registered_hours or points < passed_hours or mj not in TOTAL_HOURS
                or sem_GPA<0 or next_sem_hours<0):
            return -2
    except Exception as e:
        print(e)
        return -1
    return get_report_extended(text.report_c, passed_hours, points, semester, lang, registered_hours=passed_hours, mj=mj)


def get_report_extended(type, passed_hours, points, semester, lang, registered_hours, mj, sem_GPA, next_semester_hours):
    failed_hours = registered_hours - passed_hours
    exact_gpa = get_exact_gpa(points, registered_hours)
    gpa = round(exact_gpa, 2)
    lost_points = get_lost_points(points, registered_hours)
    max_gpa = get_max_possible_gpa(lost_points, failed_hours, mj)
    honors = with_honors(gpa)
    highest_honors = with_honors(max_gpa)
    hours_percentage = get_hours_percentage(passed_hours, mj)
    rank_estimation = get_rank_estimation(gpa)
    on_plan = is_on_plan(semester, passed_hours, lang)
    remaining_hours = get_remaining_hours(passed_hours, mj)
    remaining_semesters = get_remaining_semesters(semester)
    avg_hours = get_avg_remaining_hours(remaining_semesters, remaining_hours)
    deans_list = in_deans_list(sem_GPA, lang)


