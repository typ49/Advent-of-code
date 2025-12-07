from collections import deque

def day7(filepath):


    def addInSeen(r,c):
        if (r, c) in seen: return
        seen.add((r, c))
        beams.append((r, c))

    grid = [list(line.strip()) for line in open(filepath)]

    S = [(r, c) for r, row in enumerate(grid) for c, char in enumerate(row) if char =="S"][0]

    beams = deque([S])
    seen = {S}
    count = 0

    while len(beams) > 0:
        r, c = beams.popleft()
        if grid[r][c] == "." or grid[r][c] == "S" :
            if r == len(grid)-1: continue
            addInSeen(r+1, c)

        elif grid[r][c] == "^":
            count += 1
            addInSeen(r, c-1)
            addInSeen(r, c+1)
                
    return count 



    
if __name__ == "__main__":
    print(day7("test.txt"))
    print(day7("input.txt"))
