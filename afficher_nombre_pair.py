#1. Écrivez un programme qui affiche les nombres pairs de 1 à 10.
def afficher_nombres_pairs():
    pairs= []
    for i in range(1,11):
        if i % 2 == 0: 
            pairs.append(i)
    return pairs
            
resultat = afficher_nombres_pairs()
print (resultat)

#2. Écrivez une fonction qui prend une liste de nombres en entrée et retourne leur somme.
def somme_liste(liste):
    return (sum(liste))

nombres = [1, 2, 3, 4, 5, 6, 7, 8]
print (somme_liste(nombres))

#3. Écrivez un programme qui demande à l'utilisateur un mot et affiche ce mot en majuscules.

mot=input("veullez entrer un mot: ")
print (mot.upper()) 


        