#functies stellen ons in staat om code te groeperen in herbruikbare blokken

# #functie definieren
# def fuctie_naam():

# #functie aanroepen
# fuctie_naam()

#functie aanmaken en printen
# def weather_check():
#     print("Het is een mooie dag om te reizen")
#     print("Het ziet er naar uit dat het gaat regenen")

# weather_check()

#parameter definieren
# def trip_welcome(destination):
#     print("Welcome to Tripcademy")
#     print(f"Looks like you're heading to {destination} today")

# trip_welcome("New York")

# def getallen():
#     getallen = []
#     for i in range(10):
#         getal = int(input("Voer een getal in "))
#         if getal % 2 ==0:
#             getallen.append(getal)
#             print(f"{getal} werd toegevoegd")
#         else:
#             print(f"{getal} is niet even")
    
#     gemiddelde = sum(getallen) / len(getallen)
#     print(f"Het gemiddelde van de getallen is {gemiddelde:.2f}")

# getallen()

# import random

# getallen = [random.randint(1, 100) for i in range(15)]
# print(getallen)
# for getal in getallen:
#     if getal % 2 == 0:
#         print(f"{getal} is even")
#     else:
#         print(f"{getal} is oneven")


#getallen sorten met while and for loop


# getallen = list(range(1, 21))

# even_getallen_for = 0


# for getal in getallen:
#     if getal < 10:
#         if getal % 3 == 0:
#             continue
#         elif getal % 2 == 0:
#             even_getallen_for += 1

# even_getallen_while = 0
# index = 11

# while index <= 20:
#     if index == 17:
#         break
#     elif index % 3 == 0:
#         index += 1
#         continue
#     elif getal % 2 == 0:
#         even_getallen_while += 1
#     index += 1

# print(even_getallen_for)
# print(even_getallen_while)

#getallen optellen tot 100
# totaal = 0

# while totaal <= 100:
#     print("Voer een getal in ", end="")
#     getal= float(input())
#     if getal == 0:
#         print("0 is geen geldige invoer")
#     elif getal < 0:
#         print("Negatieve waarden zijn niet geldig")
#     else:
#         totaal += getal
# print(totaal)


#vroegtijd eindigen van een lus

import random
getallen = [random.randint(1, 20) for i in range(10)]
print(getallen)

for getal in getallen:
    if getal == 13:
        print(f"Het getal {13} werd gevonden. Einde van de lus")
        break
    else:
        print(getal)


    
