woord = str(input("Typ hier het woord dat je wilt controleren "))

droow = ''.join(reversed(woord))

if woord == droow:
    print(f"{droow} is een palindroom van {woord}")
else:
    print("Dit is geen palindroom")
# print(droow)

