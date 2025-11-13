# Programozási tételek
# Maximum kiválasztás tétele

# Adott egy tömb
# A legnagyobb elem kiválasztása
# Válasz: egy elem

import random
számok = []
for index in range(0,25):
    számok.append(random.randint(1,1000))

print(*számok, sep=", ")

legnagyobb = számok[0]
for szám in számok:
    if legnagyobb < szám:
        legnagyobb = szám

print(f"legnagyobb érték: {legnagyobb}")