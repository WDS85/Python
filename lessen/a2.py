

########################***  Lists  ***############################### (())(())
###################################################################### (=o w o )('')


### Hoe lijsten opvullen, lijstvariabele naam = [waarden die je wil toekennen gesplitst door een ' , ' ]
### Hieronder zie je voorbeelden van lijsten.

#same_height_and_testscores = ["Sam",67,85.5,True]
#print(same_height_and_testscores)

#empty_list = []


############ Append #############
#################################
### De functie Append voegt achteraan de lijst een nieuwe waarde toe.
## Hieronder verschillende voorbeelden.

#append_example = ['this', 'is', 'an', 'example']
#append_example.append('list')
#print(append_example)

### Mogelijke werkwijze is 
### Lege lijst -> vraag data -> voeg toe aan lege lijst


#orders = ["Daisies", "Periwinkle"]
#orders.append("Tulips")
#orders.append("Roses")
#print(orders)


#mylist = [1, 2, 3]
#mynewlist = mylist + [4]
#print(mynewlist)


#########  Lijst Index ############
###################################
### De waarden van een lijst worden bewaard op een bepaalde index of positie, de posities starten vanaf 0, dus de eerste waarde (hieronder Juan) staat op positie 0.

#calls = ['Juan','Zofia','Amare','Ezio','Ananya']
#print(calls[0])

#studenten=['Jef','Bram','Joske','Marie']
#student_vier = studenten[3]
#print(student_vier)


################ vervangen van waarden in de lijst #####################
########################################################################
#### Er zijn een aantal manieren om waarden te wijzigen in een lijst.
### rechtstreekse index aanspreken. Je kies de positie in de lijst die je wil aanpassen en overschrijft de waarde rechtstreeks.
#garden=['Tomatoes','Green Beans', 'Cauliflower', 'Grapes']
#garden[2] = "Strawberries"
#print(garden)


#### remove ####
## Het verwijderen van een bepaalde waarde kan via de remove methode. Je geeft daarmee de waarde mee die je wil verwijderen. Als een waarde meermaals terugkomt, 
## zal het de waarde verwijderen met het laagste indexnummer (de eerst gevonden waarde).
#shopping_line = ['Cole','Kip','Chris', 'Sylvana']
#shopping_line.remove("Chris")
#print(shopping_line)

#### Insert ####
##insert - invoegen ve element op een specifieke positie
#store_line.insert(2,"Viktor")

#### Pop ####
##Pop - verwijderen ve element op een specifieke positie
#cs_topics.pop()

#### Range ####
## Een functie die een reeks ints in een lijst vorm zet.

#range(2,9,2) -> laatste 2 zijn sprongen
#myrange = range(10)
#print(list(myrange))

#### Len(gth) ####
## Len functie geeft de hoeveelheid waarden in een lijst terug, niet de waarden in de lijst zelf. 
#mylist = [1,2,3,4,5]
#print(len(mylist))

#big_range = range(2,3000,10)
#print(len(big_range))


#### Slicing ####
#################
### Met slicing geef je een bepaald deel weer van een lijst, afhankelijk van hoe je de slicing syntax gebruikt.

#letters=["a","b","c","d","e","f","g"]
#print(letters[2:6])

### Print tot de x'de positie
#print(letters[ : 3])
### Print vanaf de x'de positie
#print(letters[3: ])

### Print de posities zonder de laatste x posities
#print(letters[ :-1])
### Print de laatste x posities
#print(letters[-2: ])

#### Count ####
### count tel hoe vaak een waarde voorkomt
#letters = ["m","i","s"]
#num_i = letters.count("i")

#### Sorteren ####
### Sort methode
#lijst.sort

### Sort functie
#mylist=[c,a,b,b,e,g,e,s]
#sortedlist = sort(mylist)



##### Enkele oefeningen ######
##############################

### Voeg waarden toe aan een lege lijst. Verwijder de waarde op positie 2.
### Print hierna het resultaat.

#mylist=[]

#mylist.append(2)
#mylist.append(5)
#mylist.append(8)
#mylist.append(11)
#mylist.append(20)

#i=0
#j=0

#while i < 5:
#    j+=1
#    mylist.append(j)
##    print(mylist)
#    i+=1

#mylist.pop(2)
#print(mylist)


