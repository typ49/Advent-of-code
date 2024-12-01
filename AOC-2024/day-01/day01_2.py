def getInput(file):
    lst1 = []
    lst2 = []
    with open(file) as f:
        for line in f:
            l = line.split()
            lst1.append(int(l[0]))
            lst2.append(int(l[1]))
    return lst1, lst2


# for each unique element in lst1, find the number of times it appears in lst2
def similarity_score(lst1, lst2):
    lit1 = sorted(lst1)
    lst2 = sorted(lst2)
    similarity = []
    
    for i in range(len(lit1)):
        similarity.append(lit1[i] * lst2.count(lit1[i]))
        
    return sum(similarity)



def main():
    lst1, lst2 = getInput("test.txt")
    lst3, lst4 = getInput("input.txt")
    print(similarity_score(lst1, lst2))
    print(similarity_score(lst3, lst4))

if __name__ == "__main__":
    main()
    