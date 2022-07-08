# # list comprehension
# # new_list = [new_item for new_item in items if new_item < 0]
# # dictionary comprehension
# # dict = {something : for i in eyes / for (key,value) in dictionary.items() if (test)}
# names = ['Alex', 'Beth', 'Cathy', 'Daggy']
# # so tth goal is to ...
# # student_score ={
# # 'name' : score
# # }
# import random
# import pandas
# student_score = {n: random.randint(1, 100) for n in names}
# print(student_score)
# # passed_student = {n: student_score[n] for n in student_score if student_score[n] > 50}
# # comprenhension= {student : score for (student,score) in student_score.items() if score>50}
# # weather = {'monday':12,'tuesday':8,'wedsday':15}
# #
# # adjusted = {days:temp+30 for (days,temp) in weather.items()}
#
# # looping through dataframe
# stud = {
#     'Student' : ['Alex', 'Beth', 'Cathy','Daggy'],
#     'Score' : [312,42,13,4]
# }
# stud_pandas = pandas.DataFrame(stud)
# for (index,row) in stud_pandas.iterrows():
#     print(row)
import pandas
database = pandas.read_csv('nato_phonetic_alphabet.csv')
database_dict = {row.letter: row.code for (index, row) in database.iterrows()}
user_input = input('Enter Your Name :').upper()
result = [database_dict[n] for n in user_input if n in database_dict]
print(result)
