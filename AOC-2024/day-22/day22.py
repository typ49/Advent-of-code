# XOR between two numbers
def mix(number, secretNumber):
    return number ^ secretNumber


# number % 16777216
def prune(number):
    return number % 16777216


def sequence(secretNumber):
    mul64 = secretNumber*64
    secretNumber = mix(mul64, secretNumber)
    secretNumber = prune(secretNumber)
    div32 = secretNumber // 32
    secretNumber = mix(div32, secretNumber)
    secretNumber = prune(secretNumber)
    mul2048 = secretNumber * 2048
    secretNumber = mix(mul2048, secretNumber)
    secretNumber = prune(secretNumber)
    return secretNumber


def repeatSequence(secretNumber, times):
    for i in range(times):
        secretNumber = sequence(secretNumber)
    return secretNumber


def main():
    secretNumber = 123
    result = repeatSequence(secretNumber, 10)
    print("10 sequence : ", result)
    
    test = open('AOC-2024/day-22/test.txt').read().splitlines()
    result = 0
    for line in test:
        line = line.strip()
        if line:  # Ignore les lignes vides
            number = int(line)
            result += repeatSequence(number, 2000)
    print("Test : ", result) # should return 37327623
    
    input = open('AOC-2024/day-22/input.txt').read().splitlines()
    result = 0
    for line in input:
        line = line.strip()
        if line:  # Ignore les lignes vides
            number = int(line)
            result += repeatSequence(number, 2000)
    print("Input : ", result)
        
if __name__ == "__main__":
    main()
    
    
if __name__ == "__main__":
    main()