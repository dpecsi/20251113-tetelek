# Programozási tételek
# Metszet tétele

# Adott két tömb
# Az összes elemet rakjuk egy közös tömbbe
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

unió = list(tömbA)

unió.extend(tömbB)

# for szám2 in tömbB:
#     unió.append(szám2)

print("Unió:")
print(*unió, sep=", ")

# ha nem engedjük meg az ismétlődést
tömbA = set(tömbA)
tömbB = set(tömbB)

print("'A' tömb:")
print(*tömbA, sep=", ")
print("'B' tömb:")
print(*tömbB, sep=", ")

unió = []
for szám1 in tömbA:
    unió.append(szám1)

for szám2 in tömbB:
    bennevan = False
    for segéd in unió:
        if segéd == szám2:
            bennevan = True
    if bennevan == False:
        unió.append(szám2)

print("Unió:")
print(*unió, sep=", ")