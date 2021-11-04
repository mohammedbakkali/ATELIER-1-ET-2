liste1=[10,50,65,12,85,330,78]
liste2=[]
my_dict={'simo':65,'soulaiman':78,"abdo":12}   #"key":"values"
for i in my_dict.values():              
    for j in range(len(liste1)):
        if i==liste1[j]:
            liste2.append(liste1[j])
print(liste2)  

# my_list = [] Les listes sont utilisées pour stocker des données de différents types de données de manière séquentielle.
# my_set={} Les Sets sont une collection d’éléments non ordonnés qui sont uniques.Les opérations sont également les mêmes qu’avec les ensembles arithmitique
# my_tuple=() Les tuples sont les mêmes que les listes, à l’exception du fait que les données une fois entrées dans le tuple ne peuvent pas être modifiées
# my_dic={"key":"values"} Les dictionnaires sont utilisés pour stocker les paires clé-valeur