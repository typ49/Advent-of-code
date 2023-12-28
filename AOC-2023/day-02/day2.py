def parse_fichier_jeu(chemin_fichier, cubes_disponibles):
    """
    Parse le fichier de jeu et détermine les jeux possibles avec les cubes disponibles.

    Args:
    chemin_fichier (str): Chemin du fichier contenant les données des jeux.
    cubes_disponibles (dict): Dictionnaire contenant le nombre de cubes disponibles pour chaque couleur.

    Returns:
    int: Somme des identifiants des jeux possibles.
    """
    # Lire le fichier et extraire les données des jeux
    jeux = {}
    with open(chemin_fichier, 'r') as fichier:
        for ligne in fichier:
            if ligne.startswith("Game"):
                parts = ligne.strip().split(":")
                id_jeu = int(parts[0].split(" ")[1])
                jeux[id_jeu] = []
                sets = parts[1].split(";")
                for set in sets:
                    cubes = set.strip().split(", ")
                    for cube in cubes:
                        if cube:
                            nombre, couleur = cube.split(" ")
                            jeux[id_jeu].append((couleur, int(nombre)))

    def jeu_possible(jeu):
        """
        Find all the possible game and return the sum of their ID
        
        Args:
            (dictionary) jeu : a dictionary containing id and game
            
        Returns:
            True if "nombre" if lower or equal than "cube_diponibles[couleur]"
            False overwise
        """
        # Vérifier si un jeu est possible avec les cubes disponibles
        for couleur, nombre in jeu:
            if nombre > cubes_disponibles[couleur]:
                return False
        return True

    # Identifier les jeux possibles
    jeux_possibles = [id_jeu for id_jeu, jeu in jeux.items() if jeu_possible(jeu)]

    # Calculer la somme des identifiants des jeux possibles
    return sum(jeux_possibles)

# Exemple d'utilisation du script
chemin_fichier = './input.txt'  # Remplacer par le chemin du fichier réel
cubes_disponibles = {"red": 12, "green": 13, "blue": 14}

# Appel de la fonction
somme_jeux_possibles = parse_fichier_jeu(chemin_fichier, cubes_disponibles)
print(somme_jeux_possibles)
