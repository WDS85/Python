def telefoonboek():

    telefoonboek = {}

    while True:
        try:            
                print("\nVoor een keuze in: ")
                print("1. Voeg een nieuw contact toe")
                print("2. Bekijk een contact")
                print("3. Wijzig een contact")
                print("4. Verwijder een contact")
                print("5. Lijst alle contacten op")
                print("6. Stop")

                keuze = int(input("Voer hier uw keuze: "))
                
                if keuze == 1:
                    naam = input("Voer een naam in: ")
                    nummer = input("Voer het nummer in: ")
                    telefoonboek[naam] = nummer
                    print(f"{naam} werd toegevoegd aan het boek met nummer {nummer}")

                elif keuze == 2:
                    naam = input("Voer een naam in: ")
                    
                    if naam in telefoonboek:
                        print(f"Het nummer van {naam} is {telefoonboek[naam]}")
                    
                    else:
                        print(f"{naam} is niet aanwezig in het boek")
                        
                elif keuze == 3:
                    while True:
                        print("\nVoor een keuze in: ")
                        print("1. Wijzig een naam")
                        print("2. Wijzig een nummer")
                        print("3. Terug naar het hoofdmenu")

                        sub_keuze = int(input("Voer uw keuze in: "))
                        
                        if sub_keuze == 1:
                            sub_naam = input("Geef de naam in die je wilt wijzigen: ")
                            nieuwe_naam = input("Geef de gewijzigde naam in: ")

                            if sub_naam in telefoonboek:
                                telefoonboek[nieuwe_naam] = telefoonboek.pop(sub_naam)
                            
                            else:
                                print(f"{sub_naam} is niet aanwezig in het boek")
                                
                                        
                        elif sub_keuze == 2:
                            sub_naam = input("Geef de naam in van de persoon die je wilt wijzigen: ")
                            print(f"{sub_naam} is gekend met het nummer {telefoonboek[sub_naam]}")
                            nieuw_nummer = input("Geef het nieuwe nummer in: ")
                            telefoonboek[sub_naam] = nieuw_nummer
                            print(f"{sub_naam} is nu gekoppeld met het nummer {nieuw_nummer}")

                        elif sub_keuze == 3:
                            break
                
                elif keuze == 4:
                    to_remove = input("Geef de naam in van het contact dat je wilt verwijderen: ")

                    if to_remove in telefoonboek:
                        del telefoonboek[to_remove]
                        print(f"{to_remove} werd verwijderd uit het telefoonboek")
                    
                    else:
                        print(f"{to_remove} is niet terug te vinden in contacten")

                elif keuze == 5:
                    if not telefoonboek:
                        print("Er zijn geen contacten in het telefoonboek")
                    else: 
                        for naam, nummer in telefoonboek.items():
                            print(f"{naam} is gekend met nummer {nummer}")

                elif keuze == 6:
                    break
                else:
                    print("Een verkeerde keuze werd gegeven. Kies een juiste waarde uit het menu")

        except ValueError:
            print("Er werd een verkeerde waarde ingegeven. Maak een keuze.")

telefoonboek()