### Vul een naamlijst met de string Alice er tussen. Verwijder Alice hierna met de remove methode.
#namelist = ["Cheshire","Mad Hatter","Alice","Red Queen","Catterpillar","White Rabbit"]
#namelist.remove("Alice")
#print(namelist)


### Gebruikt sort om willekeurige getallen te sorteren.
#numbers = [11, 3, 7, 2, 1]
#numbers.sort()
#print(numbers)


### vul een legel ijst met een range. Verwijder de tweede positie, 
## voeg het getal 6 in op de eerste positie, verwijder het getal 2.
## Print hierna het resultaat.

#nummers = []
#nummers = list(range(1,6))
#nummers.pop(2)
#nummers.insert(1,6)
#nummers.remove(2)
#print(nummers)


#####  Oefening oneven/even check  #####
### doe een check in een lijst om na te kijken of een getal even of oneven is.
## Is het getal even, print dit dan als even en vise versa.


#CheckList = [11,20,3,4,50]

#i = 0

#while i<=4:
#    if CheckList[i]%2==0:
#        print("Even getal: ", CheckList[i])
#        i+=1
 #   else:
 #       print("Oneven getal: ", CheckList[i])
 #       i+=1

#i = 0

#while i<=4:
#    if CheckList[i]<10:
#        print("Kleiner dan 10: ", CheckList[i])
#        i+=1
#    else:
#        print("Groter dan 10: ", CheckList[i])
#        i+=1



###### Puntenlijst #######
#### Een puntenlijst word gegeven, voeg 84 toe, verwijder het getal 76, voet 91 toe op de 2de positie, en sorteer.
### Doe een controle, als het maximum van de lijst groter is dan 90, voeg dan 5 toe aan alle punten.
### bereken het gemiddelde van de punten, print die punten.
### Hierna geef je de mogelijkheid aan de gebruiker om het gemiddelde te raden en geef je weer of ze evt. correct zijn.

#Punten = [85,92,78,90,88,76,89,95,80]
#x = 0

#Punten.append(84)
#Punten.remove(76)
#Punten.insert(2,91)
#Punten.sort()

#if max(Punten)>90:
#    nieuwepunten = [x+5 for x in Punten]
#    average = sum(nieuwepunten)/len(nieuwepunten)
#    print(nieuwepunten)
#else:
#    print(Punten)
#    average = sum(Punten)/len(Punten)

#if input("Raad het gemiddelde : ") == average:
#    print("Je antwoord was correct!")
#else:
#    print("Verkeerd, het gemiddelde was: ", average)



######## Lussen / Loops #########
#################################
#### Loops worden gewoonlijk gebruikt om eenzelfde bewerking meermaals uit te voeren.
### Een controle dat moet blijven lopen tot het einde van een lijst van 100 componenten, 
### is lastig om te doen lijn per lijn.
### Soorten loops : - For, -While


###### For loop ######
### Deze bestaat uit het kernwoord voor, en word gelezen als, 
### Voor elk element x in een collectie, voer iets uit met dat element.
### Dit zorgt er voor dat voor de lengte van je waardelijst, de loop blijft lopen.

##for x in collection
##do x

#### Voorbeelden ####
### Een lijst met board games of sport games, deze bevat verschillende elementen in een list
## we willen alles afprinten, dus we loopen voor elk element in de lijst en printen alles af.

#board_games = ["Settlers of Catan", "Carcasonne", "Power Grid", "Agricola","Scrabble"]
#sport_games = ["football","hockey","baseball","cricket"]
#for i in board_games:
#    print(i)

#for i in sport_games:
#    print(i)

#### While loop ####
####################
### Met als kernwoord terwijl, word een while loop gebruikt met een mogelijk externe waarde.
### Word gelezen als : Terwijl een condition waar is, voer een actie uit.
### vb : Terwijl i < 5 , i+=1. Dus zolang variabele i onder 5 is, verhoog de waarde van i met 1.
### i is niet persee een element van een lijst.

##while condition :
##   action

### Hieronder een voorbeeld dat gebruik maakt van de lijst van vorige oefening.
## Eerst een korte kennismaking, print x zolang x kleiner is of gelijk is aan 3.
## daaronder, zolang de lengte van de lijst kleiner is dan x, print dan
## het element overeenstemmend met x, sinds x vergroot word in de loop, 
## zal het elke element doorlopen, tot het de waarde bereikt.


