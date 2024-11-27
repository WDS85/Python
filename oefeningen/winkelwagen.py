print("Welkom bij onze winkel")

winkelwagen = {}

while True:
    print("\nMaak een keuze:")
    print("1. Voeg een product toe")
    print("2. Verwijder een product")
    print("3. Toon de inoud van uw winkelwagen")
    print("4. Bereken het totaal en betaal")

    keuze = int(input("Voor uw keuze in: "))

    if keuze == 1:
        item = str(input("Welk product wilt u toevoegen? "))
        prijs = float(input("Wat is de prijs "))

        winkelwagen[item] = prijs

        print(f"{item} werd toegevoegd aan de winkelwagen met een prijs van €{prijs}")

    if keuze == 2:
        te_verwijderen = str(input("Welk item wilt u verwijderen? "))

        if te_verwijderen in winkelwagen:
            del winkelwagen[te_verwijderen]
            print(f"{te_verwijderen} werd verwijderd")

        else:
            print(f"{te_verwijderen} werd niet teruggevonden in de winkelwagen")

    if keuze == 3:
        for item, prijs in winkelwagen.items():
            print(f"{item}: {prijs}")

    if keuze == 4:
        totaal = sum(winkelwagen.values())

        print(f"Het totaal van u boodschappen is € {totaal}")

    elif keuze == 0 or keuze > 4:
        print("Ongeldige invoer")
        





