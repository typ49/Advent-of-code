import re

def day12(filepath):
    lines = open(filepath).read().split("\n\n")[-1].splitlines()

    result = 0

    for line in lines:
        x, y, *counts = list(map(int, re.findall(r"\d+", line)))

        if (x // 3) * (y // 3) >= sum(counts):
            result += 1


    return result


if __name__=="__main__":
    print(day12("test.txt"))
    print(day12("input.txt"))