def day14(filepath):
    with open(filepath, 'r') as f:
    # Lecture de la grille à partir du fichier et division en lignes.
        grid = f.read().splitlines()

    # Transposition de la grille pour échanger lignes et colonnes.
    grid = list(map("".join, zip(*grid)))

    # Traitement de chaque ligne (maintenant colonne) de la grille :
    # - Division en groupes séparés par '#'.
    # - Tri de chaque groupe en ordre décroissant.
    # - Réassemblage des groupes séparés par '#'.
    grid = [
        "#".join(
            ["".join(sorted(list(group), reverse=True)) for group in row.split("#")]
        ) for row in grid
    ]

    # Transposition de retour pour revenir à l'orientation originale.
    grid = list(map("".join, zip(*grid)))

    # Calcul et affichage du score total :
    # - Pour chaque ligne, compte le nombre d'occurrences de 'O'.
    # - Multiplie ce nombre par la distance de la ligne par rapport au bas de la grille.
    # - Additionne les résultats de toutes les lignes pour obtenir le score total.
    total_score = sum(row.count("O") * (len(grid) - r) for r, row in enumerate(grid))
    return total_score

# main
filepath = "./input.txt"
print(day14(filepath))
