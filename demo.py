# dictionary comprehension
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# formula: new_dict={new_key:new_value for item in list}
student_score = {student: random.randint(1, 100) for student in names}
print(student_score)

# formula: new_dict={new_key:new_value for (key,val) in dict_items if test}
# get students who scored more than 65
student_passed = {student: score for (student, score) in student_score.items() if student_score[student] > 65}
print(student_passed)
# -------------- or ---------------
student_passed = {student: score for (student, score) in student_score.items() if score > 65}
print(student_passed)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:

weather_f = {day: (temp_c * 9 / 5) + 32 for (day, temp_c) in weather_c.items()}

print(weather_f)

student_dict={
    "names":["sharath","gia","joey"]
    "score":[98,87,88]
}
for (key,val) in student_dict.items():
    print(key)
    print(val)

import pandas

