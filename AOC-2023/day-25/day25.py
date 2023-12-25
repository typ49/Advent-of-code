# github/hyper-neutrino

import networkx as nx

def generate_graph(filepath):
    # Création d'un nouveau graphe vide
    g = nx.Graph()

    # Pour chaque ligne du fichier d'entrée
    with open(filepath, 'r') as f:
        for line in f:
            # Séparation de la ligne en deux parties : 'left' et 'right', en utilisant ":" comme délimiteur
            left, right = line.split(":")
            # Pour chaque noeud dans la partie 'right' de la ligne (après avoir supprimé les espaces de début et de fin et séparé les noeuds par des espaces)
            for node in right.strip().split():
                # Ajout d'un bord entre 'left' et le noeud dans le graphe
                g.add_edge(left, node)
                # Ajout d'un bord entre le noeud et 'left' dans le graphe
                g.add_edge(node, left)

        # Suppression des bords du graphe qui font partie du minimum edge cut
        g.remove_edges_from(nx.minimum_edge_cut(g))
        # Récupération des deux composantes connectées du graphe après la suppression des bords
        a, b = nx.connected_components(g)

    # Retourne le produit des tailles des deux composantes connectées
    return len(a) * len(b)


# main
filepath = "./day25.txt"
print(generate_graph(filepath))