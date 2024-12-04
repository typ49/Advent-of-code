import re

def getinput(file):
    with open(file, 'r') as f:
        return f.read()

def getMul(file):
    # Texte d'entrée
    text = getinput(file)

    # Étape 1 : Extraire tous les `do()`, `don't()` et `mul(x,y)`
    pattern_extraction = r"(?:do\(\)|don't\(\)|mul\(\d+,\d+\))"
    all_matches = re.findall(pattern_extraction, text)
    print("Étape 1 - Occurrences extraites :", all_matches)

    # Étape 2 : Filtrer les `mul(x,y)` selon les conditions
    result = 0
    activate = True
    for match in all_matches:
        if match == "don't()":
            activate = False
        if match == "do()":
            activate = True
            
        if match.startswith("mul(") and activate:
            a, b = map(int, re.findall(r'\d+', match))
            result += a * b
        

    print("Étape 2 - Résultat final :", result)


def main():
    getMul('AOC-2024/day-03/test.txt')
    getMul('AOC-2024/day-03/input.txt')
    
    
if __name__ == '__main__':
    main()