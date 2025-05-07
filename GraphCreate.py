
import networkx as nx
import matplotlib.pyplot as plt

class GraphCreate:

    def __init__(self, nodes):
        self.nodes = nodes

    def generate_complete_graph(self):
        return nx.complete_graph(self.nodes) 
    
    def print_graph(graph):
        nx.draw(graph , with_labels=True , node_color='lightblue')
        return plt.show()