#exercice 3 / atelier 2  /////////////////////////
liste1=[2,5,6,3,3,6,9,8,5,1,2,20]
my_dict = {}
for i in range(len(liste1)):
    c=0
    for j in range(len(liste1)):
        if liste1[i]==liste1[j]:
            c=c+1
    my_dict[liste1[i]] =c
print(my_dict)   