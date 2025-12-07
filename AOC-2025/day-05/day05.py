def day05(filename):
    ranges, numbers = open(filename).read().split("\n\n")
    
    ranges = [list(map(int, range.split("-"))) for range in ranges.splitlines()]

    numbers = list(map(int, numbers.splitlines()))

    count = 0

    for number in numbers:
        for low, high in ranges:
            if low <= number <= high:
                count += 1
                break
        
    return count

if __name__ == "__main__":
    print(day05("test.txt"))
    print(day05("input.txt"))