def fileToMatrix(file_path):
    """
    Reads a file and returns a matrix of the contents.

    Args:
        (str) file_path: the path of the file

    Returns :
        a matrix for the file
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

def findSpecialCharacter(matrix):
    """
    Finds all characters that are not dot or number.

    Args:
        (tab 2D) matrix : a matrix

    Returns:
        a list of specialCharacter
    """
    specialCharacter = []
    for line in matrix:
        for character in line:
            if character not in specialCharacter and not character.isdigit() and character != '.':
                specialCharacter.append(character)
    return specialCharacter

def findPosOfSpecialCharacter(matrix, specialCharacters):
    """
    Finds all the positions of the special characters in a matrix.

    Args:
        (tab 2D) matrix : a matrix
        (list) specialCharacter : a list of specialCharacter

    Returns:
        the position of the special char in the matrix
    """
    posOfSpecialCharacter = {}
    for specialCharacter in specialCharacters:
        posOfSpecialCharacter[specialCharacter] = []
        for line in range(len(matrix)):
            for Character in range(len(matrix[line])):
                if matrix[line][Character] == specialCharacter:
                    posOfSpecialCharacter[specialCharacter].append((line, Character))
    return posOfSpecialCharacter

def findAdjacentNumbers(matrix, posOfSpecialCharacter):
    """
    Finds all the adjacent numbers to the special characters (up, down, left, right, diagonal).
    Numbers can have several digits. Also keeps track of their start and end positions.!

    Args:
        (tab 2D) matrix : a matrix
        (dict) posOfSpecialCharacter : the position of the special char in the matrix

    Returns:
        a list of adjacent numbers
    """
    adjacentNumbersWithPos = set()

    for specialCharacter in posOfSpecialCharacter:
        for pos in posOfSpecialCharacter[specialCharacter]:
            for line in range(pos[0] - 1, pos[0] + 2):
                for Character in range(pos[1] - 1, pos[1] + 2):
                    if 0 <= line < len(matrix) and 0 <= Character < len(matrix[line]) and matrix[line][Character].isdigit():
                        startPos, endPos = findNumberPosition(matrix, line, Character)
                        if (startPos, endPos) not in adjacentNumbersWithPos:  # Check if the number position is not already added
                            adjacentNumbersWithPos.add((startPos, endPos))

    # Extract and sum the numbers from their positions
    numbers = [extractNumber(matrix, startPos, endPos) for startPos, endPos in adjacentNumbersWithPos]
    return numbers

def findNumberPosition(matrix, line, Character):
    """
    Finds the start and end positions of a complete number starting from a digit at a given position.

    Args:
        (tab 2D) matrix : a matrix
        (int) line : the line of the digit
        (int) Character : the column of the digit

    Returns:
        the start and end positions of the number
    """
    startCharacter = Character
    endCharacter = Character

    # Check horizontally to the left
    while startCharacter > 0 and matrix[line][startCharacter - 1].isdigit():
        startCharacter -= 1

    # Check horizontally to the right
    while endCharacter < len(matrix[line]) and matrix[line][endCharacter].isdigit():
        endCharacter += 1

    return (line, startCharacter), (line, endCharacter - 1)

def extractNumber(matrix, startPos, endPos):
    """
    Extracts a number from the matrix given its start and end positions.

    Args:
        (tab 2D) matrix : a matrix
        (tuple) startPos : the start position of the number
        (tuple) endPos : the end position of the number

    Returns:
        the number
    """
    line, startCharacter = startPos
    _, endCharacter = endPos
    return int(''.join(matrix[line][startCharacter:endCharacter + 1]))

# Main program
file_path = './input.txt'
matrix = fileToMatrix(file_path)
specialCharacters = findSpecialCharacter(matrix)
posOfSpecialCharacter = findPosOfSpecialCharacter(matrix, specialCharacters)
adjacentNumbers = findAdjacentNumbers(matrix, posOfSpecialCharacter)

# Calculate the sum of all unique adjacent numbers
result = sum(adjacentNumbers)
print(result)
