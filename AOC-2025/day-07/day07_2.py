from functools import cache

def day7(filepath):

    grid = [list(line.strip()) for line in open(filepath)]

    S = [(r, c) for r, row in enumerate(grid) for c, char in enumerate(row) if char == "S"][0]

    @cache
    def solve(r, c):
        if r >= len(grid): return 1
        
        if grid[r][c] == "." or grid[r][c] == "S":
            return solve(r + 1, c)
        elif grid[r][c] == "^":
            return solve(r, c - 1) + solve(r, c + 1)

    return solve(*S)



    
if __name__ == "__main__":
    print(day7("test.txt"))
    print(day7("input.txt"))
