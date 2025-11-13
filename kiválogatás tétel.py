# Programozási tételek
# Kiválogatás tétele

# Adott egy tömb
# Bizonyos feltételek mentén ki kell belőle válogatni elemeket.
# Válasz: azonos típusú elemekből álló tömb

import random
számok = []
for index in range(0,15):
    számok.append(random.randint(1,10))

print(*számok, sep=", ")

# Válogassuk ki a páratlan számokat
cél = []
for szám in számok:
    if szám % 2 == 1:
        cél.append(szám)

print(*cél, sep=", ")
