# index = int(input("Voer het aantal Fibonacci-termen in: "))
# fib = []  # Lijst om de Fibonacci-reeks op te slaan

# x, y = 0, 1  # Startwaarden van de reeks

# while index > 0:
#     fib.append(x)  # Voeg het huidige getal toe aan de lijst
#     x, y = y, x + y  # Update de waarden volgens de Fibonacci-logica
#     index -= 1  # Verminder de teller

# print(fib)

# def nth_fibonacci(n):
#     x, y = 0, 1  # Startwaarden
#     for _ in range(n):
#         x, y = y, x + y  # Update de waarden
#     return x

# # Voorbeeldgebruik
# n = int(input("Welke Fibonacci-term wil je? "))
# print(nth_fibonacci(n))


# while True:
#     print("Voer een getal in (of 'stop' om te stoppen): ", end="")
#     getal = input().lower
#     if getal == "stop":
#         print("Programma beeindigd")
#         break
#     elif int(getal) % 2 == 0:
#         print(f"Het getal {getal} is even")
        
#     else:
#         print(f"Het getal {getal} is oneven")


# #oneven met loop en stop
# while True:
#     getal = input("Voer een getal in (of 'stop' om te stoppen): ").lower()
    
#     if getal == "stop":
#         print("Programma beëindigd")
#         break
    
#     if getal.isdigit():  # Controleer of de invoer een geldig getal is
#         getal = int(getal)
#         if getal % 2 == 0:
#             print(f"Het getal {getal} is even.")
#         else:
#             print(f"Het getal {getal} is oneven.")
#     else:
#         print("Ongeldige invoer. Voer een geldig getal in of typ 'stop'.")

        
# print("Voer een lijst met getallen in, gescheiden door een komma: ", end="")
# invoer = input()
# lijst = invoer.split(",")

# try:
#     # Converteer elk item naar een getal en bereken de som
#     getallen = [float(number.strip()) number in lijst]  # Verwijder spaties en converteer
#     totaal = sum(getallen)
#     print(f"De som van de getallen is: {totaal}")
# except ValueError:
#     print("Ongeldige invoer. Zorg ervoor dat je alleen geldige getallen invoert, gescheiden door komma's.")

#grootste cijfers in een lijst vinden
# print("Geef een lijst in van cijfers, gescheiden door eem komma: ", end="")
# lijst = input().split(",")

# try:
#     cijfers = [float(getal.strip()) getal in lijst]
#     print(f"De lijst met cijfers: {cijfers}")
#     if not cijfers:
#         print("De lijst is leeg")
#     else:
#         grootste_cijfer = max(cijfers)
#         print(f"Het grootste getal in de reeks is {grootste_cijfer}")
# except ValueError:
#     print("Foute waarden ingegeven")

# print("Voer een aantal gehele getallen in, gescheiden door kommas': ", end="")
# lijst = input().split(",")

# try:
#     cijfers = [int(cijfer.strip()) for cijfer in lijst]
#     if not cijfers:
#         print("De lijst is leeg")
#     else:
#         gemiddelde = sum(cijfers) / len(cijfers)
#         print(f"Het gemiddelde van de cijfers is {int(gemiddelde)}")

# except ValueError:
#     print("De foute waarden werden ingegeven")

#palindroom
# print("Geef een woord in: ", end="")
# woord = input().lower()
# reverse = woord[::-1]

# if not woord:
#     print("Er werd geen woord ingegeven")
# elif woord.isdigit():
#     print("Er werd een cijfer ingegeven")

# else:
#     if woord == reverse:
#         print(f"{reverse} is een palindroom van {woord}")
#     else:
#         print("Dit is geen palindroom")


#gemeenschappelijke getallen vinden
# # Vraag de gebruiker om twee lijsten in te voeren
# print("Voer de eerste lijst in van getallen (gescheiden door komma's): ", end="")
# lijst1 = input().split(",")  # Eerste lijst
# print("Voer de tweede lijst in van getallen (gescheiden door komma's): ", end="")
# lijst2 = input().split(",")  # Tweede lijst

# # Verwijder spaties rondom getallen en zet ze om naar integers
# try:
#     set1 = set([int(getal.strip()) for getal in lijst1])
#     set2 = set([int(getal.strip()) for getal in lijst2])

#     # Zoek de gemeenschappelijke getallen
#     gemeenschappelijke_getallen = set1 & set2

#     # Toon de resultaten
#     if gemeenschappelijke_getallen:
#         print(f"Gemeenschappelijke getallen: {gemeenschappelijke_getallen}")
#     else:
#         print("Geen gemeenschappelijke getallen.")
# except ValueError:
#     print("Foute invoer. Zorg ervoor dat je alleen getallen invoert.")


#min en max getal
# print("Geef een lijst met getallen, gescheiden door komma's: ", end="")
# lijst = input().split(",")

# getallen = [int(getal) for getal in lijst]

# if not getallen:
#     print("De lijst is leeg")
# else: 
#     min = min(getallen)
#     max = max(getallen)

#     print(f"{min} is de kleinste waarde")
#     print(f"{max} is de grootste waarde")

# else:
#     print("Er werden niet numerieke waarden ingegeven")

print("Geef een lijst van getallen in: ", end="")
lijst = input().split(",")
getallen = [int(getal) for getal in lijst]
print(lijst)
wanted = int(input("Geef het cijfer waar je naar op zoek bent: "))
positie = getallen.index(wanted)

print(positie)

