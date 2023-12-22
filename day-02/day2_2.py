def parse_fichier_jeu_minimum_cubes(chemin_fichier):
    """
    Parse le fichier de jeu et calcule le minimum de cubes nécessaires pour chaque couleur dans chaque jeu et leur puissance.

    Args:
    chemin_fichier (str): Chemin du fichier contenant les données des jeux.

    Returns:
    dict: Dictionnaire contenant le minimum de cubes pour chaque couleur et leur puissance pour chaque jeu.
    int: Somme des puissances de tous les jeux.
    """
    jeux = {}
    with open(chemin_fichier, 'r') as fichier: # ouvre le fichier en mode lecture
        for ligne in fichier: # pour chaque ligne dans le fichier
            if ligne.startswith("Game"): # si la ligne commence par "Game"
                parts = ligne.strip().split(":") # on enlève les espaces et on sépare la ligne en deux parties
                id_jeu = int(parts[0].split(" ")[1]) # on récupère l'id du jeu
                jeux[id_jeu] = [] # on crée une liste vide pour les tirages
                sets = parts[1].split(";") # on récupère les tirages
                for set in sets: # pour chaque tirage
                    cubes = set.strip().split(", ") # on enlève les espaces et on sépare le tirage en cubes
                    for cube in cubes: # pour chaque cube
                        if cube: # si le cube n'est pas vide
                            nombre, couleur = cube.split(" ") # on récupère le nombre et la couleur
                            jeux[id_jeu].append((couleur, int(nombre))) # on ajoute le cube au tirage

    def calculer_minimum_et_puissance(jeu):
        min_cubes = {"red": 0, "green": 0, "blue": 0} # on initialise le minimum de cubes à 0 pour chaque couleur
        for couleur, nombre in jeu: # pour chaque cube dans le tirage
            min_cubes[couleur] = max(min_cubes[couleur], nombre) # on met à jour le minimum de cubes pour la couleur
        puissance = min_cubes["red"] * min_cubes["green"] * min_cubes["blue"] # on calcule la puissance du jeu
        return min_cubes, puissance # on retourne le minimum de cubes et la puissance

    minimum_cubes_par_jeu = {} # on initialise le dictionnaire des minimums de cubes par jeu
    somme_puissances = 0 # on initialise la somme des puissances

    for id_jeu, tirages in jeux.items(): # pour chaque jeu
        min_cubes, puissance = calculer_minimum_et_puissance(tirages) # on calcule le minimum de cubes et la puissance
        minimum_cubes_par_jeu[id_jeu] = min_cubes # on ajoute le minimum de cubes au dictionnaire
        somme_puissances += puissance # on ajoute la puissance à la somme

    return minimum_cubes_par_jeu, somme_puissances # on retourne le dictionnaire et la somme

# Exemple d'utilisation du script
chemin_fichier = './day2.txt'

# Appel de la fonction
minimum_cubes_par_jeu, somme_puissances = parse_fichier_jeu_minimum_cubes(chemin_fichier)
print(somme_puissances)