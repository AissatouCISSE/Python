val = int(input("Entrer une valeur  :"))
som=0
i=1
while i<val:
    if val%i==0:
        som=som+i
    i=i+1
if som==val:
    print("le nombre " , val , " est parfait")
else:
    print("le nombre " , val , " n' est parfait")