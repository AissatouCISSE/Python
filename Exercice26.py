rep = 1
t = 0
maliste = []
while (rep == 1):
    n = int(input("Entrer une valeur: "))
    maliste.append(n)
    rep = int(input("taper 1 si vous voulez continuer à saisir: "))
    t = t + 1
print(maliste)
c = True
d = True
for i in range(1,len(maliste)):
    if maliste[i] > maliste[i - 1]:
        d = False
    else:
        c = False
    if c == False and d == False:
        print("quelconque")
        break

if c:
    print("Croissant")
if d:
    print("decroissant")

