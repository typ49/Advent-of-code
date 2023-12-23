import sys
import multiprocessing

def lire_fichier_matrice(chemin_du_fichier):
    with open(chemin_du_fichier, 'r', encoding='utf-8') as fichier:
        return [list(ligne.strip()) for ligne in fichier]

import time

def longest_hike(matrix, start_pos, end_pos):
    rows, cols = len(matrix), len(matrix[0])
    max_length = 0
    visited = [[False] * cols for _ in range(rows)]
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    last_print_time = time.time()

    def backtrack(x, y, path_length):
        nonlocal max_length, last_print_time
        current_time = time.time()

        if current_time - last_print_time > 30:  # Imprimer toutes les secondes
            print(f"Exploring: ({x}, {y}), Path length: {path_length}, Max length: {max_length}")
            last_print_time = current_time

        if (x, y) == end_pos:
            max_length = max(max_length, path_length)
            return

        visited[x][y] = True
        for dx, dy in directions:
            next_x, next_y = x + dx, y + dy
            if 0 <= next_x < rows and 0 <= next_y < cols and matrix[next_x][next_y] != '#' and not visited[next_x][next_y]:
                backtrack(next_x, next_y, path_length + 1)
        visited[x][y] = False

    backtrack(*start_pos, 0)
    return max_length


def parallel_longest_hike(matrix, start_pos, end_pos):
    # Diviser la grille en régions et lancer des processus parallèles pour chacune
    # Cette partie dépend de la manière dont vous souhaitez diviser la grille
    # Pour l'exemple, on suppose qu'il y a plusieurs points de départ
    start_points = [start_pos]  # Exemple, devrait être une liste de points de départ

    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = [pool.apply_async(longest_hike, (matrix, start, end_pos)) for start in start_points]
        max_lengths = [res.get() for res in results]

    return max(max_lengths)

def day23(filepath):
    matrix = lire_fichier_matrice(filepath)
    start_pos = next(((i, j) for i, row in enumerate(matrix) for j, val in enumerate(row) if i == 0 and val == '.'), None)
    end_pos = next(((i, j) for i, row in enumerate(matrix) for j, val in enumerate(row) if i == len(matrix) - 1 and val == '.'), None)

    if start_pos is None or end_pos is None:
        return "Start or end position not found."

    return parallel_longest_hike(matrix, start_pos, end_pos)

sys.setrecursionlimit(10000)
print(day23("./day23_test.txt"))
print("début du test")
start_time = time.time()
print(day23("./day23.txt"))
end_time = time.time()
print(f"Temps d'exécution: {end_time - start_time} secondes")