#menu = {"toast": 6, "wortelsap": 5, "muffin": 2}
#begint en eindigt met {}
#elk item bestaat uit een sleutel en een waarde
#elk sleutel-waardepaar wordt gescheiden door een komma
#een lijst kan geen sleutel zijn, dan krijg je een typeError
#een dictionary kan ook leeg zijn

# eng_sin = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}

#waarde toevoegen via
#dictionary[key] = value

# menu = {"toast": 6, "wortelsap": 5, "muffin": 2}
# menu["cheesecake"] = 8
# print(menu)

#oefening1
# animals_in_zoo = {}
# animals_in_zoo["Zebras"] = 8
# animals_in_zoo["Apen"] = 12
# animals_in_zoo["Dinosaurussen"] = 0

# print(animals_in_zoo)

# #we kunnen verschillende toevoegen in 1 command .update()

# sensors = {"living room": 21, "kitchen": 20, "bedroom": 18}
# sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
# print(sensors)

#we kunnen een waarde overschrijven

# sensors["bedroom"] = 20
# print(sensors)

# #we kunnen van 2 lijsten 1 woordenboek maken
# names = ["Jenny", "Alexus", "Sam", "Grace"]
# heights = [61, 70, 67, 64]
# students = {key:value for key, value in zip(names, heights)}
# print(students)

#we kunnen waarden oproepen door de sleutel te geven
#sensors = {"living room": 21, "kitchen": 20, "bedroom": 18}
# print(sensors["bedroom"])
# print(sensors["kitchen"])
#als we een waarde zoeken die niet bestaat krijgen we een error
#print(sensors["garage"])
#via een .get() methode krijgen we geen foutmelding maar een none, waardoor het script verder gaat
# print(sensors.get("Garage"))
#we kunnen ook een waarde opgeven om te retourneren in plaats van none
# print(sensors.get("Garage", 0))
# print(sensors.get("Garage", "No value"))
# print(sensors.get("Garage", False))

#we kunnen .pop() gebruiken om waarden uit een woordenboek te halen, te returnen en meteen ook te verwijderen
# print(sensors.pop("living room"))
# print(sensors)

#we kunnen een lijst printen van een woordenboek
#print(list(sensors))

#we kunnen via .values() of .keys() de keys of values eruit halen
# for sensors in sensors.values():
#     print(sensors)

# auto = {"Merk": "Toyota", "Model": "Corolla", "Jaar": 2022, "Kleur": "Blauw"}
# #print(list(auto))
# auto.pop("Jaar")
# #print(list(auto))
# print(auto.get("Brandstof", "Niet gespecificeerd"))
# print(list(auto))
# print(auto.get("Jaar"), None)
# print(auto.get("Brandstof"))

# auto = {
#     "Merk": "Toyota",
#     "Model": "Corolla",
#     "Jaar": 2022,
#     "Kleur": "Blauw"
# }

# verwijderde_jaar = auto.pop("Jaar", None)

# brandstof = auto.get("Brandstof", "Niet gespecifieerd")

# print("Aangepaste dictionary", auto)
# print("Verwijderde auto")

#oefening

getallen = {'getal1': 5, 'getal2': 10, 'getal3': 15, 'getal4': 20, 'getal5': 25}

#getallen.pop('getal5')
getallen[-1].pop()
print(getallen)

print(getallen.get('getal5', 'Niet gevonden'))
