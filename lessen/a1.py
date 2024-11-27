
###########*** Logica  ***############
######################################

########### Leren werken met print, strings, variabelen ###############
#######################################################################
## Variabele = een naamgevind die je geeft voor een bepaalde waarde, dit kan vanalles zijn, in ons voorbeeld een 'string' of woord.
## Verwijder bij de toepassingen hieronder de #'s om ze te testen.


## Variabele = x, met waarde Alice
## Je print in je Terminal de uitkomst met de waarde achteraan.

# x = "Alice"
# print("Mijn naam is : ",x)

## Variabele = Begroetinsbericht, je print enkel de waarde in de variabele.

#begroetingsBericht = "Goede morgen, deze morgen"
#print(begroetingsBericht)


## In dit voorbeeld zal python een foutmelding geven, er mag geen enter zitten tussen de lijnen.

### Fouten in code:
#print('goocheltrucje, 
#      dit is een spreuk")
#print(abracadabra)



######*** Werken met Integers en Floats  ***#######
###################################################
## Een integer is een cijfer, een geheel getal.
## Een float is een kommagetal.


##Dit kort voorbeeld toont je de uitkomst afhankelijk van variabele keuze.
#an_int = 2
#a_float = 2.13
#sum = an_int + 3

#print(sum)
#print(a_float + 2)


###oefening 1
## Deze oefening toont simpel de uitkomsten in de Terminal.

#release_year = 2
#runtime = 4
#rating_out_of_10 = 6.7

#print(release_year)
#print(runtime)
#print(rating_out_of_10)  


##Concatenate of samenvoegen, zoals de naam aangeeft zal een string aan een andere string hangen. ! als je een cijfer wil toevoegen moet je dit omzetten als een string.
##Concatenate [+]
#a = "De les"
#b = "is leuk"

#print(a+" "+b)


## Plus equals is een korte manier om een waarde aan een bestaande waarde toe te voegen. Je originele waarde staat links.
##Plus equals [+=]
#a = 10
#print(a)

#a = a + 2
#print(a)

#a += 2
#print(a)


##Voorbeeldje voor bewerkingen in variabelen & strings printen.
## Halveer je leeftijd in variabele my_age en sla deze op in de variabele half_my_age, Geef een greeting & je naam in een string variabele.
## Gebruik de variabele om een zin te vormen, print achteraf half je leeftijd en de zin af in de Terminal.

#my_age = 30
#half_my_age = my_age / 2

#greeting = "Hellow"
#name = "Alice"

#greeting_with_name = greeting + " " + name

#print(half_my_age)
#print(greeting_with_name)


##Als je text onder elkaar wil printen, is dit een manier om dat de doen.
#ditismijnvariabele = """
#Dit
#is
#mijn
#text """
#print(ditismijnvariabele)



#######*** Conditionals & Operators ***#########
################################################
### Info over mijn notities : <>  staat voor: is anders dan / niet gelijk aan.

## Conditionals of voorwaardelijkheden, zijn een voorwaarde dat je geeft aan je variabelen. Deze gaan meestal samen met booleans.
## Een boolean kan je zien als : aan of uit, 1 of 0, TRUE of FALSE en Ja of Nee. 
## Dit is altijd een waarde dat aangeeft dat de code iets al dan niet mag doen/uitvoeren.
### Klein voorbeeldje :      1 is groter dan 2   Boolean = Nee    |    1 > 2   ->   Boolean = False
## Operators, zijn de tekens die gebruikt worden bij vergelijkingen of bewerkingen, zoals >= , ++ of * .


## voorbeeldje van de les: 
## string 7 gelijk aan nummer 7 ?   |   nummer 2 NIET gelijk aan 4
## vergelijking 1 is vals, zeven <> 7
## vergelijking 2 is waar, 2 <> 4 

#print('7'==7, 2 != 4)



### Je kan een boolean op voorhand al zetten zoals je wil, zie wel dat je niet de string gebruikt. om dit tegen te gaan gebruiken we de type() functie.
## Hieronder zie je twee mogelijke manieren, check ze gerust even uit.

#my_baby_bool = "true"
#print (type(my_baby_bool))

#my_baby_bool_two = True
#print(type(my_baby_bool_two))


### IF & ELSE ####
##################
## Zoals de naam kan aangeven, ga je een ALS toevoegen aan je vraagstelling. Als een getal groter is dan, laat mijn code x doen.
## ELSE of Elif, als de ALS voorwaarde niet word vervult, kan je een elif of else toevoegen die zegt wat de code dan wel moet uitvoeren in de plaats.
## Als je dit niet doet, gaat je programma niets doen.

### Oefening: Gebruik van IF/ELSE als iemand anders dan 'DAVE' op een computer zou inloggen. De Terminal zou afhankelijk van je user_name 1 van de 2 zinnen moeten printen.
#user_name = ""
#if user_name == "Dave":
#    print("Get off my computer Dave!")
#else:
#    print("Welcome back.")



### controle op waarde, gelijke waarden. Als we enkel '=' gebruiken, zetten we een variabele naar een waarde, dus x = 1 maakt van de variabele x een 1.
### Voor de conditional '==' Vragen we echter, kijk of de linkerkant van deze bewerking gelijk is met de rechterkant. Dus als we zeggen : 2 == 2, krijgen we een boolean van TRUE terug.
## Hieronder kan je een oefeningetje zien waar je met twee variabele kunt spelen om dit te kunnen zien.
#x=20
#y=20
#if x == y:
#    print("getallen zijn gelijk")


