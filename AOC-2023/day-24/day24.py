import sys
import re
from copy import deepcopy
from math import gcd
from collections import defaultdict, Counter, deque
import heapq
import math
from z3 import *

def day24(filepath):
    try:
        f = open(filepath, 'r')
        print("Ouverture du fichier...")
        D = f.read().strip()
        print("Fichier ouvert avec succès.")
    except IOError:
        print("Erreur : Fichier introuvable ou impossible à lire.")
        sys.exit(1)

    L = D.split('\n')
    S = []
    print("Début du traitement des données.")
    for line in L:
        pos, vel = line.split('@')
        x, y, z = map(int, pos.split(', '))
        vx, vy, vz = map(int, vel.split(', '))
        S.append((x, y, z, vx, vy, vz))
    print("Données traitées.")

    # Initial calculations
    print("Début des calculs initiaux.")
    ans = 0
    for i in range(len(S)):
        for j in range(i+1, len(S)):
            x1, y1, x3, y3 = S[i][0], S[i][1], S[j][0], S[j][1]
            x2, y2, x4, y4 = x1 + S[i][3], y1 + S[i][4], x3 + S[j][3], y3 + S[j][4]

            den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
            if den != 0:
                px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / den
                py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / den
                validA = (px > x1) == (x2 > x1)
                validB = (px > x3) == (x4 > x3)

                if 200000000000000 <= px <= 400000000000000 and 200000000000000 <= py <= 400000000000000 and validA and validB:
                    ans += 1
    print(f"Calculs initiaux terminés. Résultat : {ans}")

# main
filepath = "./input.txt"
if __name__ == '__main__':
    day24(filepath)