#x=0
#Lengthlist = len(board_games)

#while x <= 3:
#    #loop
#    print(x)
#    x+=1


#while x < Lengthlist:
#    print(board_games[x])
#    x+=1

#### BREAK ####
###############
### Een break is een manier om een loop te stoppen als een bepaalde gewenste of ongewenste waarde is bereikt.
### Dit kan er voor zorgen dat een programma nie crashed als het iets niet vind.
## Het bovenste voorbeeld is zonder break, het onderste is met.

#### Hieronder loopt een for loop een lijst door tot het een bepaald element vind en dan print het deze af.
#### Deze loop loopt door tot elk element is gelezen, ook na het element te hebben gevonden.
#items_on_sale = ["blue shirt","red shirt","jeans","dress","belt"]

#for item in items_on_sale:
#    if item == "dress":
#        print("found it")


#### In deze versie, stopt de loop als dit het element heeft gevonden.
### Dit bespaard je computer meer geheugen gebruik en loopt vlotter.

#print("Checking the sales list!")

#for item in items_on_sale:
#    print(item)
#    if item == "dress":
#        break

#print("end of search!")


#### CONTINUE ####
##################
### Ongelijk break dat de loop volledig stopzet, laat continue de loop voorlopen, 
## maar zal het bepaalde waarden overslaan.
## Dit hangt af van de conditie die daarvoor is opgestelt.
### Hieronder word elk getal dat kleiner of gelijk is aan 0 overgeslagen, 
## maar blijft de loop wel nog lopen tot het einde van de lijst.

#big_number_list = [-1, 0 , 2 , 9 , -2 , 3 , -5]

#for i in big_number_list:
#    if i <= 0:
#        continue
#    print(i)


###### Nesting ######
#####################
### Nesten van loops, of een loop in een loop, 
## soms kan je met 1 loop niet genoeg doen om iets te bereiken.
### Dit is het moment dat we nesten overwegen.


#### hieronder een voorbeeld van een loop in een loop.
### We hebben verschillende teams en we splitsen in de eerste loop 
## de teams op en daarachter een loop voor elke student.
### Als je tussendoor het team print, zie je de geschrevenl ijsten, 
## als je daarna de students print, krijg je een algemene lijst van alle studenten, in volgorde van de teams.

#project_teams = [["Ava", "Jesse", "James"],["Lucille", "Zed"],["Edgar", "Gabriel"]]

#for team in project_teams:
#    #print (team)
#    for student in team:
#        print(student)


#### bewerkingen met lijsten. ####
##################################
### Je kan natuurlijk wel meer doen met lijsten, zoals waarden aanpassen afhankelijk van situatie.
## hieronder een korte opdracht om de waarde van een lijst te verdubbelen.

#single_digits = [0,1,2,3,4,5,6,7,8,9] # of range(10)
#squares = []

#for x in single_digits:
#    squares.append(x*2)
#    print(x)

#print(squares)


#### hieronder een oefening om een bepaald patroon te maken met een loop.
### Ik heb hiervoor beide loops een keer gebruikt om aan te tonen hoe je beide kunt gebruiken.

#x = 0
#while x <= 5:
#    print("*"*x)
#    x+=1

#for i in range(1,6):
#    print('*'*i)


##################### Functies #######################
######################################################
#### Functies zijn voorgedefinieerde bewerkingen die we kunnen oproepen en zelfs een waarde met kunnen meegeven.
### Functies houden de code leesbaar & meer compact

### Vorm van een Functie ###  een functie begint altijd met defining,
##  dus ' def ' en daarachter de naam voor de funtie die je wil maken.

#def function_name():

### Hieronder zie je een functie dat een vaste waarde zal printen als het word opgeroept.
#def trip_welcome():
#    print("Welcome to Tripcademy!")
#    print("Let's get you to your destination.")

#trip_welcome()


##### Een functie kan natuurlijk meer dan vaste waarden weergeven, hieronder word een een controle gedaan
### Afhankelijk van meegegeven weer, zal het een ander antwoord printen.

#def weather_check(weather):
#    print("Weather Check:")
#    if weather == "sunny":
#        print("Het is een mooie dag om te reizen!")
#    elif weather == "rain":
#        print("Donkere wolken, voorzie jullie van een paraplu.")

