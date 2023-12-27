def hash(s):
    res = 0

    for ch in s:
       res += ord(ch)
       res *= 17
       res %= 256

    return res



def day15(filepath):
    res = 0
    with open(filepath) as f:
        res = sum(map(hash, f.read().split(',')))
    
    return res

# main
filepath = "./input.txt"
if __name__ == '__main__':
    print(day15(filepath))
    
