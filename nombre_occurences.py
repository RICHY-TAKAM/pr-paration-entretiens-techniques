def nombre_occurences(liste, element):
    return liste.count(element)

liste_occurences = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
element_a_compter = 3
print(f"Occurrences de {element_a_compter} :", nombre_occurences(liste_occurences, element_a_compter))
