def day05(filename):
    ranges, _ = open(filename).read().split("\n\n")
    
    ranges = [list(map(int, range.split("-"))) for range in ranges.splitlines()]
    ranges.sort()

    last = None

    count = 0

    for low, high in ranges:
        if last is None:
            last = (low, high)
        elif last[1] < low:
            count += last[1] - last[0] + 1
            last = (low, high)
        else:
            last = (last[0], max(last[1], high))

    count += last[1] - last[0] + 1
        
    return count

if __name__ == "__main__":
    print(day05("test.txt"))
    print(day05("input.txt"))