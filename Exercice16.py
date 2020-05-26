a = int(input("Entrer la valeur de a :"))
b = int(input("Entrer la valeur de b :"))
r=0
q=0
while(a>=b):
    r=a-b
    a=r
    q=q+1
print("le quotient est ",q, " et le reste est ",r);