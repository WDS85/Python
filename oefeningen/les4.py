# soorten_fruit = ["Appel", "Banaan", "Appelsien", "Peer"]
# for fruit in soorten_fruit:
#     print(fruit)

# for temp in range(6):
#     print("Learning Loops")

# for temp in range(6):
#     print("Loop is on iteration number") + str(temp +1))

# count = 0
# while count <= 10:
#     print(count)
#     count += 1

#while loop gebruiken om te itereren
#
# soorten_fruit = ["Appel", "Banaan", "Appelsien", "Peer"]
# len_soorten_fruit = len(soorten_fruit)
# index = 0
# while index < len_soorten_fruit:
#     print(soorten_fruit[index])
#     index += 1

#item zoeken in een lijst en break gebruiken om loop te stoppen
# soorten_fruit = ["Appel", "Banaan", "Appelsien", "Peer"]
# for item in soorten_fruit:
#     if item == "Appelsien":
#         break
# print("End Of Search")

#de huidige iteratie van lus overslaan, verder gaan zolang de if trigger niet triggert
# cijfers = [1, 2, -1, 3, -3, 4, 5]
# for i in cijfers:
#     if i <=0:
#         continue
#     print(i)

#nested loops
# project_teams = ["Tim"], ["Tom"], []
# for teams in project_teams:µ
#     for teamlid in teams:
#     print(teamlid)

# single_digits = range(10)
# squares = []
# for digit in single_digits:
#     print(digit)
#     squares.append(digit*2)

# print(squares)

# lijst = ["*", "**","***","****","*****"]
# for item in lijst:
#     print(item)

# for i in range(1, 6):
#     print("*" * i)

#functies
#def function_name():
    #taken

# #functie definieren
# def trip_welcome():
#     print("Welcome to Tripcademy")
#     print("Select your destination")
#     #alles binnen deze insprong valt onder de functie
# #functie oproepen 
# trip_welcome()

# print("Checking the weather")
# def weather_check():
#     print("Het is een mooie dag om te reizen")
#     print("Waarschuwing: er is kans op regen")

# weather_check()

#bij de def kunnen we aangeven dat we parameters verwachten


# getallen = []
# even = []
# index = len(getallen)

# while index <= 9:
#     getal = int(input("Geef 10 getallen in"))
#     getallen.append(getal)
#     index += 1
# print("Dit waren 10 getallen")
# # print(getallen)

# for i in getallen:
#     if i % 2  == 0:
#         even.append(i)
#         # print(even)

# gemiddelde = sum(even) / len(even)
# print(gemiddelde)


# even_getallen = []
# for i in range(10):
#     getal = int(input("Voer een getal in"))
#     if getal % 2 ==0:
#         even_getallen.append(getal)

# if even_getallen:
#     gemiddelde = sum(even_getallen) / len(even_getallen)
#     print(f"Het gemiddelde van de even getallen is {gemiddelde}")
# else:
#     print(f"Er zijn geen even getallen ingevoerd")

# getallen = [20, 21, 53, 54, 60, 80, 90]

# for getal in getallen:
#     if getal % 2 ==0:
#         print(getal)


# reeks1 = range(11)
# reeks2 = range(11, 21)
# index = 11

# for getal in reeks1:
#     if getal % 2 ==0:
#         print(getal)
#         if getal % 3 ==0:
#             continue


# while index <= 20:
#     for i in reeks2:
#         if i % 2 ==0:
#             print(i)
#             index += 1
#             if i == 17:
#                 break

# totaal = 0
# while totaal <= 100:
#     getal = int(input("Voer een getal in "))
#     totaal += getal
# print(totaal)

# getallen = [11, 17, 14, 15, 9, 2, 5, 4, 6, 13, 1, 20, 8, 7, 3]
# for getal in getallen:
#     if getal == 13:
#         print("Het getal is 13. STOP")
#         break
#     else:
#         print(getal)





            