def calcul(n):
    if n==0:return 0
    return 1+calcul(n//10)

a=int(input("donne un nombre"))
print(calcul(a))


