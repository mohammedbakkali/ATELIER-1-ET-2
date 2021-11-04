#exercice 1 / atelier 2  /////////////////////////
liste=[2,9,8,5,12,45,7,20,13,45,16,14,5,96,52,20]
l1=[]
l2=[]
l3=[]
a=int(len(liste)/3)
for i in range(a):
    l1.append(liste[i])
for i in range(a,a*2):
    l2.append(liste[i])
for i in range(a*2,(a*3)):
    l3.append(liste[i])        
l1.reverse()         
print(l1)
l2.reverse()
print(l2)
l3.reverse()
print(l3)
    