#weather_check("sunny")
#weather_check("rain")


#### Je kan hierdoor ook een meer dynamisch antwoord vormen zoals het voorbeeld hieronder.
#def trip_welcome(destination):
#    print("welcome")
#    print("looks like you're going to " + destination + " today.")

#trip_welcome("Times Square")


##### Hieronder een oefening, er word input gevraagd aan de gebruiker 10 in totaal,
####  de code zal daarvan enkel de even getallen aangeven en daarna het gemiddelde berekenen.
#even_getallen = []
#x = 0
#while x < 10:
#    i = input()
#    if int(i) %2 == 0:
#        even_getallen.append(int(i))
#    x+=1
    
#print(even_getallen)
#print(sum(even_getallen)/len(even_getallen))

#### Er word een lijst opgemaakt van een aantal getallen, hieronder word een willekeurig getal 
## opgevraagd per positie in de lijst.
### Hierna word de lijst gebruikt om enkel even getallen toe te voegen aan de even_getal lijst.

#rand_list = []
#from random import randint
#for i in range(0,21):
#    x=randint(0,50)
#    rand_list.append(x)

#even_getallen = []
#for x in rand_list:
#    if x%2 == 0:
#        even_getallen.append(x)

#print(even_getallen)

##### Oefening van de les :
###schrijf een programma dat de even getallen telt tussen 1&20. gebruik een for-lus voor de eerste 10 getallen 
## en een while-lus voor de resterende 10 getallen.
## gebruik continue om de iteratie over te slaan als het getal deelbaar is door 3 & gebruik break om de lus te verlaten als het geal 17 is.

#### Dit heeft meerdere oplossingen, hieronder vind je mijn persoonlijk gevonden oplossing.

#even_getallen = range(0,20)

#i = 0

#for x in even_getallen:
#    if x < 20 and x > 10:
#        while x < 20 and x > 10:
#            if x == 17:
#                break  # Exit the while loop if x equals 17.
#            
#            elif x % 3 == 0:
#                break  # Skip adding if x is a multiple of 3
#            
#            elif x % 2 == 0:
#                i += x  # Add to i if x is even
#            x += 1  # Increment x
#            break
#                
#    elif x % 3 == 0:
#        continue  # Skip if x is a multiple of 3
#    elif x % 2 == 0:
#        i += x

#print("Final sum:", i)



###### De opdracht hieronder vraagt input van de gebruiker
#### Als de som van het getal kleiner blijft dan 100, blijft de loop input vragen.
### Hierachter print je het getal af.

#x = 0
#getal = 0
#counttotal = []

#while x <= 100:
#    getal = input("Gelieve een getal in te voeren ")
#    counttotal.append(getal)
#    x += int(getal)

#print(x)


#### Gebruik van reeds bestaande modules (lenen van bestaande bibliotheken.) ####

#### hieronder word een willekeurige lijst gemaakt via de rand functie.
### Daarna word de nummer 13 gezocht in de lijst en stopt de loop als deze word teruggevonden.
### Zo niet, word welk getal gewoon afgedrukt.

#rand_list = []
#from random import randint
#for i in range(0,10):
#    x=randint(1,20)
#    rand_list.append(x)

#for x in rand_list:
#    if x == 13:
#        print("Number 13 was found.")
#        break
#    print(x)

### Hieronder nog een klein stuk code dat filtert op waarde deelbaar door 4 en dan afdrukken van deze waarden.

#for i in range(1,16) :
#    if i%4:
#        i+=1
#        continue
#    else:
#        print(i)
#        i += 1


##for i in range(0,11):
##    if not i%2:
##        continue
##    else:
##            print(" "*(i),"*"*i)


##### Powershell en power automate #######
##########################################
### Zie cursus/PDF
## Power Automate = cloudservice van Microsoft
## GUI based, geen command pannel.


###### String Methodes ###########
##################################

### Aanpassen van schrijfwijze vd string
##print('Hello world'.upper())
##print('Hello world'.lower())
##print('Hello world'.title())
##print('Hello world'.format())

### Aanpassen van string, splitsen en samenvoegen
##print('Hello world'.split())
##print(''.join(['Hello', 'world']))

### Aanpassen van string, vervangen en wegnemen.
##print('Hello world'.replace([H,J]))
##print('Hello world'.strip())


