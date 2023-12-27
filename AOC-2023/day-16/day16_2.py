from collections import deque

def calculate(r, c, dr, dc):

    # r= row, c= column, dr= delta row, dc= delta column

    # in a grid, we start here : 
    # > . . . .
    #   . . . .
    #   . . . .
    #   . . . .

    a = [(r, c, dr, dc)]
    # q= queue
    q = deque(a)
    seen = set()

    while q: # while queue is not empty
        r, c, dr, dc = q.popleft() # pop the first element

        # update new position
        r += dr
        c += dc

        # if we are out of bounds, skip
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            continue

        # ch = character
        ch = grid[r][c]

        if ch == "." or (ch == "-" and dc != 0) or (ch == "|" and dr != 0):
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        elif ch == "/":
            # if we are going down, go left : (0, 1) => (-1, 0)
            # if we are going up, go right : (0, -1) => (1, 0)
            # if we are going left, go down : (-1, 0) => (0, 1)
            # if we are going right, go up : (1, 0) => (0, -1)
            # (dr, dc) => (-dc, -dr)

            dr, dc = -dc, -dr
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        elif ch == "\\":
            dr, dc = dc, dr
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        else:
            for dr, dc in [(1, 0), (-1, 0)] if ch == "|" else [(0,1), (0,-1)]:
                if (r, c, dr, dc) not in seen:
                    seen.add((r, c, dr, dc))
                    q.append((r, c, dr, dc))
    coords = {(r, c) for (r, c, _, _) in seen}

    return len((coords))

def main(filepath):
    global grid
    with open(filepath, 'r') as f:
        grid = f.read().splitlines()
    max_value = 0

    for r in range(len(grid)):
        max_value = max(max_value, calculate(r, -1, 0, 1))
        max_value = max(max_value, calculate(r, len(grid[0]), 0, -1))

    for c in range(len(grid[0])):
        max_value = max(max_value, calculate(-1, c, 1, 0))
        max_value = max(max_value, calculate(len(grid), c, -1, 0))


    return max_value

filepath = "./input.txt"
if __name__ == "__main__":
    print(main(filepath))