punten = [85, 92, 78, 90, 88, 76, 89, 95, 80]
punten.append(84)
print(punten)
punten.remove(76)
print(punten)
punten.insert(2, 91)
print(punten)
# sort = sorted(punten)
# print(sort)
punten.sort()
print(punten)
#count = sum(punten) / len(punten)
count = punten[0] + punten[1] + punten[2] + punten[3] + punten[4] + punten[5] + punten[6] + punten[7] + punten[8] + punten[9] 
gemiddelde = count/10
print(gemiddelde)
if punten[-1] > 90:
#    print(punten[0]+5)
#    print(punten[1]+5)
    plus = [punten[0]+5,punten[1]+5,punten[2]+5,punten[3]+5,punten[4]+5,punten[5]+5,punten[6]+5,punten[7]+5,punten[8]+5,punten[9]+5]
print(plus)
count_plus = plus[0] + plus[1] + plus[2] + plus[3] + plus[4] + plus[5] + plus[6] + plus[7] + plus[8] + plus[9]
gemiddelde_plus = count_plus/10

guess = float(input('Wat is het gemiddelde?'))

if guess == gemiddelde_plus:
    print('Correct, proficiat')
else:
    print('Verkeerd, jammer')


