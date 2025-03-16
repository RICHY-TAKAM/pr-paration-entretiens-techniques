#une fonction pour calculer le nombre de voyelles dans un mot
#definir une fonction get_vowels_numbers(mot)
#creer un compteur de voyelles 
#pour chaque lettre du mot, verifier s'il s'agit d'un voyelle, si c'est le cas, on ajoute 1 au compteur
#a la fin de la fonction, vous allez renvoyer le compteur. 

def get_vowels_numbers(word):
    # créer un compteur de voyelles
    nb_vowels = 0

    # pour chaque lettre du mot vous verifiez s'il s'agit d'un voyelle
    for letter in word:
        if letter in ['a', 'e', 'i', 'o', 'u', 'y']:
            # on ajoute un au compteur
            nb_vowels += 1

    # à la fin de la fonction, vous allez renvoyer le compteur
    return nb_vowels


word = input("Entrer un mot")
vowels_count = get_vowels_numbers(word)
print("Il y a", vowels_count, "voyelles dans le mot", word) 

