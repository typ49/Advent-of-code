def find_mirror(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]
        
        if sum(sum(0 if a == b else 1 for a, b in zip(x, y)) for x, y in zip(above, below)) == 1:
            return r

    return 0

def day13p2(filepath):
    total = 0
    with open(filepath, 'r') as f:
        for block in f.read().split("\n\n"):
            grid = block.splitlines()

            row = find_mirror(grid)
            total += row * 100

            col = find_mirror(list(zip(*grid)))
            total += col

    return total

# main
filepath = "./day13.txt"
print(day13p2(filepath))