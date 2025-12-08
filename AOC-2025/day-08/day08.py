from collections import defaultdict


def solve_day8_file(filepath, max_connections=1000):
    # Lecture de l'entrée
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
        return 0

    # Union-Find
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

    # Construction de toutes les arêtes (paires)
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

    # Appliquer les max_connections plus courtes connexions
    max_connections = min(max_connections, len(edges))
    for k in range(max_connections):
        _, i, j = edges[k]
        union(i, j)

    # Calcul des tailles de circuits
    sizes = defaultdict(int)
    for i in range(n):
        root = find(i)
        sizes[root] += 1

    component_sizes = sorted(sizes.values(), reverse=True)
    if len(component_sizes) < 3:
        # Cas pathologique : moins de 3 circuits, on adapte
        # (pour AoC normalement tu en as au moins 3) [web:12]
        prod = 1
        for s in component_sizes:
            prod *= s
        return prod

    a, b, c = component_sizes[0], component_sizes[1], component_sizes[2]
    return a * b * c


if __name__ == "__main__":
    print("test:", solve_day8_file("test.txt"))
    print("input:", solve_day8_file("input.txt"))
