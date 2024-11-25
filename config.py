admin_username = '@mio66mio'
admin_id = 0

english_users_json = 'english_users.json'

MAX_GPA = 4.00

AR = 0
EN = 1

UNIVERSITY = [' جامعة الأمير سلطان', ' Prince Sultan University']

NUMBER_OF_SEMESTERS = 8

COP_HOURS = 10

cs_plan = {1: 18, 2: 35, 3: 53, 4: 72, 5: 89, 6: 107, 7: 124, 8: 134}
ce_plan = {1: 18, 2: 36, 3: 54, 4: 73, 5: 92, 6: 111, 7: 128, 8: 138}
cl_plan = {1: 18, 2: 36, 3: 54, 4: 73, 5: 92, 6: 112, 7: 127, 8: 137}
ch_plan = {1: 17, 2: 33, 3: 50, 4: 67, 5: 85, 6: 104, 7: 123, 8: 133}
cb_plan = {1: 17, 2: 35, 3: 53, 4: 71, 5: 89, 6: 107, 7: 125, 8: 135}
cd_plan = {1: 19, 2: 37, 3: 55, 4: 73, 5: 92, 6: 111, 7: 128, 8: 138}

PLANS = {'cs': cs_plan, 'ce': ce_plan, 'cl': cl_plan, 'ch': ch_plan, 'cb': cb_plan, 'cd': cd_plan}

TOTAL_HOURS = {'cs': 134, 'ce': 138, 'cb': 135, 'cd': 138, 'cl': 137, 'ch': 133}

cs = ['كلية علوم الحاسب والمعلومات', 'College of Computer and Information Sciences']
cl = ['كلية القانون', 'College of Law']
ce = ['كلية الهندسة', 'College of Engineering']
cb = ['كلية إدارة الأعمال', 'College of Business Administration']
cd = ['كلية العمارة والتصميم', 'College of Architecture and Design']
ch = ['كلية الإنسانيات والعلوم', 'College of Humanities and Sciences']

colleges_dict = {
    'cs': cs,
    'cl': cl,
    'ce': ce,
    'cb': cb,
    'cd': cd,
    'ch': ch
}

colleges_acro = ['الكلية(القانون: cl، الهندسة: ce، إدارة الأعمال: cb، العمارة والتصميم: cd، كلية الإنسانيات والعلوم: ch)',
                 'College(Law: cl, Engineering: ce, Business: cb, Architecture and Design:cd, College of Humanities and Sciences: ch)']


HONORS = {1: 3.75, 2: 3.25, 3: 3.00}
DEANS_LIST_MIN = 3.75
DEFAULT_SEMESTER_HOURS = 18

report_a_command = 'a'
report_b_command = 'b'

arabic_form_link = 't.me/PSUgpa_bot/formar'
english_form_link = 't.me/PSUgpa_bot/formen'

logo = '''(\\  /)
(•ㅅ•)'''

signature = '@PSUgpa_bot\nby 𝖒𝖎𝖔~'

GITHUB_LINK = 'github.com/KamenYaiba/gigaChungus'

ABOUT = [
    f'مشروع My PSU GPA  ويعرف كذلك بـ gigaChungus هو مشروع مفتوح المصدر مصمم لمساعدة طلاب جامعة الأمير سلطان على حساب تقدمهم الأكاديمي والتخطيط لدراستهم بناء على الأرقام والحسابات\n\nالكود المصدري متوفر  على غيت هب: {GITHUB_LINK}\nالمساهمة مفتوحة ومقدرة (^-^)\n\n لمناقشة ما يخص المشروع أو لطلب المساعدة تواصل مع {admin_username}',
    f'The My PSU GPA project, also known as GigaChungus, is an open-source project designed to help Prince Sultan University students track their academic progress and plan their studies based on numbers and projections.\n\nThe source code is available on GitHub: {GITHUB_LINK}\nContributions are open and appreciated (^-^)\n\nTo discuss the project or if you need support please contact {admin_username}'
]

error_message = f'An unexpected error occurred\ncontact {admin_username} if you need help'

report_help = ['أكاديمي >> السجل الأكاديمي', 'Academic >> Academic Registration']

report_help_img = ['report_help_ar.png', 'report_help_en.png']

help_message = [f'تواصل مع {admin_username} إذا كنت تحتاج مساعدة^^ ', f'Contact {admin_username} if you need help^^']
