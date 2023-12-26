def find_mirror(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]
        
        above = above[:len(below)]
        below = below[:len(above)]
        
        if above == below:
            return r
        
    return 0


def day13(filepath):
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
print(day13(filepath))