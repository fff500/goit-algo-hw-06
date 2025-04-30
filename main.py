import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


from bfs import bfs
from dfs import dfs
from dijkstra import dijkstra

def main():
    G = nx.Graph()
    # Stores and restaurants in my town
    G.add_nodes_from(["Home", "PD", "C1", "C2", "A", "L", "IM", "BK", "TP"])

    G.add_edge("Home", "PD", weight=2)
    G.add_edge("PD", "C1", weight=8)
    G.add_edge("C1", "C2", weight=2)
    G.add_edge("C1", "TP", weight=2)
    G.add_edge("TP", "C2", weight=3)
    G.add_edge("C2", "A", weight=2)
    G.add_edge("A", "L", weight=1)
    G.add_edge("A", "BK", weight=1)
    G.add_edge("BK", "L", weight=1)
    G.add_edge("A", "IM", weight=2)
    G.add_edge("IM", "Home", weight=10)
    G.add_edge("IM", "C1", weight=6)

    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    is_connected = nx.is_connected(G)
    degree_centrality = nx.degree_centrality(G)
    closeness_centrality = nx.closeness_centrality(G)
    betweenness_centrality = nx.betweenness_centrality(G)

    print("Кількість вершин:")
    print(num_nodes)
    print("Кількість ребер:")
    print(num_edges)
    print("Сполученість вершин:")
    print(is_connected)
    print("Центральність за ступенем:")
    print(degree_centrality)
    print("Центральність за близькістю:")
    print(closeness_centrality)
    print("Центральність за посередництвом:")
    print(betweenness_centrality)

    print("Ступені вершин:")
    for node, degree in G.degree():
        print(f"{node}: {degree}")

    print("DFS:")
    dfs(G, 'Home')
    print("\nBFS:")
    bfs(G, deque(["Home"]))

    print("\nDijkstra:")
    print(dijkstra(G, 'Home'))

    pos = nx.spring_layout(G, seed=42)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

if __name__ == "__main__":
    main()
