data = open('AOC-2024/day-08/input.txt').read()
grid = list(map(list, data.splitlines()))

rows = len(grid)    # number of rows
cols = len(grid[0]) # number of collumns

antennas = {} #all the antennas in the input (digit, lowercase and upercase character except '.')

# register all the unique antennas with there position in the grid
for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if char != ".":
            if char not in antennas: antennas[char] = []
            antennas[char].append((r,c))

# print(antennas)
antinodes = set() # all the nodes created by following the rules

for array in antennas.values():
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            r1, c1 = array[i]
            r2, c2 = array[j]
            antinodes.add((2*r1 - r2, 2* c1 - c2))
            antinodes.add((2*r2 - r1, 2* c2 - c1))

print(len([0 for r, c in antinodes if 0 <= r < rows and 0 <= c < cols]))