# Fonction récursive pour calculer la factorielle
def factorielle(n):
    if n == 0 or n == 1:  # Cas de base : la factorielle de 0 ou 1 est 1
        return 1
    else:
        return n * factorielle(n - 1)  # Appel récursif

nombre = int(input("Entrez un nombre entier : "))
print(f"La factorielle de {nombre} est : {factorielle(nombre)}")

