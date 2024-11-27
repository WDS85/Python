#we vragen om het getal
print("Geef het getal in waarbij we de multiplicatietafel gaan uitvoeren: ", end="")
getal = input()
#we werken met try en except om errors op te vangen
try:
    
    for i in range(1, 11):
        getal = int(getal)
        som = getal * i
        print(f"{getal} x {i} = {som}")

except ValueError:
    print("Er werd een verkeerde waarde ingegeven. Geef een getal in.")