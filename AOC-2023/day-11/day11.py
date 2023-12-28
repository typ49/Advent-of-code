def day11(filepath):
    """
    Déterminer la somme des longueurs des plus courts chemins entre chaque paire de galaxies dans une image de l'univers.
    Les galaxies sont représentées par le symbole #, et l'espace vide par le point (.).
    L'univers subit une expansion cosmique,
    ce qui signifie que toute ligne ou colonne sans galaxies doit être considérée comme ayant une taille double.

    Args:
        filepath (str): Le chemin vers le fichier à lire.

    Returns:
        int: La somme des longueurs des plus courts chemins entre chaque paire de galaxies.
    """
    with open(filepath, 'r') as f:
        grid = f.read().splitlines()

    empty_rows = [r for r, row in enumerate(grid) if all(ch == "." for ch in row)] # all the row with only dots
    empty_cols = [c for c, col in enumerate(zip(*grid)) if all(ch == "." for ch in col)] # all the col with only dots

    points = [(r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "#"] # all the galaxy points

    total = 0
    scale = 2

    for i, (r1, c1) in enumerate(points):
        for (r2, c2) in points[:i]:
            for r in range(min(r1, r2), max(r1, r2)):
                total += scale if r in empty_rows else 1
            for c in range(min(c1, c2), max(c1, c2)):
                total += scale if c in empty_cols else 1

    return total

# main
filepath = "./input.txt"
print(day11(filepath))