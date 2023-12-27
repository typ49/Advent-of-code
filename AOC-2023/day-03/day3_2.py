def fileToMatrix(file_path):
    """
    Reads a file and returns a matrix of the contents.
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

def findSpecialCaracter(matrix):
    """
    Finds all characters that are not dot or number.
    """
    specialCaracter = []
    for line in matrix:
        for caracter in line:
            if caracter not in specialCaracter and not caracter.isdigit() and caracter != '.':
                specialCaracter.append(caracter)
    return specialCaracter

def findPosOfSpecialCaracter(matrix, specialCaracters):
    """
    Finds all the positions of the special characters in a matrix.
    """
    posOfSpecialCaracter = {}
    for specialCaracter in specialCaracters:
        posOfSpecialCaracter[specialCaracter] = []
        for line in range(len(matrix)):
            for caracter in range(len(matrix[line])):
                if matrix[line][caracter] == specialCaracter:
                    posOfSpecialCaracter[specialCaracter].append((line, caracter))
    return posOfSpecialCaracter

def findNumberPosition(matrix, line, caracter):
    """
    Finds the start and end positions of a complete number starting from a digit at a given position.
    """
    startCaracter = caracter
    endCaracter = caracter

    # Check horizontally to the left
    while startCaracter > 0 and matrix[line][startCaracter - 1].isdigit():
        startCaracter -= 1

    # Check horizontally to the right
    while endCaracter < len(matrix[line]) and matrix[line][endCaracter].isdigit():
        endCaracter += 1

    return (line, startCaracter), (line, endCaracter - 1)

def extractNumber(matrix, startPos, endPos):
    """
    Extracts a number from the matrix given its start and end positions.
    """
    line, startCaracter = startPos
    _, endCaracter = endPos
    return int(''.join(matrix[line][startCaracter:endCaracter + 1]))

def findGearRatios(matrix, posOfSpecialCaracter):
    """
    Finds the gear ratios for each gear. A gear is defined as a special symbol adjacent to exactly two part numbers.
    The gear ratio is the product of these two numbers.
    """
    gearRatios = []

    for specialCaracter in posOfSpecialCaracter:
        for pos in posOfSpecialCaracter[specialCaracter]:
            adjacentNumbers = set()
            for line in range(pos[0] - 1, pos[0] + 2):
                for caracter in range(pos[1] - 1, pos[1] + 2):
                    if 0 <= line < len(matrix) and 0 <= caracter < len(matrix[line]) and matrix[line][caracter].isdigit():
                        startPos, endPos = findNumberPosition(matrix, line, caracter)
                        number = extractNumber(matrix, startPos, endPos)
                        adjacentNumbers.add(number)

            # Check if the symbol is adjacent to exactly two part numbers
            if len(adjacentNumbers) == 2:
                gearRatio = 1
                for num in adjacentNumbers:
                    gearRatio *= num
                gearRatios.append(gearRatio)

    return gearRatios

# Main program
matrix = fileToMatrix('./input.txt')
specialCaracters = findSpecialCaracter(matrix)
posOfSpecialCaracter = findPosOfSpecialCaracter(matrix, specialCaracters)
gearRatios = findGearRatios(matrix, posOfSpecialCaracter)

# Calculate the sum of all gear ratios
totalGearRatio = sum(gearRatios)
print(totalGearRatio)
