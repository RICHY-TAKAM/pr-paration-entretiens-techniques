def calculer_moyenne_generale(notes):
    """
    Calcule la moyenne générale d'une salle de classe.
    
    Paramètres :
    notes (list) : Liste des notes des élèves (float ou int).
    
    Retourne :
    float : Moyenne générale de la classe.
    """
    if not notes:
        return 0  # Retourne 0 si la liste est vide

    moyenne = sum(notes) / len(notes)
    return moyenne


notes_classe = [12.5, 14, 16, 9, 11.5, 17, 13]
moyenne_generale = calculer_moyenne_generale(notes_classe)
print(f"La moyenne générale de la classe est : {moyenne_generale:}")
