import re
def day1p2(filepath):
    t = 0
    n = "one two three four five six seven eight nine".split()
    p = "(?=(" + "|".join(n) + "|\\d))"

    """
    La regex (?=(" + "|".join(n) + "|\\d)) est utilisée pour trouver tous les chiffres ou noms de chiffres dans une chaîne.

    Voici une explication détaillée :

    |.join(n) : Cela crée une chaîne à partir de la liste n (qui contient les noms des chiffres de "one" à "nine")
    en les joignant avec le caractère |, qui est l'opérateur OR en regex. 
    Le résultat est une chaîne "one|two|three|four|five|six|seven|eight|nine".

    "|\d" : Cela ajoute l'expression |\\d à la fin de la chaîne précédente,
    ce qui donne "one|two|three|four|five|six|seven|eight|nine|\d". L'expression \\d correspond à tout chiffre de 0 à 9.

    "(?=(" + "|".join(n) + "|\d))" : Cela entoure la chaîne précédente avec "(?=...)",
    qui est une assertion de lookahead positive en regex. 
    Cela signifie que la regex va chercher une correspondance pour "one|two|three|four|five|six|seven|eight|nine|\d", 
    mais sans consommer de caractères dans la chaîne de recherche. En d'autres termes, après avoir trouvé une correspondance, 
    la recherche continue à partir du même point dans la chaîne.

    Donc, en résumé, cette regex cherche tous les chiffres ou noms de chiffres dans une chaîne, 
    sans consommer de caractères. 
    Cela signifie que si deux chiffres ou noms de chiffres se chevauchent dans la chaîne,
    ils seront tous les deux trouvés par la regex.
    """


    def f(x):
        if x in n:
            return str(n.index(x) + 1)
        return x


    for x in open(filepath, 'r'):
        digits = [*map(f, re.findall(p, x))]
        t += int(digits[0] + digits[-1])

    return t

# main
filepath = "./input.txt"
if __name__ == '__main__':
    print(day1p2(filepath))