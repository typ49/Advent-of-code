def day1(filepath):
    """
    take a file and for every line in the file,
    find the first digit of the string and the last digit of the string
    concate the two digits to make a number
    and add every number together
    
    Args:
        filepath (str): The path to the file to parse.

    Returns:
        int: the sum of all the numbers
    """
    with open(filepath, 'r') as f:
        for line in f:
            digits = [char for char in line if char.isdigit()]
            t += int(digits[0] + digits[-1])

    return t

# main
filepath = "./input.txt"
if __name__ == '__main__':
    print(day1(filepath))