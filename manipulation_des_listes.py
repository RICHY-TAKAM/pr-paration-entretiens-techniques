def filtrer_nombres_pairs(liste):
    return [x for x in liste if x % 2 == 0]

liste_nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Nombres pairs :", filtrer_nombres_pairs(liste_nombres))



