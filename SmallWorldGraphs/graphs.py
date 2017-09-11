import random
import matplotlib.pyplot as plt

import networkx as nx
import numpy as np

def randomSeed(x):
    random.seed(x)
    np.random.seed(x)

# this function generates edges with degree k if k is even, and k - 1 if k is odd
def adjacent_edges(nodes, k):
    n = len(nodes)
    for i, u in enumerate(nodes):
        for j in range(i + 1, i + k // 2 + 1):
            v = nodes[j % n]
            yield u, v 

def make_ring_lattice(n, k):
    G = nx.Graph()
    nodes = range(n)
    G.add_nodes_from(nodes)
    G.add_edges_from(adjacent_edges(nodes, k))
    return G

def rewire_lattice(lattice, p):
    nodes = set(lattice.nodes())
    for u,v in lattice.edges():
        if flip(p):
            choices = nodes - {u} - set(lattice[u])
            new_v = np.random.choice(tuple(choices))
            lattice.remove_edge(u,v)
            lattice.add_edge(u,new_v)

def make_ws_graph(numberOfNodes, numberOfEdges, prob):
    lattice = make_ring_lattice(numberOfNodes, numberOfEdges)
    rewire_lattice(lattice, prob)
    return lattice

def flip(p):
    return np.random.random() < p

def main():
    randomSeed(17)
    #nodes = range(3)
    #for edge in adjacent_edges(nodes, 2):
    #    print(edge)

    #lat#tice = make_ring_lattice(10, 4)
    #nx.#draw_circular(lattice)
    ws = make_ws_graph(10, 4, 1)
    nx.draw_circular(ws)
    plt.show()

if __name__ == "__main__":
    main()
