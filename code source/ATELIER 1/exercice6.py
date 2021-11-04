#exercice 6
#tri a bulle
def tri_bulle(tableau):
    permutation = True
    c = 0
    while permutation == True:
        permutation = False
        c = c + 1
        for i in range(0, len(tableau) - c):
            if tableau[i] > tableau[i + 1]:
                permutation = True
                tableau[i], tableau[i + 1] = tableau[i + 1],tableau[i]
    return tableau

from array import *
t = array('i', [1,2,8,0,3,9,8])
print(tri_bulle(t))

#tri par selection 
def tri_selection(tab):
    for i in range(len(tab)):

        min = i

        for j in range(i + 1, len(tab)):
            if tab[min] > tab[j]:
                min = j

        tmp = tab[i]
        tab[i] = tab[min]
        tab[min] = tmp

    return tab

#tri par insertion
def tri_insertion(tab):
    for i in range(1, len(tab)):
        k = tab[i]
        j = i-1
        while j >= 0 and k < tab[j] :
                tab[j + 1] = tab[j]
                j -= 1
        tab[j + 1] = k
    return tab



