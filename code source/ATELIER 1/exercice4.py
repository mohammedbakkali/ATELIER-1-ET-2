def Fibonacci(n):
    if n==1 or n==0 :return n
    return Fibonacci(n-1)+Fibonacci(n-2)
a=int(input("donner un terme "))    
for i in range(a):
    print(Fibonacci(i))