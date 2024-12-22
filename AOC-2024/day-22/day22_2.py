# XOR between two numbers
def mix(number, secretNumber):
    return number ^ secretNumber


# number % 16777216
def prune(number):
    return number % 16777216


def sequence(secretNumber, buyer):
    mul64 = secretNumber*64
    secretNumber = mix(mul64, secretNumber)
    secretNumber = prune(secretNumber)
    div32 = secretNumber // 32
    secretNumber = mix(div32, secretNumber)
    secretNumber = prune(secretNumber)
    mul2048 = secretNumber * 2048
    secretNumber = mix(mul2048, secretNumber)
    secretNumber = prune(secretNumber)
    buyer.append(secretNumber % 10)
    return secretNumber


def repeatSequence(secretNumber, buyer, times):
    for i in range(times):
        secretNumber = sequence(secretNumber, buyer)
    return secretNumber


def find_best_sequence(buyer, seen, seq_to_total):
    for i in range(len(buyer) - 4):
            a, b, c, d, e = buyer[i:i + 5]
            seq = (b - a, c - b, d - c, e - d)
            if seq in seen: continue
            seen.add(seq)
            if seq not in seq_to_total: seq_to_total[seq] = 0
            seq_to_total[seq] += e

    return max(seq_to_total.values())


def main():
    seq_to_total = {}

    input = open('AOC-2024/day-22/input.txt').read().splitlines()

    for line in input:
        num = int(line)
        buyer = [num % 10]
        num = repeatSequence(num, buyer, 2000)
        seen = set()
        result = find_best_sequence(buyer, seen, seq_to_total)
    print("Input : ", result)
    
    
if __name__ == "__main__":
    main()