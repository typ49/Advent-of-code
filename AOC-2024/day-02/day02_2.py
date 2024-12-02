def parse_input_onto_int_list(file):
    print(f"Parsing input file: {file}")
    with open(file) as f:
        data = [[int(x) for x in line.split()] for line in f]
    print(f"Parsed data: {data}")
    return data

def doesDecreaseByOneTwoOrThree(lst):
    print(f"Checking if list decreases by 1, 2, or 3: {lst}")
    for i in range(1, len(lst)):
        if lst[i-1] - lst[i] != 1 and lst[i-1] - lst[i] != 2 and lst[i-1] - lst[i] != 3:
            print(f"List does not decrease by 1, 2, or 3 at index {i}: {lst[i-1]} -> {lst[i]}")
            return False
    print("List decreases by 1, 2, or 3")
    return True

def doesIncreaseByOneTwoOrThree(lst):
    print(f"Checking if list increases by 1, 2, or 3: {lst}")
    for i in range(1, len(lst)):
        if lst[i-1] - lst[i] != -1 and lst[i-1] - lst[i] != -2 and lst[i-1] - lst[i] != -3:
            print(f"List does not increase by 1, 2, or 3 at index {i}: {lst[i-1]} -> {lst[i]}")
            return False
    print("List increases by 1, 2, or 3")
    return True

def doesSafeIfOneLevelRemoved(lst):
    print(f"Checking if list is safe if one level is removed: {lst}")
    for i in range(0, len(lst)):
        newLst = lst[:i] + lst[i+1:]
        print(f"Checking new list without index {i}: {newLst}")
        if doesDecreaseByOneTwoOrThree(newLst) or doesIncreaseByOneTwoOrThree(newLst):
            print(f"List is safe if element at index {i} is removed: {lst[i]}")
            return True
    print("List is not safe if any one level is removed")
    return False

def getdecreaseLine(file):
    print(f"Processing file to get decrease lines: {file}")
    res = 0
    data = parse_input_onto_int_list(file)
    for line in data:
        print(f"Processing line: {line}")
        if doesDecreaseByOneTwoOrThree(line) or doesIncreaseByOneTwoOrThree(line) or doesSafeIfOneLevelRemoved(line):
            print(f"Line meets criteria: {line}")
            res += 1
        else:
            print(f"Line does not meet criteria: {line}")
    print(f"Total lines meeting criteria: {res}")
    return res

def main():
    res = getdecreaseLine("test.txt")
    print(f"Result for test.txt: {res}")
    res2 = getdecreaseLine("input.txt")
    print(f"Result for input.txt: {res2}")

if __name__ == "__main__":
    main()