############ Modules ##############
###################################


### from 'library/module' import 'object'
## > Voorbeeld datetime

##  ;) if you're bored 
### import turtle
### turtle.circle(50)


###import random
###random_list = [random.randint(1,100) for i in range (20)]

#### Oefening les 6 ####

#def to_uppercase(input_str):
    #print(input_str.upper())
    #return input_str.upper()


#to_uppercase(input("Geef een zin mee : \n"))
#print(to_uppercase(input"Geef een zin mee : \n"))


#######

#def countdown(beginget):
#    while beginget > 0:
#        print(beginget)
#        beginget-=1
#    print("lancering")
     
#countdown(5)



########

#def print_even_numbers(limiet):
#    setrange = range(0,limiet)
#    for x in setrange:
#        if not x%2 and x!=0:
#            print (x)

#print_even_numbers(10)


######


#def counttofifty():
#    newrange = range(1,51)
#    for x in newrange:
#        if not x%3 and not x%5:
#            print(x, " FizzBuzz")
#        elif not x%3:
#            print(x, " Fizz")
#        elif not x%5:
#            print(x, " Buzz")
#        else:
#            print(x)        

#counttofifty()



###########
### Omzetten met een input mogelijkheid

#def operation(een,twee,teken):
#    x = 0
#    if teken == "+":
#        x = float(een) + float(twee)
#        print(x)
#    elif teken == "-":
#        x = float(een) - float(twee)
#        print(x)
#    elif teken == "*" or teken == "x":
#        x = float(een) * float(twee)
#        print(x)
#    elif teken =="/":
#        x = float(een) / float(twee)
#        print(x)
#    else:
#        print("\n Please give a valid operator. \n")

#operation(input("Geeft het eerste getal in : \n"),input("Geef het tweede getal in : \n"),input("Geef een operator mee, '+','-'.'*' of '/' : \n"))

##################  Woordenboek  ########################
#########################################################
#woordenboek = {"Mountain": "Orod","Bread":"Bass","Friend":"Mellon","Horse":"Roch"}
#print(woordenboek["Friend"])

#### lege woordenboek
#empty_dict = {}

#### Waarde toevoegen
##dictionary[key] = value

#menu = {"oatmeal" : 4,"Carrot" : 5}
#menu["cheesecake"] = 8

#print(menu)

########## dieren in de zoo oefening ###########
################################################

#animals_in_zoo = {}
#animals_in_zoo["zebra's"] = 8
#animals_in_zoo["apen"] = 12
#animals_in_zoo["dinosaurussen"] = 0
#print(animals_in_zoo)



########  Update ########
#sensors = {'living room' : 21,'kitchen' : 23,'bedroom' : 20}
#sensors.update({'pantry':22, 'Guest Room' : 23,'Patio' : 34})
#print(sensors)



###### Waarden overschrijven ####
#menu = {"oatmeal" : 4,"Carrot" : 5}
#menu["oatmeal"] = 5
#print(menu)



########## woordenboeken combineren ##########
#names = {'Jenny','Alexus','Jerry','Sam'}
#heights = {61,70,67,64}

#students = {key:value for key, value in zip(names,heights)}
#print(students)

####  waarden oproepen/printen via sleutel ####
#print(students["Sam"])
#print(students["Jerry"])

######  .get() methode ####
## Dit voorkomt het script van stoppen als er een error is bij het inlezen van een key.

#print(students.get("Sam"))
#print(students.get("Rudy"))  ### Print None or meegegeven waarde, omdat dit niet in de lijst aanwezig is.
#print(students.get("Shanaya","Not found"))

### testlist = {"Found" : True,"Read" : False}

#########  .pop methode, waarde verwijderen #########
#print(students.pop("Jeremy","Wrong Name"))
#print(students)


######  Print(list(   woordenboek  ))  > geen keys #########

#punten = {"Jerry":4,"Milo":8,"Fray":6,"Jazz":9}

#for score in punten.values:
#    print(score)
#for student in punten.keys:
#    print(student)


#auto = {'Merk':"Toyota","Model":"Corolla","Jaar":2022,"Kleur":"Blauw"}
#x = auto.pop("Jaar",auto["Jaar"])
#y = auto.get("Brandstof","Niet gespecifieerd")

#print(auto)
#print(x)
#print(y)





