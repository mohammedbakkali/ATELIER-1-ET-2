def binaire(b):
    f=1
    s=0
    while(b!=0):
        r=b%2
        s+=r*f
        f*=10
        b//=2
    return s
print(binaire(8))    
