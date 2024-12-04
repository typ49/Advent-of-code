def getInput(file):
    with open(file, 'r') as f:
        return f.read().splitlines()

grid = getInput('AOC-2024/day-04/input.txt')
testGrid = getInput('AOC-2024/day-04/test.txt')


# on cherche le motif :
# M M    S S    M S    S M
#  A  ou  A  ou  A  ou  A
# S S    M M    S M    M S
# ce qui revient à chercher les A dans la grille qui ont les coins en M et S    
def getPattern(grid):
    count = 0

    for r in range(1, len(grid) - 1):
        for c in range(1, len(grid[0]) - 1):
            if grid[r][c] != "A": continue
            corners = [grid[r - 1][c - 1], grid[r - 1][c + 1], grid[r + 1][c + 1], grid[r + 1][c - 1]]
            if "".join(corners) in ["MMSS", "MSSM", "SSMM", "SMMS"]:
                count += 1
    return count


def main():
    print(f"Le nombre du motifs dans la grille de test est : {getPattern(testGrid)}")
    print(f"Le nombre du motifs  dans la grille est : {getPattern(grid)}")
    
    
    
if __name__ == "__main__":
    main()