## In deze oefening kijk je na of je voldoende credits zou hebben als je minimum 120 nodig hebt. 
## Pas de credits variabele aan en je zal zien dat je geen print krijgt in de terminal als het getal te laag is.
#credits = 120
#if credits >= 120:
#    print("Je hebt genoeg credits")


####### AND en OR en NOT ###########
####################################
### De conditionals And & Or of vertaalt, en & of, zoals het kan gelezen worden zullen nakijken of meerdere of een enkele voorwaarden worden voldaan.

### De AND conditional, zal voorwaarden nakijken en zal enkel de code gebruiken als alle voorwaarden worden voldaan. 
### VB : 1 == 1 AND 2 > 3   , Booleans lezen -> true en false.   Omdat de AND conditional enkel werkt als alles true is, zal de code niet doorgaan.
### De OR conditional, zal voorwaarden nakijken en gebruikt code als er minstens 1 true word teruggegeven.
### VB : 1 == 1 OR  2 > 3   , Booleans lezen -> true en false.   Er is minstens 1 true, de de opvolende code zal uitgevoerd worden.

### De NOT conditional is een speciaal geval. Deze veranderd een boolean naar zijn tegenpool, zoals je een lichtknop zou schakelen.
### Als een boolean true zou zijn en je plaats er de NOT conditional voor, zal deze false zijn in de plaats.


### Een beetje ingewikkelder, hieronder hebben we 2 variabelen.
### we kijken na met gebruik van AND of OR, om te zien wat de uitkomst is van de boolean in de Terminal.
#x = 20
#y = 20

#wantedvalue = 20
#if x == wantedvalue and y == wantedvalue:
#    print("x en y zijn beide waar")

#if x == wantedvalue or y== wantedvalue:
#    print("x of y is waar")

#if not (x == wantedvalue or y == wantedvalue):
#    print("de not operator veranderd een false")




### Dit zijn een paar kleine voorbeeldjes voor boolean werking te leren kennen met And en Or.
#first = (1+1 == 2) and (2+2 == 4)
#second = (1>9) and (5 != 6)
#third = (1+1 == 2) and (2<1)
#fourth = (0 == 10) and (1+1 == 1)
#print(first, second, third, fourth)

#first = (True or True)
#second=(True or False)
#third=(False or True)
#fourth=(False or False)
#print(first, second, third, fourth)


### Kort voorbeeldje van een voorgmaakte boolean, als je een if direct laat weten of het true of false is, zit de 'vraag' er al in verwerkt.
### Dus hieronder zie je gewoon 'if weekday' wat anders zou zijn 'if weekday == True'. 
### Maar nu geef je gewoon mee dat de waarde TRUE is en schiet de code direct in de IF.

#weekday = True

#if weekday:
#    print("wake up at 6:30")
#else:
#    print("sleep in")


#### Een voorbeeldje dat toont dat je volgorde in een if / else structuur veel uitmaakt.\
### Als je 1 van de lagere punten eerst zet, zal de uitkomst van je code niet meer kloppen.
### Test dit gerust uit :) .

#grade = 82

#if grade >= 90:
#    print("A")
#elif grade >= 80:
#    print("B")
#elif grade >= 70:
#    print("C")
#elif grade >= 60:
#    print("D")
#else: print("F")


#######*** Bewerkingen en getalmanipulatie (Operators) ***#########
#######################################################
### Je kent waarschijnlijk wel wat shortcuts van de calculator app? Wel deze zijn hetzelfde voor python. 
### Voor een som gebruik je + , verschil een - , een deling gebruik je / en voor vermenigvuldiging een * .
### Deze staan hieronder ook mooi onder elkaar geschreven.

#a = 4
#b = 2

#sum = a+b
#dif = a-b
#dev = a/b
#multi = a*b


#print(sum)
#print(dif)
#print(dev)
#print(multi)


##########  INPUT  ###############
##################################
### Input is noodzakelijk voor een groot deel programma's, we vragen de 'gebruiker' om ons iets te geven om te manipuleren. 
### Of dit een woord, zin of getal is, moeten wij hen duidelijk maken.

### hieronder vragen we een naam aan de gebruiker en hiernaasst ook nog gewicht en lengte, we gebruiken de functie 'input()', 
### tussen de haken kan je een vraag stellen aan de gebruiken die ze in de Terminal te zien krijgen.
### Het is ook daar dat ze input kunnen invullen om in de code te gebruiken.

#naam = input("wat is je naam?")
#print(naam)

#kg = int(input("Wat is je gewicht?"))
#cm = int(input("Wat is je lengte"))

#print(kg/cm)



##############  De % Operator  #################
###################################################
### Dit is een operator dat nakijkt of een getal al dan niet deelbaar is door het gekozen getal. 
### vb : x%2  -> is x deelbaar door 2 en houdt dit een geheel getal over.
### Hieronder zie je de verwerkte bewerking, maar ipv een restberekening kan je ook een %2 gebruiken om te zien of een getal al dan niet even is. Misschien vindt jij dit wel terug?
### Test het even uit.

#x = 11

#getal = x/2
#rest = getal - int(getal)

#print(getal*2)

#if rest != 0:
#    print("getal is oneven")
#else:
#    print("getal is even")



####  Een oefening op bewerkingen met gebruik van input. je vraagt kg en cm en berekent een BMI.

#kg = float(input("Wat is je gewicht in kg?"))
#cm = float(input("wat is je lengte in cm?"))

#cm = cm/100
#BMI = kg/cm*cm

#print(BMI)


#### Korte bewerking die graden naar fahrenheit omzet.

#graden = float(input("Hoeveel graden celcius?"))
#Fahr = (graden*9/5)+32

#print(Fahr)