import random

# numbers = random.sample(range(1, 100), 5)
# for i in numbers:
#     if i % 2 == 0:
#         print(f"Het getal {i} is even")
#     else:
#         print(f"Het getal {i} is oneven")

# num = random.randint(1, 100)

# rekening = float(input("Wat is het bedrag? "))
# aantal_mensen = int(input("Hoeveel mensen betalen mee? "))
# fooi = float(input("Hoeveel fooi moet er voorzien worden? 0 voor geen fooi"))

# if fooi > 0:
#     rekening += rekening * (fooi /100)
#     print(f"Er zal een fooi voorzien worden van {fooi}%")
# else:
#     print("Er zal geen fooi voorzien worden")

# if aantal_mensen == 0:
#     print("Het aantal mensen moet groter zijn dan 0")
# else:
#     bedrag_per_persoon = rekening / aantal_mensen
#     print(f"Ieder persoon moet {bedrag_per_persoon} betalen")

# def calculator():
#     x = float(input("Wat is het eerste getal? "))
#     y = float(input("Wat is het tweede getal? "))
#     n = input("Wat is de operator ?")

#     if n == "+":
#         result = x + y
#     elif n == "-":
#         result = x - y
#     elif n == "*":
#         result = x * y
#     elif n == "/":
#         result = x / y
#     else:
#         print("De verkeerde operator werd gebruikt")
#     print(f"{x} {n} {y} = {result}")

# calculator()

# def even_of_oneven():
#     n = int(input("Geef een getal in "))

#     if n % 2 == 0:
#         print(f"Het getal {n} is even")
#     else:
#         print(f"Het getal {n} is oneven")

# even_of_oneven()

# def gemiddelde():
#     a = float(input("Voer het eerste getal in "))
#     b = float(input("Voer het tweede getal in "))
#     c = float(input("Voer het derde getal in "))

#     gemid = (a + b + c) / 3

#     print(f"Het gemiddelde van {a}, {b} en {c} is {gemid:.0f}")

# gemiddelde()

def contactenbeheer():

    contacten = {}

    while True:
        print("\nVoor een keuze in: ")
        print("1: Voeg een nieuw contact toe")
        print("2: Bekijk een contact")
        print("3: Wijzig een contact")
        print("4: Verwijder een contact")
        print("5: Stop")

        keuze = int(input("Voer hier uw keuze: "))
        
        if keuze == 1:
            naam = input("Voer een naam in: ")
            nummer = input("Voer het nummer in: ")
            contacten[naam] = nummer
            print(f"{naam} werd toegevoegd aan het boek met nummer {nummer}")

        elif keuze == 2:
            naam = input("Voer een naam in: ")
            
            if naam in contacten:
                print(f"Het nummer van {naam} is {contacten[naam]}")
            
            else:
                print(f"{naam} is niet aanwezig in het boek")
                
        elif keuze == 3:
            while True:
             print("\nVoor een keuze in: ")
             print("1: Wijzig een naam")
             print("2: Wijzig een nummer")
             print("3. Terug naar het hoofdmenu")

             sub_keuze = int(input("Voer uw keuze in "))
             
             if sub_keuze == 1:
                sub_naam = input("Geef de naam in die je wilt wijzigen")
                nieuwe_naam = input("Geef de gewijzigde naam in")

                if sub_naam in contacten:
                    contacten[nieuwe_naam] = contacten.pop(sub_naam)
                
                else:
                    print(f"{sub_naam} is niet aanwezig in het boek")
                                
             elif sub_keuze == 2:
                sub_naam = input("Geef de naam in van de persoon die je wilt wijzigen")
                print(f"{sub_naam} is gekend met het nummer {contacten[sub_naam]}")
                nieuw_nummer = input("Geef het nieuwe nummer in")
                contacten[sub_naam] = nieuw_nummer
                print(f"{sub_naam} is nu gekoppeld met het nummer {nieuw_nummer}")

             elif sub_keuze == 3:
                break
        
        elif keuze == 4:
            to_remove = input("Geef de naam in van het contact dat je wilt verwijderen ")

            if to_remove in contacten:
                del contacten[to_remove]
                print(f"{to_remove} werd verwijderd uit het boek")
            
            else:
                print(f"{to_remove} is niet terug te vinden in contacten")
                                  
        elif keuze == 5:
            break

contactenbeheer()


