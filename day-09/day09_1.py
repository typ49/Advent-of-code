def lire_fichier_matrice(chemin_du_fichier, type):
    """
    Lit un fichier structuré sous forme de matrice.

    Args:
    chemin_du_fichier (str): Le chemin vers le fichier à lire.
    type (str): Le type de la matrice à lire.

    Returns:
    list: Une liste de listes représentant la matrice.
    """
    matrice = []
    with open(chemin_du_fichier, 'r', encoding='utf-8') as fichier:
        for ligne in fichier:
            if type == "int":
                # Diviser chaque ligne en éléments et les ajouter à la matrice
                matrice.append([int(x) for x in ligne.strip().split()])
            else:
                matrice.append(ligne.strip().split())
    return matrice

def nextList(liste):
    """
    retourne une liste avec pour element x = (n+1 - n), n étant un element de la liste

    Args:
    liste (list): liste d'entiers

    Returns:
    list: liste d'entiers
    """
    res = []
    for i in range(len(liste)-1):
        res.append(liste[i+1] - liste[i])
    return res

def listOfNextList(list):
    """
    retourne une liste de liste avec pour element x = (n+1 - n), n étant un element de la liste jusqu'as ce que la liste soit rempli de 0
    exemple : [[0, 3, 6, 9, 12, 15], [3, 3, 3, 3, 3], [0, 0, 0]]
    
    Args:
    list (list): liste d'entiers
    
    Returns:
    list: liste de liste d'entiers
    """
    list = [list]
    while True:
        list.append(nextList(list[-1]))
        if all(x == 0 for x in list[-1]):
            list.pop()
            break
    return list

def findNextNumber(liste):
    """
    trouve la suite logique de la liste à l'index 0 de liste
    exemple : [[0, 3, 6, 9, 12, 15, A], [3, 3, 3, 3, 3, B], [0, 0, 0, C]]
    C = 0, B = 3+C = 3+0 = 3, A = 15+B = 15+3 = 18
    
    Args:
    liste (list): liste de liste d'entiers
    
    Returns:
    int: le prochain nombre de la suite logique
    """
    return sum(list[0]) + liste[1][-1]

def sumOfNextNumber(matrix):
    res = 0
    for i in range(len(matrix)):
        res += findNextNumber(listOfNextList(matrix[i]))
    return res

# main
matrix = lire_fichier_matrice("day09.txt", "int")
res = sumOfNextNumber(matrix)
print(res)