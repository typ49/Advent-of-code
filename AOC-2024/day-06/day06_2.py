def loops(grid, rows, r, cols, c):
        row_direction = -1
        column_direction = 0

        seen = set()

        while True:
            seen.add((r, c, row_direction, column_direction))
            if r + row_direction < 0 or r + row_direction >= rows or c + column_direction < 0 or c + column_direction >= cols: return False
            if grid[r + row_direction][c + column_direction] == "#":
                column_direction, row_direction = -row_direction, column_direction
            else:
                r += row_direction
                c += column_direction
            if (r, c, row_direction, column_direction) in seen:
                return True

def guardPath(grid):
    rows = len(grid)
    cols = len(grid[0])

    # find the guard
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "^":
                break
        else:
            continue
        break

    count = 0

    for current_row in range(rows):
        for current_column in range(cols):
            if grid[current_row][current_column] != ".": continue
            grid[current_row][current_column] = "#"
            if loops(grid, rows, r, cols, c):
                count += 1
            grid[current_row][current_column] = "."

    return count

def main():
    input = list(map(list, open('AOC-2024/day-06/input.txt').read().splitlines()))
    test = list(map(list, open('AOC-2024/day-06/test.txt').read().splitlines()))
    
    print(guardPath(test))
    print(guardPath(input))
    
if __name__ == "__main__":
    main()