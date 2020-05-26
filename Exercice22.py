n = int(input("Veuillez saisir la taille de la séquence : (entre 10 et 50)"))
while(n <10 or n >50):
    n = int(input("Veuillez saisir la taille de la séquence : (entre 10 et 50)"))
print("n= ",n)
liste=[]
for i in range(1,n):
    nombre = int(input("Veuillez saisir un nombre : "))
    liste.append(nombre)
    while(i<1 or i> 100):
        nombre=int(input("Veuillez saisir un nombre : "))
print(liste)
longueur = 1
position = 0
longueur_i = 1
for i in range(len(liste)):
    if (liste[i] > liste[i - 1]) :
        longueur=longueur+1
    elif(longueur > longueur_i) :
        longueur_i = longueur
        position = i - longueur_i
        longueur = 1
    if(i==len(liste)-1):
        if (longueur > longueur_i):
            longueur_i = longueur
            position = (i - longueur_i)+1
print("La plus longue séquence est ")
i=position
for i in range((longueur_i + position)):
    print(liste[i])
print("qui débute à la position " , (position + 1));
print(" et elle est de longueur " , longueur_i);

