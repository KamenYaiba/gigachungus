import config
import json
from config import(
    MAX_GPA, TOTAL_HOURS, report_a_command, report_b_command, AR, EN,
    arabic_users_json, NUMBER_OF_SEMESTERS, COP_HOURS, HONORS, DEANS_LIST_MIN,
    hrs, advanced_by, late_by)
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


def in_deans_list(gpa):
    if gpa >= DEANS_LIST_MIN:
        return 'Yes! 🎉'
    return 'No'


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
    return '-'


def get_hours_percentage(hours, mj):
    return str(round(((hours / TOTAL_HOURS[mj])*100), 1)) + '%'


def is_on_plan(semester, hours, lang):
    if semester == 0:
        return '-'
    delta = hours - config.PLAN[semester]
    if delta == 0:
        return 'On Plan'
    if delta > 0:
        return f'{advanced_by[lang]} {delta} {hrs[lang]}'
    if delta < 0:
        return f'{late_by[lang]} {abs(delta)} {hrs[lang]}'


def report_a_request(msg, lang):
    msg = msg.strip(report_a_command).strip()
    inputs = msg.split("\n")
    inputs = [i.strip() for i in inputs]
    try:
        points = abs(float(inputs[0]))
        passed_hours = abs(int(inputs[1]))
        semester = abs(int(inputs[2]))
        max_points = passed_hours * MAX_GPA
        mj = 'cs'
        if (points > max_points or passed_hours > TOTAL_HOURS[mj] or semester > NUMBER_OF_SEMESTERS
                or points < passed_hours):
            return -2
    except Exception as e:
        print(e)
        return -1
    return get_report(config.report_a, passed_hours, points, semester, lang, registered_hours=passed_hours, mj=mj)+ f'{config.signature}'


def report_b_request(msg, lang):
    msg = msg.strip(report_b_command).strip()
    inputs = msg.split("\n")
    inputs = [i.strip() for i in inputs]
    try:
        points = abs(float(inputs[0]))
        passed_hours = abs(int(inputs[1]))
        registered_hours = abs(int(inputs[2]))
        semester = abs(int(inputs[3]))
        max_points = passed_hours * MAX_GPA
        mj = inputs[4]
        if (points > max_points or semester > NUMBER_OF_SEMESTERS or passed_hours > TOTAL_HOURS[mj]
                or passed_hours > registered_hours or points < passed_hours or mj not in TOTAL_HOURS):
            return -2
    except Exception as e:
        print(e)
        return -1
    return get_report(config.report_b, passed_hours, points, semester, lang, registered_hours, mj)+ f'{config.signature}'


def get_report(type, passed_hours, points, semester, lang, registered_hours, mj):
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

    return report_formatter(
        type=type,
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
        lost_points=lost_points
    )


def report_formatter(type, gpa, exact_gpa, max_gpa, passed_hours, failed_hours, remaining_hours, avg_hours, remaining_semesters, on_plan, lost_points, honors, highest_honors, hours_percentage, rank_estimation, lang):
    report = f'''{config.logo}
{type[lang]}\n\n
{config.GPA[lang]}{gpa}\n
{config.exact_gpa[lang]}{exact_gpa}\n
{config.max_gpa[lang]}{max_gpa}\n
{config.points_lost[lang]}{lost_points}\n

{config.passed_hours[lang]}{passed_hours}\n
{config.failed_hours[lang]}{failed_hours}\n
{config.remaining_hours[lang]}{remaining_hours}\n

{config.hours_percentage[lang]}{hours_percentage}\n
{config.avg_hours[lang]}{avg_hours}\n
{config.remaining_semesters[lang]}{remaining_semesters}\n
{config.on_plan[lang]}{on_plan}\n

{config.honors[lang]}{honors}\n
{config.highest_honors[lang]}{highest_honors}\n
{config.rank_estimation[lang]}{rank_estimation}\n\n\n
'''
    return report


def error_log(e):
    dt = datetime.now(pytz.timezone('Asia/Riyadh'))
    with open('errorsLog.txt', 'a') as file:
        file.write(dt.strftime("%A %d %B %Y %H:%M") + '\n'+''.join(traceback.format_exception(None, e, e.__traceback__))+ '\n\n\n')


def log(msg):
    dt = datetime.now(pytz.timezone('Asia/Riyadh'))
    id = msg.chat.id
    usr = msg.from_user.username
    if usr is None:
        usr = '-'
    name = msg.chat.first_name
    if name is None:
        name = '-'
    with open('logs.txt', 'a') as file:
        file.write(dt.strftime("%A %d %B %Y %H:%M") + '\t' + str(id) + '\t' + str(usr) + '\t' + str(name) + '\t' + msg.text + '\n\n')


def report_log(id, report):
    dt = datetime.now(pytz.timezone('Asia/Riyadh'))
    sep = '\n-------------------------------------------------'
    with open('reportsLog.txt', 'a') as file:
        file.write(dt.strftime("%A %d %B %Y %H:%M") + '\t\t' + str(id) + '\n' + report + sep +'\n\n\n')


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

