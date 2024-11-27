
#### Oefeningen

## Schrijf een programma dat de frequentie van elke letter in een opgegeven woord telt.

#newinput = input("Geef een woord : \n")
#searchletter = input("Geef een letter van het woord : \n")
#hvlhletters = newinput.count(searchletter)
#print("De hoeveelheid " , searchletter, "'s in het woord ", newinput, " is : ", hvlhletters, " keer.")



#test = "Testje"
#d={}
#for char in set(test):
#    d[char]=test.count(char)
#print(d)



#### oefening 2

## Schrijf een programma dat een eenvoudig winkelwagentje simuleert.
## De gebruiker moet items toevoegen aan het winkelwagentje met bijbehorende prijzen.
## Het programma moet het totqaalbedrag van de winkelwagen berekenen.


#nok = False
#winkelwagen = {}
#prijs = 0
#i = ""
#x = 0


#def Korting(winkelwagen):
#    korting = 0
#    newprice = 0
#    if sum(winkelwagen.values()) >= 50:
#        korting = sum(winkelwagen.values())*0.1
#        newprice = sum(winkelwagen.values()) - korting
#        print("Je totale rekening is : ", newprice)
#        print("Je genoot van ", round(korting), " euro korting.")
#    else:
#        print("Je totale rekening is : ", sum(winkelwagen.values()))


#while nok != True:
#    print("De volgende producten zijn beschikbaar, gelieve hieruit te kiezen: \n Appel, banaan en peer \n Ben je klaar schrijf OK")
#    print("Bekijk je mandje type : toon")
#    print("Wens je je mandje leeg te maken type : R \n")
#    print("Wens je iets te verwijderen type : D \n ")

#    i = input("Gelieve een product toe te voegen : \n")
#    if i == "OK":
#        print(winkelwagen)
#        break
#    else:
#        if i == "appel" or i == "Appel":
#            prijs = 10
#            winkelwagen[i,x]=prijs
#            x+=1
#        elif i == "peer" or i == "Peer":
#            prijs = 12
#            winkelwagen[i,x]=prijs
#            x+=1
#        elif i == "banaan" or i =="Banaan":
#            prijs = 8
#            winkelwagen[i,x]=prijs
#            x+=1
#        elif i == "D":
#            print("Je huidige winkelwagen : ", winkelwagen)
#            j = input("vul hier het product in dat je wenst te verwijderen: \n ")
#            winkelwagen.pop(j,"")
#        elif i == "toon":
#            print(winkelwagen)
#        elif i == "R":
#            winkelwagen = {}
#        prijs = 0
#Korting(winkelwagen)


#### bouw een winkelwagentje waarin items en prijzen worden opgeslagen.
### Voeg een functie toe waarmee een korting van 10% wordt toegepast op het taaltbedrag als de waarde meer dan 50 euro is.






#### Schrijf een programma dat een willekeurig wachtwoord genereert op basis van opgegeven criteria
## zoals de lengte en gebruik van hoofdletters, cijfers en speciale tekens.     interessante site voor string() -> https://pynative.com/python-generate-random-string/

#from random import randint

#print("Please type in length of password minimal 8 : \n")
#inp = int(input())

#if inp < 8:
#    print("password length to short.")
#elif inp >= 8:
#    x = inp

#print("Please type in if you'd like uppercase or not Y/N ?")
#x = False
#inp2 = input()
#if inp2 == "Y":
#    x = True
#else:
#    x = False

#print("Please type in if you'd like numerics or not Y/N?")
#y = False
#inp3 = input()
#if inp3 == "Y":
#    y = True
#else:
#    y = False

#print("Please type in if you'd like special characters or not Y/N?")
#z = False
#inp4 = input()
#if inp4 == "Y":
#    z = True
#else:
#    z = False    




##### oef flowchart
###  teken een flowchart die een proces beschrijft waarbij een gebruiker hun
###  huidige leeftijd invoert en het aantal jaren berekent tot hun pensioen.
## uitgaande van 67 jaar, Voeg beslispunten toe voor uitzonderingen
## Zoals negatieve leeftijden of leeftijden boven 67 jaar.



#### Laat de gebruiker een getal raden tussen 1 en 100. Het programma geeft aan of
## Het getal hoger of lager is dan het geheime getal. Dit herhaalt zich tot he tjuiste getal wordt geraden.

#from random import randint
#i = randint(1,20)
#j = 0

#while int(j) != i:
#    j = input("Raad het getal: ")
#    if int(j) != i :
#        if int(j) < i:
#            print("Het getal dat je zoekt is groter. probeer opnieuw")
#        elif int(j) > i:
#            print("Het getal dat je zoekt is kleiner. probeer opnieuw")
#        else:
#            continue
#    if int(j) == i :
#        print("Goed geraden, het getal was :", i , "!")
#        break






#### Schrijf een programma dat een eenvoudig koffiebestelsysteem simuleert.
## Gebruikers moeten hun favorieten koffie kunnen bestellen met verschillende opties.

#booly = False
#additielst = ""
#koffielijst=["Machiatto","Mokka","Latte","Esspresso","Koffie Verkeerd"]
#addities = ["Ahorn Siroop","Cacao","Extra Suiker","Extra Melk","Hazelnoot Siroop"]
#keuzes = []

#print("Hallo, hierbij ons koffiemenu: \n1 Machiatto\n2 Mokka\n3 Latte\n4 Esspresso\n5 verkeerd\nOm te bestellen, geef je naam en je keuze in: \n")

#naam = str(input("Naam:"))
#koffie = int(input("Koffie:"))

#while booly == False:
#    print("Enige additionele opties bij je koffie?\n1 Ahorn syroop\n2 Cacao\n3 Extra suiker\n4 Extra melk\n5 Hazelnoot syroop\nType 'OK' als u klaar bent.")
#    addi = input("Kies je optie:")

#    if addi == "OK":
#        booly = True
#    else:
#        try:
#            addi = int(addi)
#            if 1 <= addi <= 5:
#                keuzes.append(addi)
#            else:
#                print("Kies een getal tussen 1 en 5, of 'OK' om klaar te zijn.")
#        except ValueError:
#            print("Ongeldige invoer, probeer het opnieuw.")
# Verwerk de gekozen addities
#for x in keuzes:
#    additielst += addities[x-1] + ", "

# Verwijder de laatste komma en spatie
#additielst = additielst.strip(", ")#

#koffies = koffielijst[koffie-1]
#print(naam, "Jouw keuze was : \n", koffies, "met", additielst)




#### *Genereer willekeurige tafelsommen (bvb 6x7)
#### *Laat de gebruiker antwoorden
#### *Alt het antwoord juis is, zeg "Correct!"
#### *Bij een fout antwoord, zeg "Helaas, het juiste antwoord is x" (laat de gebruiker eerst 5x gokken)
#### *Na 6 pogingen geef je het antwoord weer.


#from random import randint
#counter = 0
#a = randint(1,20)
#b = randint(1,20)

#c = a+b
#print(c)
#som = "Antwoord op de volgende som : ", a,"+",b,"= ? \n"

#while counter <5: 
#    userinput = input(som)
##    print(c)
#    print(userinput)
#    if int(userinput) != c:
#        print("Je antwoord was verkeerd, je hebt nog", 5-counter,"pogingen over \n")
#        counter +=1
#    elif int(userinput) == c:
#        print("Correct!")
#        break
#if counter >= 5:
#    "Helaas, het juiste antwoord is ", c,







#### Schrijf een eenvoudig tekstavonturenspel waarbij de spelen keuzes moet 
### maken die het verloop van het verhaal beinvloeden.























