def day1(filepath):
    with open(filepath, 'r') as f:
        """parsing a file like this:
        L99
        R45
        ...

        L for left, R for right followed by number of steps

        the dials is a circle from 0 to 99
        we start at 50
        we need to find how many times we stop at pose 0
        """
        position = 50
        nb_zeros = 0
        for line in f:
            if line[0] == 'L':
                position -= int(line[1:])
            elif line[0] == 'R':
                position += int(line[1:])
            position = position % 100
            if position == 0:
                nb_zeros += 1
    return nb_zeros
#main
if __name__ == '__main__':
    filepath = "./input.txt"
    testfilepath = "./test.txt"
    print(day1(testfilepath))
    print(day1(filepath))



        
        
        
