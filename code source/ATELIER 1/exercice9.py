#Python n'a pas de type intégré pour les matrices. Cependant, nous pouvons traiter une liste de liste comme une matrice.
def position(T,x):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if x==M[i][j]:
                pi=i
                pj=j
                return pi,pj
        

M = [ [3, 1, 5], [9, 8, -1], [10, 12, 2] ]
x=int(input("cherche un élément : "))
a=position(M,x)
print("la position (i,j) de  ",x,"dans la matric est ",a)

           