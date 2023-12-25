import re
def day1p2(filepath):
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
filepath = "./day1.txt"
print(day1p2(filepath))