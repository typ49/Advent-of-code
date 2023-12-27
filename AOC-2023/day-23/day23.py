import sys

def lire_fichier_matrice(chemin_du_fichier):
    with open(chemin_du_fichier, 'r', encoding='utf-8') as fichier:
        return [list(ligne.strip()) for ligne in fichier]


def valid_next_positions(matrix, pos, visited):
    directions = {'>': (0, 1), '<': (0, -1), 'v': (1, 0), '^': (-1, 0)}
    x, y = pos
    next_steps = []

    if matrix[x][y] in directions:
        dx, dy = directions[matrix[x][y]]
        next_x, next_y = x + dx, y + dy
        if 0 <= next_x < len(matrix) and 0 <= next_y < len(matrix[0]) and (next_x, next_y) not in visited:
            next_steps.append((next_x, next_y))
    else:
        for dx, dy in directions.values():
            next_x, next_y = x + dx, y + dy
            if 0 <= next_x < len(matrix) and 0 <= next_y < len(matrix[0]) and matrix[next_x][next_y] != '#' and (next_x, next_y) not in visited:
                next_steps.append((next_x, next_y))

    return next_steps

def longest_hike(matrix, pos, endPos, visited, path_length):
    if pos == endPos:
        return path_length
    max_length = 0
    for next_pos in valid_next_positions(matrix, pos, visited):
        visited.add(next_pos)
        max_length = max(max_length, longest_hike(matrix, next_pos, endPos, visited, path_length + 1))
        visited.remove(next_pos)
    return max_length

def day23(filepath):
    matrix = lire_fichier_matrice(filepath)
    startPos = next(((i, j) for i, row in enumerate(matrix) for j, val in enumerate(row) if i == 0 and val == '.'), None)
    endPos = next(((i, j) for i, row in enumerate(matrix) for j, val in enumerate(row) if i == len(matrix) - 1 and val == '.'), None)

    if startPos is None or endPos is None:
        return "Start or end position not found."

    return longest_hike(matrix, startPos, endPos, set([startPos]), 0)

# main
sys.setrecursionlimit(10000)
filepath = "./input.txt"
if __name__ == '__main__':
    print(day23(filepath))
