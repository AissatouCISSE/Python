import math

x1 = int(input("Entrer x1 :"))
y1 = int(input("Entrer y1 :"))
x2 = int(input("Entrer x2 :"))
y2 = int(input("Entrer y2 :"))
d2 = 2*(y1-y2);
d1 = 2*(x2-x1);
res=d1+d2;
d=math.sqrt(res)
print("la distance entre les deux points est:", d)