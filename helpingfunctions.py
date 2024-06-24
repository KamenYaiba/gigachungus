import json
from config import(
    MAX_GPA, TOTAL_HOURS, report_a_command, report_b_command,
    arabic_users_json, NUMBER_OF_SEMESTERS, COP_HOURS, HONORS, DEANS_LIST_MIN, PLAN)
import text
from text import(hrs, advanced_by, late_by, no, yes, college, AR, EN,)
from _datetime import datetime
import pytz
import traceback


def round_to_nearest_quarter(num):
    return round(num * 4) / 4


def add_to_arabic_users(id):
    with open(arabic_users_json, 'r') as file:
        arabic_ids = json.load(file)
    if id not in arabic_ids:
        arabic_ids.append(id)
        with open(arabic_users_json, 'w') as file:
            json.dump(arabic_ids, file)
        return True
    return False


def remove_from_arabic_users(id):
    with open(arabic_users_json, 'r') as file:
        arabic_ids = json.load(file)
    if id in arabic_ids:
        arabic_ids.remove(id)
        with open(arabic_users_json, 'w') as file:
            json.dump(arabic_ids, file)
        return True
    return False


def language(id):
    with open(arabic_users_json, 'r') as file:
        arabic_ids = json.load(file)
    result = AR if id in arabic_ids else EN
    return result


def get_lost_points(points, hours):
    return (hours * MAX_GPA) - points


def get_exact_gpa(points, hours):
    return points / hours


def get_gpa(points, hours):
    return round(points / hours)


def in_deans_list(gpa, lang):
    if gpa >= DEANS_LIST_MIN:
        return yes[lang]
    return no[lang]


def with_honors(gpa):
    if gpa >= HONORS[1]:
        return '🥇 1st'
    elif gpa >= HONORS[2]:
        return '🥈 2nd'
    elif gpa >= HONORS[3]:
        return '🥉 3rd'
    return '-'


def get_max_possible_gpa(lost_points, failed_hours, mj):
    return round(MAX_GPA - (lost_points / (TOTAL_HOURS[mj]+failed_hours)), 2)


def get_avg_remaining_hours(remaining_semesters, remaining_hours):
    if remaining_hours <= COP_HOURS or remaining_semesters <= 1: return 0
    return round((remaining_hours - COP_HOURS) / (remaining_semesters - 1), 1)


def get_remaining_hours(hours, mj):
    return TOTAL_HOURS[mj] - hours


def get_remaining_semesters(semester):
    return NUMBER_OF_SEMESTERS - semester


def get_rank_estimation(gpa):
    if gpa >= 3.98: return 'Top 5'
    if gpa >= 3.90: return 'Top 10'
    if gpa >= 3.85: return 'Top 20'
    if gpa >= 3.75: return 'Top 50'
    if gpa >= 3.5: return 'Top 100'
    if gpa >= 3.0: return 'Top 200'
    if gpa >= 2.75: return 'Top 500'
    return '-'


def get_hours_percentage(hours, mj):
    return str(round(((hours / TOTAL_HOURS[mj])*100), 1)) + '%'


def is_on_plan(semester, hours, lang):
    if semester == 0:
        return '-'
    delta = hours - PLAN[semester]
    if delta == 0:
        return 'On Plan'
    if delta > 0:
        return f'{advanced_by[lang]} {delta} {hrs[lang]}'
    if delta < 0:
        return f'{late_by[lang]} {abs(delta)} {hrs[lang]}'


def get_max_boost(points, registered_hours, next_sem_hours):
    tot_points = points + next_sem_hours * MAX_GPA
    tot_hours = registered_hours + next_sem_hours
    return round(get_exact_gpa(tot_points, tot_hours), 2)


def error_log(e):
    dt = datetime.now(pytz.timezone('Asia/Riyadh'))
    with open('errorsLog.txt', 'a') as file:
        file.write(dt.strftime("%A %d %B %Y %H:%M") + '\n'+''.join(traceback.format_exception(None, e, e.__traceback__))+ '\n\n\n')


def log(msg):
    dt = datetime.now(pytz.timezone('Asia/Riyadh'))
    chat_id = msg.chat.id
    usr = msg.from_user.username
    if usr is None:
        usr = '-'
    name = msg.chat.first_name
    if name is None:
        name = '-'
    with open('logs.txt', 'a') as file:
        file.write(dt.strftime("%A %d %B %Y %H:%M") + '\t' + str(chat_id) + '\t' + str(usr) + '\t' + str(name) + '\t' + msg.text + '\n\n')


def report_log(id, report):
    dt = datetime.now(pytz.timezone('Asia/Riyadh'))
    sep = '\n-------------------------------------------------'
    with open('reportsLog.txt', 'a') as file:
        file.write(dt.strftime("%A %d %B %Y %H:%M") + '\t\t' + str(id) + '\n' + report + sep +'\n\n\n')


#currently not in use
#this function calculates the lost points using only GPA and registered hours
#since most universities round GPAs, multiple lost point scenarios are possible
#the function returns a list of possible lost points that result in the given GPA after rounding
def get_lost_points_wgpa(gpa, hours):
    gpa = abs(gpa)
    hours = abs(hours)
    max_points = hours * MAX_GPA
    lost_points = max_points - gpa * hours
    lost_points = round_to_nearest_quarter(lost_points)

    results = []
    for delta in [0, 0.25, 0.5, -0.25, -0.5]:
        hypo_lost_point = lost_points + delta
        if 0 <= hypo_lost_point <= max_points:
            calculated_gpa = round(MAX_GPA - (hypo_lost_point/hours), 2)
            if calculated_gpa == gpa:
                results.append(hypo_lost_point)
    if bool(results):
        return results
