def compter_voyelles(chaine):
    """Compte le nombre de voyelles dans une chaîne, en ignorant la casse."""
    voyelles = "aeiouyAEIOUY"
    return sum(1 for char in chaine if char in voyelles)

texte = "vous allez bien?"
print("Nombre de voyelles :", compter_voyelles(texte))