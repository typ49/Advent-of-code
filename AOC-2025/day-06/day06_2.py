def day6(filepath):

    grid = [line.strip("\n") for line in open(filepath)]
    cols = list(zip(*grid))

    groups = []
    group = []

    for col in cols:
        if set(col) == {" "}:
            groups.append(group)
            group = []
        else:
            group.append(col)

    groups.append(group)

    result = 0

    for group in groups:
        result += eval(group[0][-1].join("".join(line[:-1]) for line in group))

    return result

    



if __name__ == "__main__":
    print(day6("test.txt"))
    print(day6("input.txt"))
