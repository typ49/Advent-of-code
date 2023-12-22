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

def findAdjacentNumbers(matrix, posOfSpecialCaracter):
    """
    Finds all the adjacent numbers to the special characters (up, down, left, right, diagonal).
    Numbers can have several digits. Also keeps track of their start and end positions.
    """
    adjacentNumbersWithPos = set()

    for specialCaracter in posOfSpecialCaracter:
        for pos in posOfSpecialCaracter[specialCaracter]:
            for line in range(pos[0] - 1, pos[0] + 2):
                for caracter in range(pos[1] - 1, pos[1] + 2):
                    if 0 <= line < len(matrix) and 0 <= caracter < len(matrix[line]) and matrix[line][caracter].isdigit():
                        startPos, endPos = findNumberPosition(matrix, line, caracter)
                        if (startPos, endPos) not in adjacentNumbersWithPos:  # Check if the number position is not already added
                            adjacentNumbersWithPos.add((startPos, endPos))

    # Extract and sum the numbers from their positions
    numbers = [extractNumber(matrix, startPos, endPos) for startPos, endPos in adjacentNumbersWithPos]
    return numbers

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

# Main program
file_path = './day3.txt'
matrix = fileToMatrix(file_path)
specialCaracters = findSpecialCaracter(matrix)
posOfSpecialCaracter = findPosOfSpecialCaracter(matrix, specialCaracters)
adjacentNumbers = findAdjacentNumbers(matrix, posOfSpecialCaracter)

# Calculate the sum of all unique adjacent numbers
result = sum(adjacentNumbers)
print(result)
