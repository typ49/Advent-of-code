import re

# Texte
def getinput(file):
    with open(file, 'r') as f:
        return f.read()


def getMul(file):
    text = getinput(file)
    # Regex
    pattern = r'mul\(\d+,\d+\)'

    # Recherche
    matches = re.findall(pattern, text)
    print(matches)  # Résultat : ['mul(2,4)', 'mul(5,5)', 'mul(11,8)', 'mul(8,5)']
    res = 0
    # mul(2,4) = 8
    for match in matches:
        a, b = map(int, re.findall(r'\d+', match))
        res += a * b
    
    print(res)  # Résultat : 8 + 25 + 88 + 40 = 161
    
    
    
def main():
    getMul('AOC-2024/day-03/test.txt')
    # getMul('AOC-2024/day-03/input.txt')
    

if __name__ == '__main__':
    main()