def getInput(file):
    lst1 = []
    lst2 = []
    with open(file) as f:
        for line in f:
            l = line.split()
            lst1.append(int(l[0]))
            lst2.append(int(l[1]))
    return lst1, lst2

# get the difference between the two lists
def difference_between(lst1, lst2):
    lst1 = sorted(lst1)
    lst2 = sorted(lst2)
    res = []
    for i in range(len(lst1)):
        res.append(abs(lst1[i] - lst2[i]))
    return res

def main():
    lst1, lst2 = getInput("test.txt")
    lst3, lst4 = getInput("input.txt")
    print(difference_between(lst1, lst2))
    print(difference_between(lst3, lst4))
    res = sum(difference_between(lst1, lst2))
    res2 = sum(difference_between(lst3, lst4))
    print(res)
    print(res2)

if __name__ == "__main__":
    main()