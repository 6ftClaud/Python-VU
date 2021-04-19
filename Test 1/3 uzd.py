import collections

string = input("Iveskite simboliu seka: ")
# Input konvertuoja i int. Jei ivestis ne skaicius, praso ivesti is naujo
try:
    integer = int(input("Iveskite skaiciu: "))
except ValueError:
    integer = int(input("Tai ne skaicius, prasome ivesti is naujo: "))

# Jei visos salygos tinkamos, tesiama. Jei ne, script'as issijungs
if isinstance(integer, int) and integer > 0 and (len(string) % integer) == 0:
    pass
else:
    print("Kintamieji netinka")
    exit(1)

# Sudalija string i lygias dalis
parts = [string[i:i + integer] for i in range(0, len(string), integer)]

# Kiekviena dali patikrina ar nera duplikatu chars
for part in parts:
    print(''.join(collections.OrderedDict.fromkeys(part).keys()))
