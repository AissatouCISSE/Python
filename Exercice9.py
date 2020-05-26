#A. On considère que le départ et l'arrivé ont lieu le même jour

h1=int(input("entrer horaire de départ : h "))
m1=int(input("entrer horaire de départ : min "))
h2=int(input("entrer horaire d'arriver : h2 "))
m2=int(input("entrer horaire d'arriver : min2 "))
md1 = (h2*60+m2)
md2 = (h1*60+m1)
md = md1-md2
hd = md/60
md = md%60
print("la durée de vol est : ",hd, "h:",md,"mn")

#B. On suppose que la durée de vol est inférieure à 24 heures mais peut avoir lieu le lendemain.

if h2>h1:
    if m2>m1:
        hd = h2-h1
        md = m2-m1
        print("la duree de vol est : ",hd, "h:",md,"mn")
    else:
        hd = h2-h1-1
        md = m2+60-m1
        print("la duree de vol est : ",hd, "h:",md,"mn")
else:
    if m2 > m1:
        hd = h2-h1+24
        md = m2-m1
        print("la duree de vol est : ",hd, "h:",md,"mn")
    else:
        hd = h2 - h1 + 24 - 1
        md = m2 + 60 - m1
        print("la duree de vol est : ",hd, "h:",md,"mn")