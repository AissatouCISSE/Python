a = int(input("Entrer la valeur de a :"))
b = int(input("Entrer la valeur de b :"))
if(a<0):
    while(a<0):
        a = int(input("Entrer la valeur de a :"))
if(b<0):
    while(b<0):
        a = int(input("Entrer la valeur de b :"))
e=a
d = b
pgcd  = 0
resu = 0
while (a != b):
    if (b > a):
        c=a
        a=b
        b=c
    resu = a-b
    a =b
    b = resu
    pgcd = a
ppcm = e*d/pgcd;
print("le ppcm de " , e , " et " , d , " est : " , ppcm);