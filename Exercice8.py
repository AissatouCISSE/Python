import math

a=int(input("Entrer la valeur de a : "))
while a==0:
    a = int(input("Entrer la valeur de a : "))
b=int(input("Entrer la valeur de b : "))
c=int(input("Entrer la valeur de c : "))
d=b*b-4*a*c
if d>0:
    x1 = (-b - math.sqrt(d)) / 2 * a
    x2 = (-b + math.sqrt(d)) / 2 * a
    print("les solutions sont :" ," x1 =" , x1 , " et  x2 = " , x2)
elif d==0:
    x1 =-b/2 * a
    print("la solution est : " + x1)
else:
    print("il n y  a pas de solutions")

