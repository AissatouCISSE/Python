a = int(input("Entrer A :"))
b = int(input("Entrer B  :"))
c = int(input("Entrer C  :"))
A=[a,b,c]
print(A)
for i in range(0,len(A)-1):
    for j in range(1,len(A)):
        if A[i]>A[j]:
            e=A[i]
            A[i]=A[j]
            A[j]=e
print("les valeurs de A,B et C sont dans l’ordre:")
for i in range(len(A)):
    print(A[i])
print(A)