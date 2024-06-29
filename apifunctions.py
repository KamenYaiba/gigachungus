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
        registered_hours = int(data.get('registered_hours'))
        passed_hours = int(data.get('passed_hours'))
        semester = int(data.get('semester'))
        mj = data.get('college')
        sem_gpa = float(data.get('sem_GPA'))
        next_sem_hours = int(data.get('next_sem_hours'))
        next_sem_lost_points = float(data.get('next_sem_lost_points'))

        if any(var is None for var in(points, registered_hours, passed_hours, semester, mj, sem_gpa, next_sem_hours, next_sem_lost_points)):
            return -1

        next_sem_max_points = next_sem_hours * MAX_GPA
        max_points = passed_hours * MAX_GPA
        if (points > max_points or semester > NUMBER_OF_SEMESTERS or passed_hours > TOTAL_HOURS[mj]
                or passed_hours > registered_hours or points < passed_hours or mj not in TOTAL_HOURS
                or sem_gpa < 0 or next_sem_hours < 0 or next_sem_lost_points > next_sem_max_points):
            return -2

    except Exception as e:
        error_log(e)
        return -1
    return get_report_extended(text.report_c, passed_hours, points, semester, lang, registered_hours, mj, sem_gpa, next_sem_hours, next_sem_lost_points)


def get_report_extended(report_type, passed_hours, points, semester, lang, registered_hours, mj,
                        sem_gpa, ns_hours, ns_lost_points):

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
    max_boost = get_max_boost(points, registered_hours, ns_hours)
    deans_list = in_deans_list(sem_gpa, lang)
    gpa_change = get_gpa_change(sem_gpa, gpa, lang)

    ns_points = ns_hours*MAX_GPA - ns_lost_points
    ns_tot_points = points + ns_points
    ns_tot_reg_hours = registered_hours + ns_hours
    ns_tot_pas_hours = passed_hours + ns_hours
    ns_exact_gpa = get_exact_gpa(ns_tot_points, ns_tot_reg_hours)
    ns_gpa = round(ns_exact_gpa, 2)
    ns_max_gpa = get_max_possible_gpa(lost_points + ns_lost_points, failed_hours, mj)
    ns_sem_gpa = round(get_exact_gpa(ns_tot_points-points, ns_hours), 2)
    ns_honors = with_honors(ns_gpa)
    ns_highest_honors = with_honors(ns_max_gpa)
    ns_remaining_hours = get_remaining_hours(passed_hours+ns_hours, mj)
    ns_remaining_semesters = remaining_semesters - 1
    ns_on_plan = is_on_plan(semester+1, passed_hours+ns_hours, lang, mj)
    ns_avg_hours = get_avg_remaining_hours(ns_remaining_semesters, remaining_hours-ns_hours)
    ns_hours_percentage = get_hours_percentage(ns_tot_reg_hours, mj)
    ns_deans_list = in_deans_list(ns_sem_gpa, lang)
    ns_gpa_change = get_gpa_change(ns_sem_gpa, ns_gpa, lang)

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

        ns_hours=ns_hours,
        ns_tot_pas_hours=ns_tot_pas_hours,
        ns_points=ns_points,
        ns_gpa=ns_gpa,
        ns_lost_points=ns_lost_points,
        ns_exact_gpa=ns_exact_gpa,
        ns_max_gpa= ns_max_gpa,
        ns_sem_gpa=ns_sem_gpa,
        ns_honors=ns_honors,
        ns_highest_honors=ns_highest_honors,
        ns_remaining_hours=ns_remaining_hours,
        ns_remaining_semesters=ns_remaining_semesters,
        ns_deans_list=ns_deans_list,
        ns_gpa_change=ns_gpa_change,
        ns_on_plan= ns_on_plan,
        ns_avg_hours=ns_avg_hours,
        ns_hours_percentage=ns_hours_percentage

    ) + config.signature


def report_formatter_extended(report_type, gpa, exact_gpa, max_gpa, college, passed_hours, failed_hours, remaining_hours,
                              avg_hours, remaining_semesters, on_plan, lost_points, honors, highest_honors,
                              hours_percentage,rank_estimation, lang, max_boost, deans_list, gpa_change, ns_hours,
                              ns_gpa, ns_exact_gpa, ns_sem_gpa, ns_max_gpa, ns_on_plan, ns_avg_hours, ns_hours_percentage,
                              ns_honors, ns_highest_honors, ns_remaining_hours, ns_remaining_semesters, ns_deans_list,
                              ns_gpa_change, ns_lost_points, ns_points, ns_tot_pas_hours):

    report = f'''<pre>{config.logo}</pre>
<b>{report_type[lang]}</b>\n\n
<b>{text.uni}</b>{config.UNIVERSITY}\n
<b>{text.college[lang]}</b>{college}\n

<b>{text.GPA[lang]}</b>{gpa}\n
<b>{text.exact_gpa[lang]}</b>{exact_gpa:.16f}\n
<b>{text.max_gpa[lang]}</b>{max_gpa}\n

<b>{text.sem_gpa[lang]}</b>{ns_gpa}\n
<b>{text.gpa_change[lang]}</b>{gpa_change}\n
<b>{text.points_lost[lang]}</b>{lost_points}\n

<b>{text.passed_hours[lang]}</b>{passed_hours}\n
<b>{text.failed_hours[lang]}</b>{failed_hours}\n
<b>{text.remaining_hours[lang]}</b>{remaining_hours}\n

<b>{text.hours_percentage[lang]}</b>{hours_percentage}\n
<b>{text.avg_hours[lang]}</b>{avg_hours}\n
<b>{text.remaining_semesters[lang]}</b>{remaining_semesters}\n
<b>{text.on_plan[lang]}</b>{on_plan}\n

<b>{text.deans_list[lang]}</b>{deans_list}\n
<b>{text.honors[lang]}</b>{honors}\n
<b>{text.highest_honors[lang]}</b>{highest_honors}\n
<b>{text.rank_estimation[lang]}</b>{rank_estimation}\n\n

<b>{text.after_next_semester(ns_hours, ns_lost_points)[lang]}</b>\n

<b>{text.sem_gpa [lang]}</b>{ns_sem_gpa}\n
<b>{text.gpa_change[lang]}</b>{ns_gpa_change}\n
<b>{text.GPA[lang]}</b>{ns_gpa}\n
<b>{text.exact_gpa[lang]}</b>{ns_exact_gpa:.16f}\n
<b>{text.max_gpa[lang]}</b>{ns_max_gpa}\n


<b>{text.points[lang]}</b>{ns_points}\n
<b>{text.passed_hours[lang]}</b>{ns_tot_pas_hours}\n
<b>{text.failed_hours[lang]}</b>{failed_hours}\n
<b>{text.remaining_hours[lang]}</b>{ns_remaining_hours}\n

<b>{text.hours_percentage[lang]}</b>{ns_hours_percentage}\n
<b>{text.avg_hours[lang]}</b>{ns_avg_hours}\n
<b>{text.remaining_semesters[lang]}</b>{ns_remaining_semesters}\n
<b>{text.on_plan[lang]}{ns_on_plan}</b>\n

<b>{text.max_boost[lang]}</b>{max_boost}\n
<b>{text.honors[lang]}{ns_honors}</b>\n
<b>{text.highest_honors[lang]}</b>{ns_highest_honors}\n
<b>{text.deans_list[lang]}</b>{ns_deans_list}\n\n


'''
    return report


