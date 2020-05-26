somme=0
rep=0
while ((somme <= 0) or rep != 0):
    prix=int(input("Entrer le prix : "))
    somme=somme+prix
    rep=int(input("Entrer 1 si vous voulez continuer sinon taper 0 : "))
print("La somme des articles est : " , somme , "CFA")