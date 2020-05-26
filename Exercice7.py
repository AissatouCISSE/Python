montant=int(input("Entrer le montant à décomposer : "))
b20 = int(montant / 20)
reste = montant%20
b10 = int(reste / 10)
reste = reste%10
b5 = int(reste / 5)
reste = reste%5
p2 = int(reste / 2)
reste = reste%2
p1 = int(reste)
print("le montant " , montant, " contient ",b20," billets de 20 ",b10," billets de 10 ",b5," billets de 5 ",p2," pièces de 2 et ",p1," pièces de 1 ")