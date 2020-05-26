j = int(input("Entrer le jour  :"))
m = int(input("Entrer le mois  :"))
a = int(input("Entrer l'annee :"))
if((j<1 or j>31) or (m<1 or m>12) or(m==2 and j>29 and a%4==0)or(j>28 and a%4!=0) or(a<1583)):
    print("La date est incorrecte")
elif ((a % 4 == 0 and a % 100 != 0) or a % 400 == 0):
    print("l'annee est bissextile  ")
else:
    print("La date n'est pas bisextille ")