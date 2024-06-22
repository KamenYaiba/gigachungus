arabic_users_json = 'arabic_users.json'

MAX_GPA = 4.00
TOTAL_HOURS = {'cs': 134, 'ce': 138, 'cba': 135, 'cad': 138, 'cl': 137}
NUMBER_OF_SEMESTERS = 8
COP_HOURS = 10
PLAN = {1: 18, 2: 35, 3: 53, 4: 72, 5: 89, 6: 107, 7: 124, 8: 134}
HONORS = {1: 3.50, 2: 3.25, 3: 3.00}
DEANS_LIST_MIN = 3.75

report_a_command = 'a'
report_b_command = 'b'

AR = 0
EN = 1
logo = '''(\\  /)
(•ㅅ•)'''
signature = '@PSUgpa_bot\nby 𝖒𝖎𝖔~'

arabic_form_link = 'https://docs.google.com/forms/d/e/1FAIpQLSeEd8LNfdi6TKc9Mh4vzKrURpKacafCkIjH6--9jrdyMS5AWg/viewform?usp=sf_link'
arabic_form = f'<a href="{arabic_form_link}">الإسنمارة</a>'
english_form = 'https://docs.google.com/forms/d/e/1FAIpQLSeEd8LNfdi6TKc9Mh4vzKrURpKacafCkIjH6--9jrdyMS5AWg/viewform?usp=sf_link'

arabic_menu = '''/en To change the language to English


/reporta تقرير من نوع أ
-الأسرع
-خاص بطلاب كلية الحاسب\n

/reportb تقرير من نوع ب
- الأكثر شعبية
- يجب عليك تحديد كليتك\n

/reportc تقرير من نوع ج
-الأكثر تفصيلا
-سيتوجب عليك ملء استمارة 'Google Forms'\n
'''

english_menu = '''/ar لتغيير اللغة إلى العربية


/reporta Report type A
-Fastest
-For CCIS students only\n

/reportb Report type B
-Most popular
-Must specify your college\n

/reportc Report Type C
-Most detailed
-Must submit a Google Form
'''
menu = [arabic_menu, english_menu]
a_ar = '''أرسل رسالة بالصيغة التالية:

نوع التقرير(a)
عدد النقاط التي حصلت عليها
الساعات المسجلة
الساعات المجتازة
عدد الفصول التي أكملتها(لا تحسب التحضيري والفصول الصيفية)
------------------------------------------

مثال:
_____
a
117.75
36
33
2
¯¯¯¯¯

/reporthelp  إذا كنت لا تعرف نقاطك أو ساعاتك المسجلة أو المجتازة
'''
a_en = '''send a message in the following format:

Report Type(a)
Points you gained
Registered hours
Passed Hours
Number of semesters you've passed(PYP and summer semesters don't count)
------------------------------------------

Example:
_____
a
117.75
36
33
2
¯¯¯¯¯

/reporthelp  if you don't know your points, registered hours, or passed hours
'''
report_a_manual = [a_ar, a_en]

b_ar = '''أرسل رسالة بالصيغة التالية:

نوع التقرير(b)
عدد النقاط التي حصلت عليها
الساعات المسجلة
الساعات المجتازة
عدد الفصول التي أكملتها(لا تحسب التحضيري والفصول الصيفية)
الكلية(القانون:cl، الهندسة:ce، إدارة الأعمال:cba، العمارة والتصميم:cad )
------------------------------------------

مثال:
_____
b
117.75
36
33
2
ce
¯¯¯¯¯

/reporthelp  إذا كنت لا تعرف نقاطك أو ساعاتك المسجلة أو المجتازة
'''
b_en = '''send a message in the following format:

Report Type(a)
Points you gained
Registered hours
Passed Hours
Number of semesters you've passed(PYP and summer semesters don't count)
College(Law:cl, Engineering:ce, Business:cba, Architecture and Design:cad')
------------------------------------------

Example:
_____
b
117.75
36
33
2
ce
¯¯¯¯¯

/reporthelp  if you don't know your points, registered hours, or passed hours
'''
report_b_manual = [b_ar, b_en]

c_ar = 'انسخ رقم الطلب واملأ' + arabic_form
c_en = 'fill the form'
report_c_manual = [c_ar, c_en]

report_help = ['سجل الدخول في بوابة النظام الأكاديمي"Edugate"\nأكاديمي>السجل الأكاديمي',
               'Log in to your Edugate account\nAcademic > Academic Transcript']
report_help_photo = ['arabic_report_help.png', 'english_report_help.png']

