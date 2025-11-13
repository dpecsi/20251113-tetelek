# Programozási tételek
# Rendezés tétele

# Adott egy tömb
# rendezzük növekvő sorrendbe
# Válasz: azonos típusú elemekből álló és elemszámú tömb

import random
számok = []
for index in range(0,25):
    számok.append(random.randint(1,1000))

print(*számok, sep=", ")

elemszám = len(számok)
for i in range(0, elemszám):
    minIndex = i
    for j in range(i, elemszám):
        if számok[j] < számok[minIndex]:
            minIndex = j
    tmp = számok[i]
    számok[i] = számok[minIndex]
    számok[minIndex] = tmp

print(*számok, sep=", ")