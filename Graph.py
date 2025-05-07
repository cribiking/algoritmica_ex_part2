
import networkx as nx
import matplotlib.pyplot as plt


class Graph:

    def __init__(self , node):
        self.node = node
        self.graph = None

    def generete_complete_graph(self):
        self.graph = nx.complete_graph(self.node) 
        return self.graph
    
    def draw(self):
        if self.graph is None:
            raise ValueError("Genera un graf.")
    
        nx.draw(self.graph, with_labels=True, node_color='lightblue')
        plt.title("Grafo generat")
        plt.show()