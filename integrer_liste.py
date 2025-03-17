def integrer_liste(liste, pas):

#  Fonction pour calculer l'intégrale d'une liste de valeurs
#    en utilisant la méthode des rectangles.

 #   Arguments :
  #  liste -- Liste des valeurs à intégrer.
# pas -- Largeur de chaque rectangle 

   # Retourne : La valeur de l'intégrale.

    integrale = sum(liste) * pas
    return integrale


valeurs = [1, 2, 3, 4]  # Exemple de liste de valeurs
pas = 0.5  # Largeur de chaque rectangle
resultat = integrer_liste(valeurs, pas)

print(f"Valeur de l'intégrale : {resultat}")
