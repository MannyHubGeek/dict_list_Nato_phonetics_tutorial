#
# numbers = [1, 2, 3]
#
# # new_list = []
# #
# # for number in numbers:
# #     temp = number + 1
# #     new_list.append(temp)
# #
# # print(new_list)
#
# new_list_comprehension = [number + 1 for number in numbers]
#
# name = "Emmanuel"
# new_name = [letter for letter in name]
# print(new_name)
#
#
# new_range = [number * 2 for number in range(1, 5)]
#
# print(new_range)
#
# # Conditional List Comprehension
#
# names = ["Emmanuel", "Kasia", "Jasper", "Betuel", "Leo"]
#
# new_names = [name for name in names if len(name) > 3 and len(name) < 6]
# print(new_names)
#
# # Turn names to upper case
# new_names = [name.upper() for name in names if len(name) > 3 and len(name) < 6]
# print(new_names)
#
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above 👆
#
# #Write your 1 line code 👇 below:
#
# squared_numbers = [number * number for number in numbers]
#
# #Write your code 👆 above:
#
# print(squared_numbers)
#
#
#
#
#
#
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above
#
# #Write your 1 line code 👇 below:
#
# result = [num for num in numbers if not num % 2]
#
# #Write your code 👆 above:
#
# print(result)

#
# f1 = open("file1.txt", "r")
# file1 = f1.readlines()
# f2 = open("file2.txt", "r")
# file2 = f2.readlines()
#
# result = [int(num) for num in file1 if num in file2]
# # Write your code above 👆
#
# print(result)

# Dictionary Comprehension

# new_dict = {new_key: new_value for item in list}
#
#
# new_dict = {new_key: new_value for (key, value)  in dict.items()}
#
# new_dict = {new_key: new_value for (key, value)  in dict.items() if test}


# import random
# names = ["Emmanuel", "Kasia", "Jasper", "Betuel", "Leo"]
#
# new_dict = {student:random.randint(1, 101) for student in names}
# print(new_dict)
#
# passed_students = {student:score for (student, score) in new_dict.items() if score > 40}
# print(passed_students)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
#
# # Write your code below:
# result = {word:len(word) for word in sentence.split()}
#
# print(result)


# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆
#
#
# # Write your code 👇 below:
# weather_f = {day:temp*9/5+32 for (day, temp ) in weather_c.items()}
#
#
# print(weather_f)
#
# # Pandas dataframe looping
import pandas
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 65, 49]
# }
# student_df = pandas.DataFrame(student_dict)
# for (index, row) in student_df.iterrows():
#     #print(row.student, row.score)
#     # if row.score > 500:
#     #     print(row.score, row.student)
#     if row.student == "James":
#         print(row.score)

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_al = pandas.DataFrame(data)

new_nato = {row.letter:row.code for (index, row) in nato_al.iterrows()}
print(new_nato["A"])
user = "come"
user_input = list(user.upper())
spell = [new_nato[letter] for letter in user_input]
print(spell)