greet = ['arabic_greeting.png', 'english_greeting.png']
report_a = ['تقرير من نوع أ\n----------------', 'Report Type A\n----------------']
report_b = ['تقرير من نوع ب\n----------------', 'Report Type B\n----------------']
report_c = ['تقرير من نوع ج\n----------------', 'Report Type C\n----------------']
GPA = ['المعدل: ', 'GPA: ']
passed_hours = ['الساعات المجتازة: ', 'Hours Passed: ']
max_gpa = ['أعلى معدل يمكن التخرج به: ', 'Max possible graduation GPA: ']
exact_gpa = ['المعدل بالضبط: ', 'Exact GPA: ']
honors = ['مرتبة الشرف: ', 'Honors: ']
highest_honors = ['أعلى مرتبة شرف يمكن تحقيقها: ', 'Highest possible honors: ']
points_lost = ['النقاط التي خُسرت: ', 'Points lost: ']
on_plan = ['على الخطة؟: ', 'On Plan?: ']
deans_list = ['قائمة العميد؟: ', "Dean's list?: "]
avg_hours = ['متوسط الساعات المتبقية في الفصل الواحد(باستثناء الفصل الأخير): ',
             'Average remaining hours per semester(excluding the last cop semester): ']
rank_estimation = ['الترتيب التقريبي(على كليتك): ', 'Rough rank estimation(in your college): ']
hours_percentage = ['نسبة الساعات المجتازة: ', 'Credit Hours Completed Percentage: ']
remaining_hours = ['الساعات المتبقية: ', 'Hours Remaining: ']
remaining_semesters = ['الفصول المتبقية: ', 'Remaining Semesters: ']
max_gpa_next_semester = [
    'أعلى معدل تراكمي ممكن بعد الفصل القادم(بافتراض أنك ستسجل 18 ساعة وتحصل على A+ في جميع المواد): ',
    'The highest possible cumulative GPA after the next semester (assuming you register for 18 hours and get an A+ in all courses): ']
failed_hours = ['ساعات الرسوب: ', 'Failed Hours: ']
advanced_by = ['متقدم بـ ', 'Advanced by ']
late_by = ['متأخر بـ ', 'Late by ']
hrs = ['ساعة / ساعات ', 'Hour / Hours']
semester_gpa = ['المعدل الفصلي: ', 'Semester GPA: ']
semester_lost_points = ['الساعات التي خسرتها هذا الفصل: ', 'Semester lost points: ']
exact_semester_gpa = ['المعدل الفصلي بالضبط: ', 'Exact semester GPA: ']
semester_failed_hours = ['ساعات الرسوب هذا الفصل: ', 'Semester failed hours: ']
points = ['النقاط التي حصلت عليها: ', 'Points gained: ']
semester_points = ['النقاط التي حصلت عليها هذا الفصل: ', 'Points gained this semester: ']
max_boost_def = ['أقصى زيادة ممكنة للمعدل التراكمي(بافتراض أنك ستسجل 18 ساعة وتحصل علىA + في جميع المواد): ',
                 'Max possible GPA boost (assuming you register for 18 hours and get A+ in all courses next semester): ']
max_boost = ['أقصى زيادة ممكنة للمعدل التراكمي بعد الفصل القادم: ',
             'Max possible GPA boost by the end of next semester: ']
college = ['الكلية: ', 'College: ']

invalid_format_warning = ['خطأ في تنسيق الطلب! يرجى اتباع التنسيق المقدم لكم',
                          'Invalid format! please follow the format provided previously']
wrong_info = ['البيانات التي قدمتها لا تبدو صحيحة! يرجى مراجعتها',
              "The data you provided doesn't seem to make sense! try again please"]
no_such_college = ['لم نعثر على كليتك\ncl:القانون\nce: الهندسة\ncba: إدارة الأعمال\ncad: العمارة والتصميم',
                   'No such college.\ncl: Law\nce: Engineering\ncba: Business\ncad: Architecture and Design']
language_changed = ["لقد غيرت اللغة إلى العربية", "Language changed to English"]

lil_bunny = '''(\\__/) 
(•ㅅ•) 
 /  　 づ'''

giga_bunny = '''.      (\\__/)
       (•ㅅ•) 
    ＿ノヽ ノ＼＿      
/　/ ⌒Ｙ⌒ Ｙ  ヽ    
( 　(三ヽ人　 /　  |
|　ﾉ⌒＼ ￣￣ヽ   ノ
ヽ＿＿＿＞､＿_／
       ｜( 王 ﾉ〈   
       /ﾐ`ー―彡\\  
      / ╰    ╯ \\ /   \\>'''

