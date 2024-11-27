def productencatalogus():
    productencatalogus = {}

    while True:
        print("\nMaak hier uw keuze:")
        print("1. Voeg een nieuw product toe")
        print("2. Bekijk de prijs van een product")
        print("3. Wijzig de prijs van een product")
        print("4. Verwijder een product")
        print("5. Lijst alle producten op")
        print("6. Sluit het programma")

        keuze = int(input("Voer hier uw keuze in: "))

        if keuze == 1:
            naam_product = input("Wat is de naam van het product? ")
            prijs_product = float(input("Wat is de prijs van het product? "))

            if naam_product in productencatalogus:
                print("Dit product is reeds gekend")

            else:
                productencatalogus[naam_product] = prijs_product
                print("Het product werd toegevoegd aan de catalogus")

        elif keuze == 2:
            naam_product = input("Wat is de naam van het product? ")

            if naam_product in productencatalogus:
                print(f"De prijs van {naam_product} is {productencatalogus[naam_product]:.2f}")
            
            else:
                print("Dit product is niet gekend")

        elif keuze == 3:
            naam_product = input("Wat is de naam van het product? ")
            
            if naam_product in productencatalogus: 
                print(f"De huidige prijs van {naam_product} is {productencatalogus[naam_product]:.2f}")
                nieuwe_prijs = float(input("Geef de nieuwe prijs op "))               
                productencatalogus[naam_product] = nieuwe_prijs
                print(f"De nieuwe prijs van {naam_product} is {nieuwe_prijs}")

            else:
                print(f"{naam_product} is niet gekend")

        elif keuze == 4:
            naam_product = input("Geef de naam het het product dat je wenst te verwijderen: ")

            if naam_product in productencatalogus:
                del productencatalogus[naam_product]
                print(f"{naam_product} werd verwijderd")
            
            else:
                print(f"{naam_product} werd niet gevonden")

        elif keuze == 5:
            print("\nProducten en hun prijzen:")
            for product, prijs in productencatalogus.items():
                print(f"{product}: € {prijs:.2f}")

        elif keuze == 6:
            break
        
productencatalogus()