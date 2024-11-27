
#we vragen 3 getallen en wijzen een variabele toe
print("We gaan het gemiddelde berekenen van 3 getallen.\n")
print("Geef het eerste getal in: ", end="")
getal1 = input()
print("Geef het tweede getal in: ", end="")
getal2 = input()
print("Geef het derde getal in: ", end="")
getal3 = input()

#om errors op te vangen werk ik met try en except
try:
    totaal = float(getal1) + float(getal2) + float(getal3) 
    gemiddelde = totaal / 3

    print(f"Het gemiddelde van {getal1}, {getal2} en {getal3} is {gemiddelde:.2f}")

except ValueError:
    print("De verkeerde waarden werden ingegeven. Geef alleen cijfers in.")
