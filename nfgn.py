job = int(input("אם אתה מורה הכנס את המספר 0 אם אתה תלמיד הכנס את המספר 1"))
if job == 0:
    teacher_name = input("הכנס את השם שלך")
    teacher_email = input("הכנס את כתובת המייל שלך")
    teacher_subject = input("איזה מקצוע אתה מלמד?")
    if teacher_subject == "מתמטיקה":
        math_teacher = int(input("מה מספר היחידות שאתה מלמד?"))
    if teacher_subject == "אנגלית":
        english_teacher = int(input("מה מספר היחידות שאתה מלמד?"))
    grade10 = input("אתה מלמד את כיתה י?")
    if grade10 == "כן":
        num_grade10 = input("מה מספרי הכיתות שאתה מלמד(הפרד בין הכיתות בפסיקים)")
    grade11 = input("אתה מלמד את כיתה יא?")
    if grade11 == "כן":
        num_grade11 = input("מה מספרי הכיתות שאתה מלמד(הפרד בין הכיתות בפסיקים)")
    grade12 = input("אתה מלמד את כיתה יב?")
    if grade12 == "כן":
        num_grade12 = input("מה מספרי הכיתות שאתה מלמד(הפרד בין הכיתות בפסיקים)")

# users = open("users.text", "r")
users = open("users.text", "a")
users.write(teacher_name + "," + teacher_email + "," + teacher_subject)
print(users.read())

