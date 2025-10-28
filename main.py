from classes.graph import Graph

def main():

    Example = Graph()

    Example.add_undirected_edge("V1", "V2", 1)
    Example.add_undirected_edge("V1", "V3", 1)
    Example.add_undirected_edge("V1", "V6", 1)
    Example.add_undirected_edge("V1", "V7", 1)
    Example.add_undirected_edge("V2", "V5", 1)
    Example.add_undirected_edge("V3", "V4", 1)
    Example.add_undirected_edge("V3", "V6", 1)
    Example.add_undirected_edge("V3", "V7", 1)
    Example.add_undirected_edge("V4", "V5", 1)
    Example.add_undirected_edge("V4", "V6", 1)
    Example.add_undirected_edge("V5", "V7", 1)
    Example.add_undirected_edge("V5", "V8", 1)
    Example.add_undirected_edge("V5", "V10", 1)
    Example.add_undirected_edge("V6", "V7", 1)
    Example.add_undirected_edge("V6", "V9", 1)
    Example.add_undirected_edge("V8", "V10", 1)
    Example.add_undirected_edge("V9", "V10", 1)


    coloring_exemple = {
        "V1": "vermelho",
        "V2": "azul",
        "V3": "vermelho",
        "V4": "amarelo",
        "V5": "azul",
        "V6": "verde",
        "V7": "vermelho",
        "V8": "azul",
        "V9": "verde",
        "V10": "vermelho"
    }

    return 0