# som = range(1, 11)
# for num in som:
#     print(num)

# totaal = 0
# som_range = range(1, 21)
# for num in som_range:
#     totaal += num

# print(totaal)

# getal = range(1, 31)
# for num in getal:
#     if num %2 == 0:
#         print(num, 'is even')
#     else:
#         print(num, 'is oneven')

# getal = int(input('Kies een nummer'))
# factor = range(1, 11)
# for num in factor:
#     print(getal, 'x', num, '=', getal*num)

# getal = range(1, 11)
# for num in getal:
#     print(f"{num}^2 = {num**2}")

# getal = int(input("Kies een getal"))
# faculteit = 1
# for num in range(1, getal + 1):
#     faculteit *= num

# print(f"De faculteit van {getal} is {faculteit}")

# reeks = int(input("Kies hoe groot de reeks moet zijn"))
# basis = 1
# for num in range(reeks - 1):
#     print(f"0, 1, {basis + num}")

# getal = int(input("Geef een getal in"))
# if getal %2 == 0:
#     print(f"{getal} is even")
# else:
#     print(f"{getal} is oneven")

# letters=["a","b","c","d","e","f","g"]
# print(letters[2:6])

# studenten = ['Jef', "Bram", 'Joske', "Marie"]
# student_vier = studenten[3]
# print(student_vier)

# my_range = (list(range(1, 10, 2)))
# print(my_range)



#lijst met random cijfers bewerken


# import random

# lijst = []

# for i in range(5):
#     lijst.append(random.randint(1, 50))
# lijst.sort()
# print(lijst)

# lijst.pop(2)
# print(lijst)

# nummers = []

# for i in range(1, 6):
#     nummers.append(i)
# print(nummers)

# nummers.pop(2)
# nummers.insert(1, 6)
# nummers.remove(2)
# print(nummers)





#even of oneven getal bepalen van random getallen

# import random

# getallen = [random.randint(1, 100) for i in range(5)]
# print(getallen)

# # for getal in getallen:
# #     if getal % 2 == 0:
# #         print(f"Even getal: {getal}")
# #     else:
# #         print(f"Oneven getal: {getal}")

# for getal in getallen:
#     if getal < 10:
#         print(f"Kleiner dan 10: {getal}")
#     else:
#         print(f"Groter dan 10: {getal}")





#lijst met punten aanmaken en bewerken, gemiddelde berekenen en laten raden

# punten = [85, 92, 78, 90, 88, 76, 89, 95, 80]
# punten.append(84)
# print(punten)
# punten.remove(76)
# print(punten)
# punten.insert(2, 91)
# print(punten)
# punten.sort()
# print(punten)

# gemiddelde = sum(punten) / len(punten)
# print(f"Het huidige gemiddelde is {gemiddelde}")
# if punten[-1] > 90:
#     punten = [punt + 5 for punt in punten]
# print(punten)
# nieuw_gemiddelde = sum(punten) / len(punten)
# print(nieuw_gemiddelde)
# while True:
#     guess = float(input("Raad het gemiddelde: "))
#     if guess == nieuw_gemiddelde:
#         print(f"Proficiat, dat klopt. Het gemiddelde is {nieuw_gemiddelde}")
#         break
#     else:
#         print(f"Helaas, niet juist")


#functie met string voor hoofdletters
# def to_uppercase(text):
#     return text.upper()
# input_str = 'Dit is een voorbeeld'
# output_str = to_uppercase(input_str)
# print(output_str)

#sterren printen
# def print_star_pattern(amount):
#     for i in range(1, amount + 1):
#         print('*' * i)

# print_star_pattern(5)


#countdown to lancering
# def countdown(tminus):
#     while tminus > 0:
#         print(f"{tminus} seconds to launch")
#         tminus -= 1
#         if tminus == 0:
#             print("Lancering!")

# countdown(20)

#print_even_nummers
# def print_even_numbers(limit):
#     index = 0
#     while index <= limit:
#         if index % 2 == 0:
#             print(index)
#         index += 1
    
#     print(f"{limit} werd bereikt")

# print_even_numbers(int(input("Geef een limiet op ")))

#fizz
# def fizz():
#     for i in range(1, 51):
#         if i % 3 == 0 and i % 5 == 0:
#             print('FizzBuzz')
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)

# fizz() 

#calculator
# def calculator():
#     num1 = float(input("Voer het eerste getal in "))
#     num2 = float(input("Voer het tweede getal in "))
#     op = str(input("Voer de operator in "))
#     totaal = 0

#     if op == '+':
#         totaal = num1 + num2
#         print(f"{num1} {op} {num2} = {totaal}")
#     elif op == "-":
#         totaal = num1 - num2
#         print(f"{num1} {op} {num2} = {totaal}")
#     elif op == "*":
#         totaal = num1 * num2
#         print(f"{num1} {op} {num2} = {totaal}")
#     elif op == "/":
#         totaal = num1 / num2
#         print(f"{num1} {op} {num2} = {totaal}")
#     else:
#         print("De verkeerde operator werd ingegeven")
#         return

