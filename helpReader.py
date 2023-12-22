# Code Python simplifié pour lire un fichier texte sans gestion poussée d'erreur

def lire_fichier_texte(chemin_du_fichier):
    """
    Lit le contenu d'un fichier texte.

    Args:
    chemin_du_fichier (str): Le chemin vers le fichier à lire.

    Returns:
    str: Le contenu du fichier.
    """
    # Ouverture du fichier en mode lecture et lecture de son contenu
    with open(chemin_du_fichier, 'r', encoding='utf-8') as fichier:
        contenu = fichier.read()
        return contenu

# Exemple d'utilisation de la fonction
# chemin_du_fichier = "chemin/vers/le/fichier.txt"
# contenu_du_fichier = lire_fichier_texte(chemin_du_fichier)
# print(contenu_du_fichier)


# Code Python pour lire des fichiers structurés sous forme de matrice et de liste

def lire_fichier_matrice(chemin_du_fichier):
    """
    Lit un fichier structuré sous forme de matrice.

    Args:
    chemin_du_fichier (str): Le chemin vers le fichier à lire.

    Returns:
    list: Une liste de listes représentant la matrice.
    """
    matrice = []
    with open(chemin_du_fichier, 'r', encoding='utf-8') as fichier:
        for ligne in fichier:
            # Diviser chaque ligne en éléments et les ajouter à la matrice
            matrice.append(ligne.strip().split())
    return matrice

def lire_fichier_liste(chemin_du_fichier):
    """
    Lit un fichier structuré sous forme de liste.

    Args:
    chemin_du_fichier (str): Le chemin vers le fichier à lire.

    Returns:
    list: La liste des éléments du fichier.
    """
    liste = []
    with open(chemin_du_fichier, 'r', encoding='utf-8') as fichier:
        for ligne in fichier:
            # Ajouter chaque ligne à la liste
            liste.append(ligne.strip())
    return liste

# Exemples d'utilisation des fonctions
# chemin_matrice = "chemin/vers/le/fichier_matrice.txt"
# matrice = lire_fichier_matrice(chemin_matrice)
# print(matrice)

# chemin_liste = "chemin/vers/le/fichier_liste.txt"
# liste = lire_fichier_liste(chemin_liste)
# print(liste)



# Code Python pour parser un fichier avec une fonction universelle et paramétrable

def parser_fichier(chemin_du_fichier, delimiteur=' ', ignorer_lignes=0, colonnes_a_inclure=None, convertir_en_types=None):
    """
    Parse un fichier avec des options spécifiques pour le rendre aussi universel que possible.

    Args:
    chemin_du_fichier (str): Le chemin vers le fichier à parser.
    delimiteur (str, optional): Le caractère utilisé pour séparer les éléments dans le fichier. Par défaut, il s'agit d'un espace.
    ignorer_lignes (int, optional): Le nombre de lignes à ignorer au début du fichier. Par défaut, aucune ligne n'est ignorée.
    colonnes_a_inclure (list, optional): Liste des indices des colonnes à inclure. Par défaut, toutes les colonnes sont incluses.
    convertir_en_types (list, optional): Liste des types auxquels convertir chaque colonne. Par exemple, [int, float, str]. Par défaut, aucune conversion n'est effectuée.

    Returns:
    list: Une liste de listes représentant les données parsées.
    """
    donnees_parsees = []
    with open(chemin_du_fichier, 'r', encoding='utf-8') as fichier:
        for _ in range(ignorer_lignes):
            next(fichier)  # Ignorer les lignes initiales

        for ligne in fichier:
            elements = ligne.strip().split(delimiteur)
            
            # Sélectionner uniquement les colonnes spécifiées
            if colonnes_a_inclure:
                elements = [elements[i] for i in colonnes_a_inclure]

            # Convertir les éléments dans les types spécifiés
            if convertir_en_types:
                elements = [convertir_en_types[i](element) for i, element in enumerate(elements)]

            donnees_parsees.append(elements)

    return donnees_parsees

# Exemple d'utilisation de la fonction
# chemin_du_fichier = "chemin/vers/le/fichier.txt"
# donnees = parser_fichier(chemin_du_fichier, delimiteur=',', ignorer_lignes=1, colonnes_a_inclure=[0, 2], convertir_en_types=[int, str])
# print(donnees)
