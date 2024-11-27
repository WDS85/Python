#we vragen de gebruiker een aantal cijfers in te geven
print("Geef een reeks cijfers in, gescheiden door een komma: ", end="")
cijfers = input().split(",")
#try en except om fouten op te vangen
try:
    cijfers = [int(cijfer.strip()) for cijfer in cijfers]


    hoogste_cijfer = max(cijfers)
    laagste_cijfer = min(cijfers)
    som_cijfers = sum(cijfers)

    print(f"\nHet hoogste cijfer van de reeks is {hoogste_cijfer}")
    print(f"Het laagste cijfer van de reeks is {laagste_cijfer}")
    print(f"De som van de reeks is {som_cijfers}\n")

except ValueError:
    print("De verkeerde waarde werd ingegeven")

    

