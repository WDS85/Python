# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
#
# is_even(4)
from lib2to3.pygram import python_grammar_no_print_statement


# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)
#     else:
#         continue

# def fibonacci(n):
#
#     a = 0
#     b = 1
#     lijst = []
#
#
#     while n != 0:
#         lijst.append(a)
#         a, b = b, a + b
#         n -= 1
#
#     return lijst
#
# print(fibonacci(6))

# scores = {
# #     "Anna": 85,
# #     "Bob": 92,
# #     "Claire": 88,
# #     "Daniel": 79
# # }
# #
# # scores["Emma"] = 91
# # print(scores)
# #
# # punten = scores.values()
# # gemiddelde = sum(punten) / len(punten)

#list comprehension
# kwadraten = [x**2 for x in range(1, 11)]
# print(kwadraten)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#tekst omdraaien
# def reverse_string(s):
#     reverse = s[::-1]
#     return reverse
#
# print(reverse_string("test"))

# def safe_devide(a, b):
#     if b == 0:
#         print("Kan niet door nul delen")
#     else:
#         totaal = a / b
#         print(totaal)
#
# safe_devide(10, 4)

#palindroom functie
# def is_palindrome(s):
#     s_reversed = s[::-1]
#     if s == s_reversed:
#         return True
#     else:
#         return False
#
# print(is_palindrome("radar"))

#woordenboek waarden uithalen, hoogste waarde uithalen
# student_scores = {
#     "Anna": 85,
#     "Bob": 92,
#     "Claire": 88,
#     "Daniel": 79
# }

# for student, score in student_scores.items():
#     print(student, score)

# top_student = max(student_scores, key=student_scores.get)
# print(top_student)

# numbers = [12, 45, 23, 67, 34, 89, 14, 56]
# even_numbers = []

# for num in numbers:
#     if num % 2 == 0:
#         even_numbers.append(num)

# kleinste_getal = min(numbers)
# grootste_getal = max(numbers)

# print(even_numbers)    
# print(kleinste_getal)
# print(grootste_getal)


# def remove_duplicates():
#     items = [5, 3, 9, 1, 3, 7, 5, 8, 9, 2]
#     no_dup = [set(items)]
#     print(no_dup)

# remove_duplicates()

# def remove_duplicates(lst):
#     seen = set()  # Een set om de al geziene elementen bij te houden
#     no_dup = []  # Een lege lijst voor de resultaten

#     for item in lst:
#         if item not in seen:  # Als het item nog niet is gezien
#             no_dup.append(item)  # Voeg het toe aan de lijst zonder duplicaten
#             seen.add(item)  # Markeer het item als gezien

#     return no_dup

# # Test de functie
# items = [5, 3, 9, 1, 3, 7, 5, 8, 9, 2]
# print(remove_duplicates(items))  # Output: [5, 3, 9, 1, 7, 8, 2]

# student_grades = {
#     "Anna": [85, 92, 88],
#     "Bob": [78, 85, 91],
#     "Claire": [88, 91, 94],
#     "Daniel": [79, 84, 88]
# }

# student_gem = {}


# for student, grades in student_grades.items():
#     gemiddelde = sum(grades) / len(grades)
#     student_gem[student] = gemiddelde

# print(student_gem)

# hoogste_cijfer_naam = max(student_gem, key=student_gem.get)
# hoogste_cijfer = student_gem[hoogste_cijfer_naam]
# print(hoogste_cijfer_naam, hoogste_cijfer)

#data uit bestand halen en gemiddelde
# students = {}

# with open('data.txt') as data_file:
#     for line in data_file:
#         line = line.strip()
#         student, grade = line.split()
#         students[student] = int(grade)

# gemiddelde = sum(students.values()) / len(students)

# print(gemiddelde)


#alternatief data uit bestand halen en gemiddelde 
# students = {}

# try:
#     with open('data.txt') as data_file:
#         for line in data_file:
#             line = line.strip()
#             student, grade = line.split()
#             students[student] = int(grade)

#     # Bereken het gemiddelde cijfer
#     gemiddelde = sum(students.values()) / len(students)

#     # Print het gemiddelde
#     print("Gemiddeld cijfer:", gemiddelde)

# except FileNotFoundError:
#     print("Het bestand 'data.txt' is niet gevonden.")
# except ValueError:
#     print("Er is een fout in de gegevens op een van de regels.")






