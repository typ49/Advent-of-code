def day11_2(filepath):
    """
    Même problème que la partie 1, mais avec un univers beaucoup plus grand.
    Augmenter considérablement l'échelle de l'univers en remplaçant chaque ligne et chaque colonne vide
    par un million de lignes ou de colonnes vides respectivement.
    Cette expansion massive change drastiquement la taille de l'univers et la distance relative entre les galaxies.

    Args:
        filepath (str): Le chemin vers le fichier à lire.

    Returns:
        int: La somme des longueurs des plus courts chemins entre chaque paire de galaxies.
    """
    with open(filepath, 'r') as f:
        grid = f.read().splitlines()

    empty_rows = [r for r, row in enumerate(grid) if all(ch == "." for ch in row)]
    empty_cols = [c for c, col in enumerate(zip(*grid)) if all(ch == "." for ch in col)]

    points = [(r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "#"]

    total = 0
    scale = 1000000

    for i, (r1, c1) in enumerate(points):
        for (r2, c2) in points[:i]:
            for r in range(min(r1, r2), max(r1, r2)):
                total += scale if r in empty_rows else 1
            for c in range(min(c1, c2), max(c1, c2)):
                total += scale if c in empty_cols else 1

    return total

# main
filepath = "./input.txt"
print(day11_2(filepath))