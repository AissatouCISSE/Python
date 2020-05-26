#Version1
r1 = float(input("Entrer R1 :"))
r2 = float(input("Entrer R2  :"))
r3 = float(input("Entrer R3  :"))
Rser=r1+r2+r3
Rpar=(r1*r2*r3)/(r1*r2+r1*r3+r2*r3)
print("La résistance en série est ", Rser)
print("La résistance en parallele est ", Rpar)

#Version2
choix = int(input("Entrer Votre choix 1 ou 2 ?"))
if choix==1:
    print("La résistance en série est ", Rser)
else:
    print("La résistance en parallele est ", Rpar)