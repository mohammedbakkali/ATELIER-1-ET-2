#exercice 1 / atelier 2  /////////////////////////
l1=[1,5,4,6,8,12,16]   
l2=[15,2,3,42,10,9,6]
l3=[]
for i in range(0,len(l1),2):
    l3.append(l1[i])
for i in range(1,len(l2),2):
    l3.append(l2[i])
print(l3)

