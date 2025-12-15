def day3(filepath):
    """
    in a raw of batteries, you need to find the two digit who made the biggest product

    the idea is to find out the first largest digit then find the second largest digit who is after the first one in the raw
    
    
    """
    with open(filepath, 'r') as file:
        lines =  file.readlines()
        result = 0
        current_first_largest = 0
        index=0
        current_second_largest = 0
        for line in lines:
            line = line.strip()
            for i in range(len(line)-1):
                if int(line[i]) > current_first_largest:
                    current_first_largest = int(line[i])
                    index = i
            for j in range(index+1, len(line)):
                if int(line[j]) > current_second_largest:
                    current_second_largest = int(line[j])
            result += current_first_largest * 10 + current_second_largest
            current_first_largest = 0
            current_second_largest = 0
        return result
    

if __name__ == "__main__":
    filepath = 'input.txt'
    fileTest = 'test.txt'
    print(day3(fileTest))  # Expected output for test file
    print(day3(filepath))