# calculator()

#woordenboek
# vertalingen = {
#     "mountain": "orod",
#     "bread": "bass",
#     "friend": "mellon",
#     "horse": "roch",
# }

# vertalingen["test"] = "test"
# print(vertalingen)

#waarde toevoegen aan woordenboek
# animals_in_zoo = {}
# animals_in_zoo["zebras"] = "8"
# animals_in_zoo["apen"] = "12"
# animals_in_zoo["dinosaurussen"] = "0"

# print(animals_in_zoo)

#meerdere waarden toevoegen aan woordenboek
# sensors = {
#     "linving room": 21,
#     "kitchen": 23,
#     "bedroom": 20,
#     }
# print(sensors)
# sensors.update({
#     "pantry": 22,
#     "guest room": 25,
#     "patio": 34,
#     })
# print(sensors)

#twee lijsten combineren in woordenboek
# names = [
#     "Jenny",
#     "Alexus",
#     "Sam",
#     "Grace",
# ]

# heights = [
#     61,
#     70,
#     67,
#     64,
# ]

# #students = {key:value for key, value in zip(names, heights)}
# #alternatief zip
# students = dict(zip(names, heights))
# print(students)

#waarde uitlezen met get
# gebouwen = {
#     "Burj Khalifa": 828,
#     "Shanghai Tower": 632,
#     "Abrai Al Bait": 601,
#     "Ping An": 599,
#     "Lotte World Tower": 554.5,
#     "One World Trade": 541.3,
# }

# print(gebouwen.get("Shanghai Tower"))
# #waarde retourneren in dien niet bestaand
# print(gebouwen.get("Shanghai Tower", 0))

#waarden verwijderen uit woordenboek
# raffle = {
#     223842: "Teddy Bear",
#     872921: "Concert Tickets",
#     320291: "Gift Basket",
#     412123: "Necklace",
#     298787: "Pasta Maker"
# }
# print(raffle.pop(320291, "No Prize"))
# print(raffle)

#alle sleutels lezen / bewerken uit woordenboek
# test_scores = {
#     "Graces": [80, 72, 90],
#     "Jeffrey": [88, 68, 81],
#     "Sylvia": [80, 82, 84],
#     "Pedro": [98, 96, 95],
#     "Martin": [78, 80, 78],
#     "Dina": [64, 60, 75]
# }
# # print(list(test_scores))

# for score_list in test_scores.values():
#     print(score_list)

# for students in test_scores.keys():
#     print(students)

# auto = {
#     "Merk": "Toyota",
#     "Model": "Corolla",
#     "Jaar": 2022,
#     "Kleur": "Blauw"
# }

# print(auto.pop("Jaar"))
# print(auto.get("Brandstof", "Niet gespecifieerd"))
# print(auto)

#document lezen met python
# with open('real_cool_document.txt') as cool_doc:
#     cool_concent = cool_doc.read()
# print(cool_concent)

#lijnen lezen uit document
# with open("keats_sonnet.txt") as keats_doc:
#     for line in keats_doc.readlines():
#         print(line)

#1 lijn lezen uit document
# with open('millay_sonnet.txt') as millay_doc:
#     line1 = millay_doc.readline()
#     line2 = millay_doc.readline()
#     print(line1)

#bestand maken met python
# with open('generated_file.txt', 'w') as gen_file:
#     gen_file.write("What an incredible line")

#lijnen toevoegen aan document met python
# with open('generated_file.txt', "a") as gen_file:
#     gen_file.write("\n it still is")

#csv files lezen

# import csv

# list_of_email_addresses = []
# with open('users.csv', newline='') as users_csv:
#     user_reader = csv.DictReader(users_csv) #delimiter=";"
#     for row in user_reader:
#         list_of_email_addresses.append(row['Email'])

# print(list_of_email_addresses)

#csv files maken

# big_list = [
#     {'name': 'Fredrick Stein', 'userid': 6712359021, 'is_admin': False},
#     {'name': 'Wiltmore Denis', 'userid': 2525942, 'is_admin': False},
#     {'name': 'Greely Plonk', 'userid': 15890235, 'is_admin': False},
#     {'name': 'Dendris Stulo', 'userid': 572189563, 'is_admin': True}
# ]

# import csv

# with open("output.csv", "w", newline='') as output_csv:
#     fields = ['name', "userid", 'is_admin']
#     output_writer = csv.DictWriter(output_csv, fieldnames=fields)

#     output_writer.writeheader()
#     for item in big_list:
#         output_writer.writerow(item) 


#json uitlezen
import json

with open('purchase_14781239.json') as purchase_json:
    purchase_data = json.load(purchase_json)

    print(purchase_data['user'])

#json schrijven
import json

with open('output.json', "w", newline='') as output_json:
    json.dump('turn_to_json', output_json)