A=[]
for i in range(10):
    n=int(input("Entrer la valeur de n"))
    A.append(n)
print(A)
max=A[0]
for i in range(0,len(A)):
    if A[i] >=max:
        max = A[i]
        pos=i
print("le plus grand de ces 10 nombres est " , max , " et il est la position " , pos)