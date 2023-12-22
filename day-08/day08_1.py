def parser(chemin_du_fichier):
    """
    Parse un fichier pour le problème Advent of Code.

    Args:
    chemin_du_fichier (str): Le chemin vers le fichier à parser.

    Returns:
    tuple: Une chaîne de caractères représentant les instructions de navigation et un dictionnaire représentant le réseau de noeuds.
    """
    with open(chemin_du_fichier, 'r', encoding='utf-8') as fichier:
        lignes = fichier.readlines()

    # Supposons que la première ligne contient les instructions de navigation
    instructions_navigation = lignes[0].strip()

    # Parse le réseau de noeuds
    reseau_noeuds = {}
    for ligne in lignes[1:]:
        noeud, voisins = ligne.strip().split(' = ')
        voisins = tuple(voisins.strip('()').split(', '))
        reseau_noeuds[noeud] = voisins

    return instructions_navigation, reseau_noeuds

########################################################################################################################
# main

chemin_du_fichier = "./day08.txt"
instructions, reseau = parser(chemin_du_fichier)
