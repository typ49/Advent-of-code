import re, itertools

def day10(filepath):

    total = 0

    for line in open(filepath):
        match = re.match(r"^\[([.#]+)\] ([()\d, ]+) \{([\d,]+)\}$", line.strip())
        target, buttons, _ = match.groups()
        target = { index for index, light in enumerate(target) if light == "#" }
        buttons = [set(map(int, button[1:-1].split(","))) for button in buttons.split()]
        for count in range(1, len(buttons) + 1):
            for attempt in itertools.combinations(buttons, r=count):
                lights = set()
                for button in attempt:
                    lights ^= button
                if lights == target:
                    total += count
                    break
            else:
                continue
            break

    return total


if __name__=="__main__":
    print(day10("test.txt"))
    print(day10("input.txt"))