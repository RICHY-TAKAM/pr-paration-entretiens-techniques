#Conversion de types o Demande à l'utilisateur d'entrer son âge et vérifie si c'est bien un entier. Si c'est un entier, affiche "Vous avez X ans", sinon, affiche un message d'erreur.#
age = input("Entrez votre âge : ")
try:
    age = int(age)
    print(f"Vous avez {age} ans.")
except ValueError:
    print("Erreur : Ce n'est pas un entier valide.")
