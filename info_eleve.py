def obtenir_informations_eleve():
    # Création d'un dictionnaire avec les informations d'un élève
    eleve = {
        "nom": input("Entrez le nom de l'élève : "),
        "age": int(input("Entrez l'âge de l'élève : ")),
        "classe": input("Entrez la classe de l'élève : ")
    }
    return eleve

# Exemple d'utilisation
eleve_infos = obtenir_informations_eleve()
print("\nInformations sur l'élève :")
for cle, valeur in eleve_infos.items():
    print(f"{cle.capitalize()} : {valeur}")

