title_message = """


Kursbestätigung


"""

with open('names.txt', 'r') as f:
    for lines in f:
        info = lines.split(',')
        name = info[0]
        level = info[1]
        course_type = info[2]
        course_start = info[3]
        course_end = info[4]
        print(f"Wir bestätigen hiermit, dass {name} den Kurs {level} {course_type}-Kurs an unserer Schule absolviert hat.\nDer Kurs fand vom {course_start} bis {course_end} statt.")
