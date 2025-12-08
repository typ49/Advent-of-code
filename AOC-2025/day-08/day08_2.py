from collections import defaultdict


def day8(filepath, max_connections_part1=1000):
    # --- Lecture de l'entrée ---
    points = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            x_str, y_str, z_str = line.split(",")
            x, y, z = map(int, (x_str, y_str, z_str))
            points.append((x, y, z))

    n = len(points)
    if n == 0:
        return 0, 0

    # --- Construction de toutes les arêtes (paires) ---
    edges = []
    for i in range(n):
        x1, y1, z1 = points[i]
        for j in range(i + 1, n):
            x2, y2, z2 = points[j]
            dx = x1 - x2
            dy = y1 - y2
            dz = z1 - z2
            dist2 = dx * dx + dy * dy + dz * dz  # distance au carré
            edges.append((dist2, i, j))

    # Tri des arêtes par distance croissante
    edges.sort(key=lambda e: e[0])

    # --- Partie 1 : 1000 connexions ---
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if rank[ra] < rank[rb]:
            parent[ra] = rb
        elif rank[ra] > rank[rb]:
            parent[rb] = ra
        else:
            parent[rb] = ra
            rank[ra] += 1
        return True

    # Appliquer les max_connections_part1 plus courtes connexions
    max_conn = min(max_connections_part1, len(edges))
    for k in range(max_conn):
        _, i, j = edges[k]
        union(i, j)

    # Calcul des tailles de circuits (partie 1)
    sizes = defaultdict(int)
    for i in range(n):
        root = find(i)
        sizes[root] += 1

    component_sizes = sorted(sizes.values(), reverse=True)
    # Sécurisation : au moins 3 tailles pour l’indexation
    while len(component_sizes) < 3:
        component_sizes.append(1)

    a, b, c = component_sizes[0], component_sizes[1], component_sizes[2]
    part1 = a * b * c

    # --- Partie 2 : continuer jusqu'à 1 seul circuit ---
    parent = list(range(n))
    rank = [0] * n

    def find2(x):
        if parent[x] != x:
            parent[x] = find2(parent[x])
        return parent[x]

    def union2(a, b):
        ra, rb = find2(a), find2(b)
        if ra == rb:
            return False
        if rank[ra] < rank[rb]:
            parent[ra] = rb
        elif rank[ra] > rank[rb]:
            parent[rb] = ra
        else:
            parent[rb] = ra
            rank[ra] += 1
        return True

    components = n
    part2 = None

    for dist2, i, j in edges:
        if union2(i, j):
            components -= 1
            if components == 1:
                # dernière connexion utile : produit des X
                xi = points[i][0]
                xj = points[j][0]
                part2 = xi * xj
                break

    return part1, part2


if __name__ == "__main__":
    p1_test, p2_test = day8("test.txt")
    print("test part 1:", p1_test)
    print("test part 2:", p2_test)

    p1_input, p2_input = day8("input.txt")
    print("input part 1:", p1_input)
    print("input part 2:", p2_input)
