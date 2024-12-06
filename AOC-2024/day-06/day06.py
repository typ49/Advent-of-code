def guardPath(grid):
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "^":
                break
        else:
            continue
        break

    row_direction = -1
    column_direction = 0

    seen = set()

    while True:
        seen.add((r, c))
        if r + row_direction < 0 or r + row_direction >= rows or c + column_direction < 0 or c + column_direction >= cols: break
        if grid[r + row_direction][c + column_direction] == "#":
            column_direction, row_direction = -row_direction, column_direction
        else:
            r += row_direction
            c += column_direction

    return len(seen)



def main():
    test = list(map(list, open('AOC-2024/day-06/test.txt').read().splitlines()))
    input = list(map(list, open('AOC-2024/day-06/input.txt').read().splitlines()))
    
    print(guardPath(test))
    print(guardPath(input))
    
if __name__ == "__main__":
    main()