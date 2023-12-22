def forceOfHandWithJoker(hand):
    # example of hand : AA2AA
    # sort hand = [A, A, A, A, 2]
    # the joker became the best card for increase the hand
    # example : A2JAA -> AA2AA |JJAAA -> AAAAA | JJJJJ -> JJJJJ | AAJJ2 -> AAJJJ | AAKKJ -> AAAKK

    sortHand = []

    for i in hand:
        sortHand.append(i)
    sortHand.sort()

    numberOfJoker = 0
    for i in range(len(sortHand)):
        if sortHand[i] == 'J':
            numberOfJoker += 1
    
    if numberOfJoker == 0:
        # hand type : 5 of a kind(7), four of a kind(6), full house(5), three of a kind(4), two pairs(3), one pair(2), high card(1)
        if sortHand[0] == sortHand[4]:
            return 7
        elif sortHand[0] == sortHand[3] or sortHand[1] == sortHand[4]:
            return 6
        elif (sortHand[0] == sortHand[2] and sortHand[3] == sortHand[4]) or (sortHand[0] == sortHand[1] and sortHand[2] == sortHand[4]):
            return 5
        elif (sortHand[0] == sortHand[2]) or (sortHand[1] == sortHand[3]) or (sortHand[2] == sortHand[4]):
            return 4
        elif (sortHand[0] == sortHand[1] and sortHand[2] == sortHand[3]) or (sortHand[0] == sortHand[1] and sortHand[3] == sortHand[4]) or (sortHand[1] == sortHand[2] and sortHand[3] == sortHand[4]):
            return 3
        elif (sortHand[0] == sortHand[1]) or (sortHand[1] == sortHand[2]) or (sortHand[2] == sortHand[3]) or (sortHand[3] == sortHand[4]):
            return 2
        else:
            return 1
    elif numberOfJoker == 1:
        # hand type : 5 of a kind(7), four of a kind(6), full house(5), three of a kind(4), two pairs(3), one pair(2), high card(1)
        if sortHand[0] == sortHand[3] or sortHand[1] == sortHand[4]:
            return 7
        elif (sortHand[0] == sortHand[2] and sortHand[3] == sortHand[4]) or (sortHand[0] == sortHand[1] and sortHand[2] == sortHand[4]):
            return 6
        elif (sortHand[0] == sortHand[2]) or (sortHand[1] == sortHand[3]) or (sortHand[2] == sortHand[4]):
            return 5
        elif (sortHand[0] == sortHand[1] and sortHand[2] == sortHand[3]) or (sortHand[0] == sortHand[1] and sortHand[3] == sortHand[4]) or (sortHand[1] == sortHand[2] and sortHand[3] == sortHand[4]):
            return 4
        elif (sortHand[0] == sortHand[1]) or (sortHand[1] == sortHand[2]) or (sortHand[2] == sortHand[3]) or (sortHand[3] == sortHand[4]):
            return 3
        else:
            return 2
        
    elif numberOfJoker == 2:
        # hand type : 5 of a kind(7), four of a kind(6), full house(5), three of a kind(4), two pairs(3), one pair(2), high card(1)
        if sortHand[0] == sortHand[2] or sortHand[1] == sortHand[3] or sortHand[2] == sortHand[4]:
            return 7
        elif (sortHand[0] == sortHand[1] and sortHand[2] == sortHand[3]) or (sortHand[0] == sortHand[1] and sortHand[3] == sortHand[4]) or (sortHand[1] == sortHand[2] and sortHand[3] == sortHand[4]):
            return 6
        elif (sortHand[0] == sortHand[1]) or (sortHand[1] == sortHand[2]) or (sortHand[2] == sortHand[3]) or (sortHand[3] == sortHand[4]):
            return 5
        else:
            return 4
    elif numberOfJoker == 3:
        # hand type : 5 of a kind(7), four of a kind(6), full house(5), three of a kind(4), two pairs(3), one pair(2), high card(1)
        if sortHand[0] == sortHand[1] or sortHand[1] == sortHand[2] or sortHand[2] == sortHand[3] or sortHand[3] == sortHand[4]:
            return 7
        else:
            return 6
    elif numberOfJoker >= 4:
        return 7


    

def parse_fichier_jeu(chemin_fichier):
    """
    crée une liste de trinome (forceOfHand, hand, value) pour chaque jeu.
    """
    jeux = []
    with (open(chemin_fichier, 'r')) as file:
        for line in file:
            hand, value = line.strip().split(" ")
            force = forceOfHandWithJoker(hand)
            jeux.append((force, hand, value))
    return jeux

def compare (hand, hand2):
    order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    print(hand,"?", hand2," : ")
    forceOfHand, hand = hand[0], hand[1]
    forceOfHand2, hand2 = hand2[0], hand2[1]
    if (forceOfHand == forceOfHand2):
        for i in range(len(hand)):
            if order.index(hand[i]) > order.index(hand2[i]):
                print(False)
                return False
            elif order.index(hand[i]) < order.index(hand2[i]):
                print(True)
                return True
        print(False)
        return False
    else:
        print(forceOfHand > forceOfHand2)
        return forceOfHand > forceOfHand2
    

def sortJeux(jeux):
    for i in range(len(jeux)):
        for j in range(i+1, len(jeux)):
            if compare(jeux[i], jeux[j]):
                jeux[i], jeux[j] = jeux[j], jeux[i]
    return jeux

def main():
    result = 0
    path = './day7.txt'
    jeux = parse_fichier_jeu(path)
    jeux = sortJeux(jeux)
    print(jeux)
    for i in range(len(jeux)):
        # value * place in the list
        result += int(jeux[i][2]) * (i+1)
        print(jeux[i][2],'*',(i+1),'=',int(jeux[i][2]) * (i+1))
        print(result)
    print(result)

main()
