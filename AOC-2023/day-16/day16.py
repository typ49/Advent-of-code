from collections import deque

def day16(filepath):
    with open(filepath) as f:
        grid = f.read().splitlines()

    # r= row, c= column, dr= delta row, dc= delta column

    # in a grid, we start here : 
    # > . . . .
    #   . . . .
    #   . . . .
    #   . . . .

    a = [(0, -1, 0, 1)]
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

# main
filepath = "./input.txt"
if __name__ == "__main__":
    print(day16(filepath))