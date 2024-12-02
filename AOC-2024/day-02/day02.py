# get an input in this format : 
## num1 num2 ...
## numX ...
# and return a list of int for each line
def parse_input_onto_int_list(file):
    with open(file) as f:
        return [[int(x) for x in line.split()] for line in f]
    return null
    
    
def doesDecreaseByOneTwoOrThree(lst):
    for i in range(1, len(lst)):
        if lst[i-1] - lst[i] != 1 and lst[i-1] - lst[i] != 2 and lst[i-1] - lst[i] != 3:
            print (lst[i], lst[i-1])
            return False
    return True

def doesIncreaseByOneTwoOrThree(lst):
    for i in range(1, len(lst)):
        if lst[i-1] - lst[i] != -1 and lst[i-1] - lst[i] != -2 and lst[i-1] - lst[i] != -3:
            print (lst[i], lst[i-1])
            return False
    return True

def getdecreaseLine(file):
    res = 0
    data = parse_input_onto_int_list(file)
    for line in data:
        print(line)
        if doesDecreaseByOneTwoOrThree(line) or doesIncreaseByOneTwoOrThree(line):
            res += 1
    return res
    
def main():
    res = getdecreaseLine("test.txt")
    print(res)
    res2 = getdecreaseLine("input.txt")
    print(res2)
    
    
if __name__ == "__main__":
    main()