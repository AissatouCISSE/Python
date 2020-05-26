x = int(input("Entrer x :"))
n = int(input("Entrer n  :"))
#Version1:
puis=int(pow(x,n))
print("La puissance en version 1 est:", puis)
#Version2:
i=1
puissance=1
while i<=n:
    puissance=puissance*x
    i=i+1
print("La puissance en version 2 est:", puis)