if job == 1:
    student_name = input("הכנס את השם שלך")
    student_email = input("הכנס את כתובת המייל שלך")
    ca = input("איזה כיתה אתה?")
    h = input("איזה שכבה אתה?")
    student_hours_dictionary = {
        "sunday": {0: "empty", 1: "empty", 2: "empty", 3: "empty", 4: "empty", 5: "empty", 6: "empty", 7: "empty",
                   8: "empty", 9: "empty", 10: "empty"},
        "monday": {0: "empty", 1: "empty", 2: "empty", 3: "empty", 4: "empty", 5: "empty", 6: "empty", 7: "empty",
                   8: "empty", 9: "empty", 10: "empty"},
        "tuesday": {0: "empty", 1: "empty", 2: "empty", 3: "empty", 4: "empty", 5: "empty", 6: "empty", 7: "empty",
                    8: "empty", 9: "empty", 10: "empty"},
        "wednesday": {0: "empty", 1: "empty", 2: "empty", 3: "empty", 4: "empty", 5: "empty", 6: "empty", 7: "empty",
                      8: "empty", 9: "empty", 10: "empty"},
        "thursday": {0: "empty", 1: "empty", 2: "empty", 3: "empty", 4: "empty", 5: "empty", 6: "empty", 7: "empty",
                     8: "empty", 9: "empty", 10: "empty"},
        "friday": {0: "empty", 1: "empty", 2: "empty", 3: "empty", 4: "empty", 5: "empty", 6: "empty", 7: "empty",
                   8: "empty", 9: "empty", 10: "empty"}
    }
    student_hours_dictionary["sunday"][0] = input("הכנס שעה 0 יןם ראשון(אם אין שיעור הכנס רווח)")
    student_hours_dictionary["sunday"][1] = input("הכנס שעה 1 יןם ראשון(אם אין שיעור הכנס רווח)")
    student_hours_dictionary["sunday"][2] = input("הכנס שעה 2 יןם ראשון(אם אין שיעור הכנס רווח)")
    student_hours_dictionary["sunday"][3] = input("הכנס שעה 3 יןם ראשון(אם אין שיעור הכנס רווח)")
    student_hours_dictionary["sunday"][4] = input("הכנס שעה 4 יןם ראשון(אם אין שיעור הכנס רווח)")
    student_hours_dictionary["sunday"][5] = input("הכנס שעה 5 יןם ראשון(אם אין שיעור הכנס רווח)")
    student_hours_dictionary["sunday"][6] = input("הכנס שעה 6 יןם ראשון(אם אין שיעור הכנס רווח)")
    student_hours_dictionary["sunday"][7] = input("הכנס שעה 7 יןם ראשון(אם אין שיעור הכנס רווח)")
    student_hours_dictionary["sunday"][8] = input("הכנס שעה 8 יןם ראשון(אם אין שיעור הכנס רווח)")
    student_hours_dictionary["sunday"][9] = input("הכנס שעה 9 יןם ראשון(אם אין שיעור הכנס רווח)")
    student_hours_dictionary["sunday"][10] = input("הכנס שעה 10 יןם ראשון(אם אין שיעור הכנס רווח)")
    student_hours_dictionary["monday"][0] = input("הכנס שעה 0 יןם שני(אם אין שיעור הכנס רווח)")
    student_hours_dictionary["monday"][1] = input("הכנס שעה 1 יןם שני(אם אין שיעור הכנס רווח)")
    student_hours_dictionary["monday"][2] = input("הכנס שעה 2 יןם שני(אם אין שיעור הכנס רווח)")
    student_hours_dictionary["monday"][3] = input("הכנס שעה 3 יןם שני(אם אין שיעור הכנס רווח)")
    student_hours_dictionary["monday"][4] = input("הכנס שעה 4 יןם שני(אם אין שיעור הכנס רווח)")
    student_hours_dictionary["monday"][5] = input("הכנס שעה 5 יןם שני(אם אין שיעור הכנס רווח)")
    student_hours_dictionary["monday"][6] = input("הכנס שעה 6 יןם שני(אם אין שיעור הכנס רווח)")
    student_hours_dictionary["monday"][7] = input("הכנס שעה 7 יןם שני(אם אין שיעור הכנס רווח)")
    student_hours_dictionary["monday"][8] = input("הכנס שעה 8 יןם שני(אם אין שיעור הכנס רווח)")
    student_hours_dictionary["monday"][9] = input("הכנס שעה 9 יןם שני(אם אין שיעור הכנס רווח)")
    student_hours_dictionary["monday"][10] = input("הכנס שעה 10 יןם שני(אם אין שיעור הכנס רווח)")
    student_hours_dictionary["tuesday"][0] = input("הכנס שעה 0 יןם שלישי(אם אין שיעור הכנס רווח)")
    student_hours_dictionary["tuesday"][1] = input("הכנס שעה 1 יןם שלישי(אם אין שיעור הכנס רווח)")
    student_hours_dictionary["tuesday"][2] = input("הכנס שעה 2 יןם שלישי(אם אין שיעור הכנס רווח)")
    student_hours_dictionary["tuesday"][3] = input("הכנס שעה 3 יןם שלישי(אם אין שיעור הכנס רווח)")
    student_hours_dictionary["tuesday"][4] = input("הכנס שעה 4 יןם שלישי(אם אין שיעור הכנס רווח)")
    student_hours_dictionary["tuesday"][5] = input("הכנס שעה 5 יןם שלישי(אם אין שיעור הכנס רווח)")
    student_hours_dictionary["tuesday"][6] = input("הכנס שעה 6 יןם שלישי(אם אין שיעור הכנס רווח)")
    student_hours_dictionary["tuesday"][7] = input("הכנס שעה 7 יןם שלישי(אם אין שיעור הכנס רווח)")
    student_hours_dictionary["tuesday"][8] = input("הכנס שעה 8 יןם שלישי(אם אין שיעור הכנס רווח)")
    student_hours_dictionary["tuesday"][9] = input("הכנס שעה 9 יןם שלישי(אם אין שיעור הכנס רווח)")
    student_hours_dictionary["tuesday"][10] = input("הכנס שעה 10 יןם שלישי(אם אין שיעור הכנס רווח)")


    def h1():
        class ca1:
            s1 = input("מה המגמה הראשונה שלך")
            s2 = input("מה המגמה השנייה שלך")
            points_math = int(input("כמה יחידות אתה במתמטטיקה"))
            points_english = int(input("כמה יחידות אתה באנגלית"))

        class ca2:
            s1 = input("מה המגמה הראשונה שלך")
            s2 = input("מה המגמה השנייה שלך")
            points_math = int(input("כמה יחידות אתה במתמטטיקה"))
            points_english = int(input("כמה יחידות אתה באנגלית"))

        class ca3:
            s1 = input("מה המגמה הראשונה שלך")
            s2 = input("מה המגמה השנייה שלך")
            points_math = int(input("כמה יחידות אתה במתמטטיקה"))
            points_english = int(input("כמה יחידות אתה באנגלית"))

        class ca4:
            s1 = input("מה המגמה הראשונה שלך")
            s2 = input("מה המגמה השנייה שלך")
            points_math = int(input("כמה יחידות אתה במתמטטיקה"))
            points_english = int(input("כמה יחידות אתה באנגלית"))

        class ca5:
            s1 = input("מה המגמה הראשונה שלך")
            s2 = input("מה המגמה השנייה שלך")
            points_math = int(input("כמה יחידות אתה במתמטטיקה"))
            points_english = int(input("כמה יחידות אתה באנגלית"))

        class ca6:
            s1 = input("מה המגמה הראשונה שלך")
            s2 = input("מה המגמה השנייה שלך")
            points_math = int(input("כמה יחידות אתה במתמטטיקה"))
            points_english = int(input("כמה יחידות אתה באנגלית"))

        class ca7:
            s1 = input("מה המגמה הראשונה שלך")
            s2 = input("מה המגמה השנייה שלך")
            points_math = int(input("כמה יחידות אתה במתמטטיקה"))
            points_english = int(input("כמה יחידות אתה באנגלית"))

        class ca8:
            s1 = input("מה המגמה הראשונה שלך")
            s2 = input("מה המגמה השנייה שלך")
            points_math = int(input("כמה יחידות אתה במתמטטיקה"))
            points_english = int(input("כמה יחידות אתה באנגלית"))

        class ca9:
            s1 = input("מה המגמה הראשונה שלך")
            s2 = input("מה המגמה השנייה שלך")
            points_math = int(input("כמה יחידות אתה במתמטטיקה"))
            points_english = int(input("כמה יחידות אתה באנגלית"))

        class ca10:
            s1 = input("מה המגמה הראשונה שלך")
            s2 = input("מה המגמה השנייה שלך")
            points_math = int(input("כמה יחידות אתה במתמטטיקה"))
            points_english = int(input("כמה יחידות אתה באנגלית"))


    def h2():
        class ca1:
            s1 = input("מה המגמה הראשונה שלך")
            s2 = input("מה המגמה השנייה שלך")
            points_math = int(input("כמה יחידות אתה במתמטטיקה"))
            points_english = int(input("כמה יחידות אתה באנגלית"))

        class ca2:
            s1 = input("מה המגמה הראשונה שלך")
            s2 = input("מה המגמה השנייה שלך")
            points_math = int(input("כמה יחידות אתה במתמטטיקה"))
            points_english = int(input("כמה יחידות אתה באנגלית"))

        class ca3:
            s1 = input("מה המגמה הראשונה שלך")
            s2 = input("מה המגמה השנייה שלך")
            points_math = int(input("כמה יחידות אתה במתמטטיקה"))
            points_english = int(input("כמה יחידות אתה באנגלית"))

        class ca4:
            s1 = input("מה המגמה הראשונה שלך")
            s2 = input("מה המגמה השנייה שלך")
            points_math = int(input("כמה יחידות אתה במתמטטיקה"))
            points_english = int(input("כמה יחידות אתה באנגלית"))

        class ca5:
            s1 = input("מה המגמה הראשונה שלך")
            s2 = input("מה המגמה השנייה שלך")
            points_math = int(input("כמה יחידות אתה במתמטטיקה"))
            points_english = int(input("כמה יחידות אתה באנגלית"))

        class ca6:
            s1 = input("מה המגמה הראשונה שלך")
            s2 = input("מה המגמה השנייה שלך")
            points_math = int(input("כמה יחידות אתה במתמטטיקה"))
            points_english = int(input("כמה יחידות אתה באנגלית"))

        class ca7:
            s1 = input("מה המגמה הראשונה שלך")
            s2 = input("מה המגמה השנייה שלך")
            points_math = int(input("כמה יחידות אתה במתמטטיקה"))
            points_english = int(input("כמה יחידות אתה באנגלית"))

        class ca8:
            s1 = input("מה המגמה הראשונה שלך")
            s2 = input("מה המגמה השנייה שלך")
            points_math = int(input("כמה יחידות אתה במתמטטיקה"))
            points_english = int(input("כמה יחידות אתה באנגלית"))

        class ca9:
            s1 = input("מה המגמה הראשונה שלך")
            s2 = input("מה המגמה השנייה שלך")
            points_math = int(input("כמה יחידות אתה במתמטטיקה"))
            points_english = int(input("כמה יחידות אתה באנגלית"))


    def h3():
        class ca1:
            s1 = input("מה המגמה הראשונה שלך")
            s2 = input("מה המגמה השנייה שלך")
            points_math = int(input("כמה יחידות אתה במתמטטיקה"))
            points_english = int(input("כמה יחידות אתה באנגלית"))

        class ca2:
            s1 = input("מה המגמה הראשונה שלך")
            s2 = input("מה המגמה השנייה שלך")
            points_math = int(input("כמה יחידות אתה במתמטטיקה"))
            points_english = int(input("כמה יחידות אתה באנגלית"))

        class ca3:
            s1 = input("מה המגמה הראשונה שלך")
            s2 = input("מה המגמה השנייה שלך")
            points_math = int(input("כמה יחידות אתה במתמטטיקה"))
            points_english = int(input("כמה יחידות אתה באנגלית"))

        class ca4:
            s1 = input("מה המגמה הראשונה שלך")
            s2 = input("מה המגמה השנייה שלך")
            points_math = int(input("כמה יחידות אתה במתמטטיקה"))
            points_english = int(input("כמה יחידות אתה באנגלית"))

        class ca5:
            s1 = input("מה המגמה הראשונה שלך")
            s2 = input("מה המגמה השנייה שלך")
            points_math = int(input("כמה יחידות אתה במתמטטיקה"))
            points_english = int(input("כמה יחידות אתה באנגלית"))

        class ca6:
            s1 = input("מה המגמה הראשונה שלך")
            s2 = input("מה המגמה השנייה שלך")
            points_math = int(input("כמה יחידות אתה במתמטטיקה"))
            points_english = int(input("כמה יחידות אתה באנגלית"))

        class ca7:
            s1 = input("מה המגמה הראשונה שלך")
            s2 = input("מה המגמה השנייה שלך")
            points_math = int(input("כמה יחידות אתה במתמטטיקה"))
            points_english = int(input("כמה יחידות אתה באנגלית"))

        class ca8:
            s1 = input("מה המגמה הראשונה שלך")
            s2 = input("מה המגמה השנייה שלך")
            points_math = int(input("כמה יחידות אתה במתמטטיקה"))
            points_english = int(input("כמה יחידות אתה באנגלית"))


print(("hi"))
