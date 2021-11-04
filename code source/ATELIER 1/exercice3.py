def sum(n):
    if n ==0:return 0
    return n+sum(n-1)
terme=int(input("donner le nombre de terme n "))
print(sum(terme))    