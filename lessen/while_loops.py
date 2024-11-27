#while <conditional statement>:
#    <action>

#getallen afdrukken
# count = 0
# while count <= 3:
#     print(count)
#     count += 1

#getallen afdrukken in 1 regel
# count = 0
# while count <= 3: print(count); count += 1

#while loop gebruiken om door een lijst te itereren
# games = ["Call of Duty", "God Of War", "Spider-Man", "Astro Bot", "Detroit"]
# length = len(games)
# index = 0

# while index < length:
#     print(games[index])
#     index += 1

#item zoeken in list, break toepassen
# games = ["Call of Duty", "God Of War", "Spider-Man", "Astro Bot", "Detroit"]
# for game in games:
#     if game == "God Of War":
#         print("Gevonden")
#         break
# print("Zoektocht beindigd")

#continue
# big_numnber_list = [1, 2, -1, 4, -5, 5, 2, -9]
# for i in big_numnber_list:
#     if i <=0:
#         continue
#     print(i)

#nested loops
# project_teams = [
#     ["Ava", "Samantha", "James"], 
#     ["Lucille", "Zed"], 
#     ["Edgar", "Gabriel"]
#     ]
# #elk team printen
# for teams in project_teams:
#     #print(teams)
# #elk lid van een team printen, nested loop
#     for staff in teams:
#         print(staff)


#een lege lijst bewerken via andere lijst
# single_digits = range(10)
# squares = []

# for digit in single_digits:
#     squares.append(digit * 2)
#     print(digit)

# print(squares)

#sterren printen
# index = range(6)

# for i in index:
#     stars = "*" * i
#     print(stars)