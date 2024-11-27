woord = str(input("Typ het woord dat je wilt controleren "))

frequentie = {}

for letter in woord:
    if letter in frequentie:
        frequentie[letter] += 1
    else:
        frequentie[letter] = 1

print("Frequentie van elke letter:")
for letter, count in frequentie.items():
    print(f"{letter}: {count}")