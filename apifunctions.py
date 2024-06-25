import json, string, random, text, config
import pytz
from _datetime import datetime
from config import (MAX_GPA, TOTAL_HOURS, report_a_command, report_b_command, arabic_users_json,
                    NUMBER_OF_SEMESTERS, COP_HOURS, HONORS, DEANS_LIST_MIN)
from helpingfunctions import (round_to_nearest_quarter, language, get_lost_points, get_exact_gpa, get_gpa,
                              in_deans_list, with_honors, get_max_possible_gpa, get_avg_remaining_hours,
                              get_remaining_hours, get_remaining_semesters, get_rank_estimation, get_hours_percentage,
                              is_on_plan, get_max_boost, error_log, log, report_log, get_college, get_gpa_change)


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
        sem_gpa = float(data.get('sem_GPA'))
        next_sem_hours = int(data.get('next_sem_hours'))

        if any(var is None for var in(points, registered_hours, passed_hours, semester, mj, sem_gpa, next_sem_hours)):
            return -1
        if (points > max_points or semester > NUMBER_OF_SEMESTERS or passed_hours > TOTAL_HOURS[mj]
                or passed_hours > registered_hours or points < passed_hours or mj not in TOTAL_HOURS
                or sem_gpa<0 or next_sem_hours<0):
            return -2
    except Exception as e:
        print(e)
        return -1
    return get_report_extended(text.report_c, passed_hours, points, semester, lang, registered_hours=passed_hours, mj=mj)


def get_report_extended(report_type, passed_hours, points, semester, lang, registered_hours, mj, sem_gpa, next_semester_hours):
    failed_hours = registered_hours - passed_hours
    exact_gpa = get_exact_gpa(points, registered_hours)
    gpa = round(exact_gpa, 2)
    lost_points = get_lost_points(points, registered_hours)
    college = get_college(mj, lang)
    max_gpa = get_max_possible_gpa(lost_points, failed_hours, mj)
    honors = with_honors(gpa)
    highest_honors = with_honors(max_gpa)
    hours_percentage = get_hours_percentage(passed_hours, mj)
    rank_estimation = get_rank_estimation(gpa)
    on_plan = is_on_plan(semester, passed_hours, lang, mj)
    remaining_hours = get_remaining_hours(passed_hours, mj)
    remaining_semesters = get_remaining_semesters(semester)
    avg_hours = get_avg_remaining_hours(remaining_semesters, remaining_hours)
    max_boost = get_max_boost(points, registered_hours, next_semester_hours)
    deans_list = in_deans_list(sem_gpa, lang)
    gpa_change = get_gpa_change(sem_gpa, gpa, lang)

    next_sem_on_plan = is_on_plan(semester, passed_hours+next_semester_hours, lang, mj)
    next_sem_avg_hours = get_avg_remaining_hours(remaining_semesters-1, remaining_hours-next_semester_hours)
    next_sem_hours_percentage = get_hours_percentage(passed_hours+next_semester_hours, mj)

    return report_formatter_extended(
        report_type=report_type,
        college=college,
        exact_gpa=exact_gpa,
        gpa=gpa,
        max_gpa=max_gpa,
        honors=honors,
        highest_honors=highest_honors,
        hours_percentage=hours_percentage,
        rank_estimation=rank_estimation,
        on_plan=on_plan,
        remaining_hours=remaining_hours,
        remaining_semesters=remaining_semesters,
        avg_hours=avg_hours,
        lang=lang,
        failed_hours=failed_hours,
        passed_hours=passed_hours,
        lost_points=lost_points,
        max_boost=max_boost,
        deans_list=deans_list,
        gpa_change=gpa_change,
        next_sem_on_plan= next_sem_on_plan,
        next_sem_avg_hours=next_sem_avg_hours,
        next_sem_hours_percentage=next_sem_hours_percentage
    ) + config.signature


def report_formatter_extended(report_type, gpa, exact_gpa, max_gpa, college, passed_hours, failed_hours, remaining_hours,
                              avg_hours, remaining_semesters, on_plan, lost_points, honors, highest_honors,
                              hours_percentage,rank_estimation, lang, max_boost, deans_list, gpa_change,
                              next_sem_on_plan, next_sem_avg_hours, next_sem_hours_percentage):

    report = f'''{config.logo}
{report_type[lang]}\n\n
{text.college[lang]}{college}\n
{text.GPA[lang]}{gpa}\n
{text.exact_gpa[lang]}{exact_gpa:.16f}\n
{text.max_gpa[lang]}{max_gpa}\n
{text.points_lost[lang]}{lost_points}\n

{text.passed_hours[lang]}{passed_hours}\n
{text.failed_hours[lang]}{failed_hours}\n
{text.remaining_hours[lang]}{remaining_hours}\n

{text.hours_percentage[lang]}{hours_percentage}\n
{text.avg_hours[lang]}{avg_hours}\n
{text.remaining_semesters[lang]}{remaining_semesters}\n
{text.on_plan[lang]}{on_plan}\n

{text.honors[lang]}{honors}\n
{text.highest_honors[lang]}{highest_honors}\n
{text.rank_estimation[lang]}{rank_estimation}\n
{text.max_boost_def[lang]}{max_boost}\n\n\n
'''
    return report


