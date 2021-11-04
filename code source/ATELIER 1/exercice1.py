def fact(n):
    if n==0: return 1
    return n*fact(n-1)

terme=int(input("donner le nombre de terme"))
s=0
for i in range(1,terme+1):
    s=s+fact(i)/i
print(s)    
