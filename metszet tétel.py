# Programozási tételek
# Metszet tétele

# Adott két tömb
# Közös elemeket válogassuk ki
# Válasz: azonos típusú elemekből álló tömb

import random
from collections import Counter
tömbA = []
tömbB = []
for index in range(0,random.randint(8,15)):
    tömbA.append(random.randint(1,10))
for index in range(0,random.randint(8,15)):
    tömbB.append(random.randint(1,10))

print("'A' tömb:")
print(*tömbA, sep=", ")
print("'B' tömb:")
print(*tömbB, sep=", ")

counter1 = Counter(tömbA)
counter2 = Counter(tömbB)
metszet = list((counter1 & counter2).elements())

# metszet = []
# for szám1 in tömbA:
#     for szám2 in tömbB:
#         if szám1 == szám2:
#             metszet.append(szám1)
#             break

print("Metszet:")
print(*metszet, sep=", ")