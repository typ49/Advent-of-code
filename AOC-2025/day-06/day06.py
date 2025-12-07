def day6(filepath):

    lines = [line.strip().split() for line in open(filepath)]
    cols = list(zip(*lines))

    result = 0

    for *number, op in cols:
        result  += eval(op.join(number))

    return result

    



if __name__ == "__main__":
    print(day6("test.txt"))
    print(day6("input.txt"))
