import re
def day1p2(filepath):
    """
    Find the first and the last digit in a string, then concatanate these digits to create a number,
    then add all the numbers to find the result.
    The digit can been written in letters or in digit
    
    Args:
        (str) filepath : the path of the file
        
    Returns:
        (int) : the result of the sequence for every line in the file
    """
    t = 0
    n = "one two three four five six seven eight nine".split()
    p = "(?=(" + "|".join(n) + "|\\d))"


    def f(x):
        if x in n:
            return str(n.index(x) + 1)
        return x


    for x in open(filepath, 'r'):
        digits = [*map(f, re.findall(p, x))]
        t += int(digits[0] + digits[-1])

    return t

# main
filepath = "./input.txt"
if __name__ == '__main__':
    print(day1p2(filepath))