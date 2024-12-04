def getInput(file):
    with open(file, 'r') as f:
        return f.read().splitlines()

def find_word_in_grid(grid, word):
    def search_direction(x, y, dx, dy):
        for i in range(len(word)):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] != word[i]:
                return False
            x += dx
            y += dy
        return True

    directions = [
        (1, 0), (0, 1), (-1, 0), (0, -1),  # Horizontal & Vertical
        (1, 1), (-1, -1), (1, -1), (-1, 1)  # Diagonal
    ]
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for dx, dy in directions:
                if search_direction(i, j, dx, dy):
                    count += 1
    return count

# Exemple de grille
grid = getInput('AOC-2024/day-04/input.txt')

word = "XMAS"
print(f"L'occurrence du mot '{word}' dans la grille est : {find_word_in_grid(grid, word)}")
