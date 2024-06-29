from config import(
    MAX_GPA, TOTAL_HOURS, report_a_command, report_b_command, NUMBER_OF_SEMESTERS)
import text, config
from helpingfunctions import (round_to_nearest_quarter, language,
                              get_lost_points, get_exact_gpa, get_gpa, in_deans_list, with_honors,
                              get_max_possible_gpa, get_avg_remaining_hours, get_remaining_hours,
                              get_remaining_semesters, get_rank_estimation, get_hours_percentage,
                              is_on_plan, get_max_boost, error_log, log, report_log, get_college)


def report_a_request(msg, lang):
    msg = msg.removeprefix(report_a_command).strip
    inputs = msg.split("\n")
    inputs = [i.strip() for i in inputs]
    try:
        points = abs(float(inputs[0]))
        registered_hours = abs(int(inputs[1]))
        passed_hours = abs(int(inputs[2]))
        semester = abs(int(inputs[3]))
        max_points = passed_hours * MAX_GPA
        mj = 'cs'
        if (points > max_points or passed_hours > TOTAL_HOURS[mj] or semester > NUMBER_OF_SEMESTERS
                or points < passed_hours or passed_hours > registered_hours):
            return -2
    except Exception as e:
        error_log(e)
        return -1
    return get_report(text.report_a, passed_hours, points, semester, lang, registered_hours=registered_hours, mj=mj)+ f'{config.signature}'


def report_b_request(msg, lang):
    msg = msg.removeprefix(report_b_command).strip()
    inputs = msg.split("\n")
    inputs = [i.strip() for i in inputs]
    try:
        points = abs(float(inputs[0]))
        registered_hours = abs(int(inputs[1]))
        passed_hours = abs(int(inputs[2]))
        semester = abs(int(inputs[3]))
        max_points = passed_hours * MAX_GPA
        mj = inputs[4]
        if (points > max_points or semester > NUMBER_OF_SEMESTERS or mj not in TOTAL_HOURS or passed_hours > TOTAL_HOURS[mj]
                or passed_hours > registered_hours or points < passed_hours):
            return -2
    except Exception as e:
        error_log(e)
        return -1
    return get_report(text.report_b, passed_hours, points, semester, lang, registered_hours, mj) + f'{config.signature}'


def get_report(report_type, passed_hours, points, semester, lang, registered_hours, mj):
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
    max_boost = get_max_boost(points, registered_hours, config.DEFAULT_SEMESTER_HOURS)

    return report_formatter(
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
        max_boost=max_boost
    )


def report_formatter(report_type, gpa, exact_gpa, max_gpa, college, passed_hours, failed_hours, remaining_hours, avg_hours,
                     remaining_semesters, on_plan, lost_points, honors, highest_honors, hours_percentage,
                     rank_estimation, lang, max_boost):
    report = f'''<pre>{config.logo}</pre>
<b>{report_type[lang]}\n\n
<b>{text.uni}</b>{config.UNIVERSITY}\n
<b><b>{text.college[lang]}</b>{college}\n

<b><b>{text.GPA[lang]}</b>{gpa}\n
<b><b>{text.exact_gpa[lang]}</b>{exact_gpa:.16f}\n
<b>{text.max_gpa[lang]}</b>{max_gpa}\n
<b>{text.points_lost[lang]}</b>{lost_points}\n

<b>{text.passed_hours[lang]}</b>{passed_hours}\n
<b>{text.failed_hours[lang]}</b>{failed_hours}\n
<b>{text.remaining_hours[lang]}</b>{remaining_hours}\n

<b>{text.hours_percentage[lang]}</b>{hours_percentage}\n
<b>{text.avg_hours[lang]}</b>{avg_hours}\n
<b>{text.remaining_semesters[lang]}</b>{remaining_semesters}\n
<b>{text.on_plan[lang]}</b>{on_plan}\n

<b>{text.honors[lang]}</b>{honors}\n
<b>{text.highest_honors[lang]}</b>{highest_honors}\n
<b>{text.rank_estimation[lang]}</b>{rank_estimation}\n
<b>{text.max_boost_def[lang]}</b>{max_boost}\n\n\n
'''
    return report

