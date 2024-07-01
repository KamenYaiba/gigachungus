import config

AR = 0
EN = 1

arabic_menu = '''/lang To change the language to English


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

english_menu = '''/lang لتغيير اللغة إلى العربية


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

b_ar = f'''أرسل رسالة بالصيغة التالية:

نوع التقرير(b)
عدد النقاط التي حصلت عليها
الساعات المسجلة
الساعات المجتازة
عدد الفصول التي أكملتها(لا تحسب التحضيري والفصول الصيفية)
{config.colleges_acro[AR]}
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
b_en = f'''send a message in the following format:

Report Type(a)
Points you gained
Registered hours
Passed Hours
Number of semesters you've passed(PYP and summer semesters don't count)
{config.colleges_acro[EN]}
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

report_c_manual = ['انسخ رقم الطلب واضغط تشغيل' + f'<a href="{config.arabic_form_link}">.</a>', 'Copy the request number and click launch' + f'<a href="{config.english_form_link}">.</a>']

report_help = ['سجل الدخول في بوابة النظام الأكاديمي"Edugate"\nأكاديمي>السجل الأكاديمي',
               'Log in to your Edugate account\nAcademic > Academic Transcript']
report_help_photo = ['arabic_report_help.png', 'english_report_help.png']

greet = ['arabic_greeting.png', 'english_greeting.png']
report_a = ['تقرير من نوع أ', 'Report Type A']
report_b = ['تقرير من نوع ب', 'Report Type B']
report_c = ['تقرير من نوع ج', 'Report Type C']
GPA = ['المعدل التراكمي: ', 'Cumulative GPA: ']
passed_hours = ['الساعات المجتازة: ', 'Hours Passed: ']
max_gpa = ['أعلى معدل يمكن التخرج به: ', 'Max possible graduation GPA: ']
exact_gpa = ['المعدل التراكمي بالضبط: ', 'Exact Cumulative GPA: ']
sem_gpa = ['المعدل الفصلي: ', 'Semester GPA: ']
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
max_gpa_next_semester = [f'أعلى معدل تراكمي ممكن بعد الفصل القادم(بافتراض أنك ستسجل {config.DEFAULT_SEMESTER_HOURS} ساعة وتحصل على  A+ في جميع المواد): ',
    f'The highest possible cumulative GPA after the next semester (assuming you register for {config.DEFAULT_SEMESTER_HOURS} hours and get an A+ in all courses): ']
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
max_boost_def = [f'أقصى زيادة ممكنة للمعدل التراكمي(بافتراض أنك ستسجل {config.DEFAULT_SEMESTER_HOURS} ساعة وتحصل علىA + في جميع المواد فس الفصل القادم): ',
                 f'Max possible Cumulative GPA boost (Assuming you register for {config.DEFAULT_SEMESTER_HOURS} hours and get A+ in all courses next semester): ']

max_boost = [f'أقصى زيادة ممكنة للمعدل التراكمي بعد الفصل القادم(بافتراض أنك ستحصل على A+ في جميع المواد): ',
             f'Max possible Cumulative GPA boost (Assuming you get A+ in all courses): ']

college = ['الكلية: ', 'College: ']

invalid_format_warning = ['خطأ في تنسيق الطلب! يرجى اتباع التنسيق المقدم لكم',
                          'Invalid format! please follow the format provided previously']
wrong_info = ['البيانات التي قدمتها لا تبدو صحيحة! يرجى مراجعتها',
              "The data you provided doesn't seem to make sense! try again please"]
no_such_college = ['لم نعثر على كليتك\n\ncl:القانون\nce: الهندسة\ncb: إدارة الأعمال\ncd: العمارة والتصميم\nch: الإنسانيات والعلوم',
                   'We couldn\'t find your college\n\ncl: Law\nce: Engineering\ncb: Business\ncd: Architecture and Design\nch:College of Humanities and Sciences']
language_changed = ["لقد غيرت اللغة إلى العربية", "Language changed to English"]
click2copy = ['اضغط للنسخ', 'Click to copy']


def after_next_semester(sem_hours, lost_points):
    return [f'بعد الفصل القادم ({sem_hours} ساعة مسجلة وخسارة {lost_points} نقاط)\n',
            f'After next semester ({sem_hours} hours, and {lost_points} lost points)\n']


gpa_change = ['تغير المعدل: ', 'GPA change: ']
down = ['↙↙', '↘↘']
up = ['↖↖', '↗↗']
constant = ['⬅⬅', '➡➡']

uni = ['الجامعة: ', 'University: ']
yes = [' نعم 🎉', ' Yes! 🎉']
no = [' لا', ' No']

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

