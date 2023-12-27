from collections import deque

def day10(filepath):
    """
    La fonction day10 analyse une grille de circuit à partir d'un fichier texte.
    Elle commence par la position marquée par "S" et suit le circuit pour déterminer le caractère qui devrait remplacer "S".
    Elle utilise une file d'attente pour suivre le chemin et un ensemble pour garder une trace des coordonnées visitées.
    Elle utilise également un ensemble pour garder une trace des caractères possibles pour "S".

    Args:
        filepath (str): Le chemin vers le fichier à analyser.

    Returns:
        int: Le nombre de points dans la grille qui ne sont pas à l'extérieur du circuit.
    """
    with open(filepath, 'r') as f:
        grid = f.read().strip().splitlines()

    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == "S":
                sr = r # sr = start row
                sc = c # sc = start column
                break
        else:
            continue
        break

    loop = {(sr, sc)}
    q = deque([(sr, sc)])

    maybe_s = {"|", "-", "J", "L", "7", "F"}

    while q:
        r, c = q.popleft()
        ch = grid[r][c]

        if r > 0 and ch in "S|JL" and grid[r - 1][c] in "|7F" and (r - 1, c) not in loop:
            loop.add((r - 1, c))
            q.append((r - 1, c))
            if ch == "S":
                maybe_s &= {"|", "J", "L"}
            
        if r < len(grid) - 1 and ch in "S|7F" and grid[r + 1][c] in "|JL" and (r + 1, c) not in loop:
            loop.add((r + 1, c))
            q.append((r + 1, c))
            if ch == "S":
                maybe_s &= {"|", "7", "F"}

        if c > 0 and ch in "S-J7" and grid[r][c - 1] in "-LF" and (r, c - 1) not in loop:
            loop.add((r, c - 1))
            q.append((r, c - 1))
            if ch == "S":
                maybe_s &= {"-", "J", "7"}

        if c < len(grid[r]) - 1 and ch in "S-LF" and grid[r][c + 1] in "-J7" and (r, c + 1) not in loop:
            loop.add((r, c + 1))
            q.append((r, c + 1))
            if ch == "S":
                maybe_s &= {"-", "L", "F"}

    assert len(maybe_s) == 1
    (S,) = maybe_s

    grid = [row.replace("S", S) for row in grid]
    grid = ["".join(ch if (r, c) in loop else "." for c, ch in enumerate(row)) for r, row in enumerate(grid)]

    outside = set()

    for r, row in enumerate(grid):
        within = False
        up = None
        for c, ch in enumerate(row):
            if ch == "|":
                assert up is None
                within = not within
            elif ch == "-":
                assert up is not None
            elif ch in "LF":
                assert up is None
                up = ch == "L"
            elif ch in "7J":
                assert up is not None
                if ch != ("J" if up else "7"):
                    within = not within
                up = None
            elif ch == ".":
                pass
            else:
                raise RuntimeError(f"unexpected character (horizontal): {ch}")
            if not within:
                outside.add((r, c))
                
    return (len(grid) * len(grid[0]) - len(outside | loop))


# main
filepath = "./input.txt"
print(day10(filepath))