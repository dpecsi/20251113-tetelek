# Programozási tételek
# Kiválogatás tétele

# Adott egy tömb
# Bizonyos feltételek mentén ki kell belőle válogatni elemeket
#  az egyik válasz tömbbe, az összes többi érték a másik válasz tömbbe kerül.
# Válasz: 2db azonos típusú elemekből álló tömb

import random
számok = []
for index in range(0,15):
    számok.append(random.randint(1,10))

print(*számok, sep=", ")

# Válogassuk szét az 5-nél kisebb és az 5-el egyenlő vagy annál nagyobb számokat
cél_kisebbmint5 = []
cél_nagyobbegyenlomint5 = []
for szám in számok:
    if szám < 5:
        cél_kisebbmint5.append(szám)
    else:
        cél_nagyobbegyenlomint5.append(szám)

print("Kisebb mint 5:")
print(*cél_kisebbmint5, sep=", ")
print("Nagyobb egyenlő mint 5:")
print(*cél_nagyobbegyenlomint5, sep=", ")
