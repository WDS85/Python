import random
import string


def genereer_wachtwoord(lengte, hoofdletters, cijfers, speciale_tekens):
    # Basis tekenset (kleine letters)
    tekenset = string.ascii_lowercase

    # Voeg hoofdletters, cijfers en speciale tekens toe op basis van de criteria
    if hoofdletters:
        tekenset += string.ascii_uppercase
    if cijfers:
        tekenset += string.digits
    if speciale_tekens:
        tekenset += string.punctuation

    # Controleer of de tekenset niet leeg is
    if not tekenset:
        print("Geen tekens opgegeven om het wachtwoord te genereren.")
        return None

    # Genereer het wachtwoord
    wachtwoord = ''.join(random.choice(tekenset) for _ in range(lengte))
    return wachtwoord


# Invoer van de gebruiker
print("Willekeurige Wachtwoordgenerator")
try:
    lengte = int(input("Voer de lengte van het wachtwoord in: "))
    hoofdletters = input("Wil je hoofdletters gebruiken? (ja/nee): ").lower() == "ja"
    cijfers = input("Wil je cijfers gebruiken? (ja/nee): ").lower() == "ja"
    speciale_tekens = input("Wil je speciale tekens gebruiken? (ja/nee): ").lower() == "ja"

    # Genereer en toon het wachtwoord
    wachtwoord = genereer_wachtwoord(lengte, hoofdletters, cijfers, speciale_tekens)
    if wachtwoord:
        print(f"Je gegenereerde wachtwoord is: {wachtwoord}")
except ValueError:
    print("Voer een geldig getal in voor de lengte.")