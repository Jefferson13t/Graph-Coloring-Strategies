import random
from classes.graph import Graph
from classes.coloring import Color, Coloring

def get_conflicts(graph: Graph, coloring: Coloring) -> tuple[int, list[str]]:
    visited = set()
    conflicting = set()

    for u in graph.graph:
        for neighbor in graph.get_neighbors(u):
            if (u, neighbor) not in visited and (neighbor, u) not in visited:
                if coloring[u] == coloring[neighbor]:
                    conflicting.add((u))
                    conflicting.add((neighbor))
                visited.add((u, neighbor))
                visited.add((neighbor, u))

    return len(conflicting), list(conflicting)

def generate_random_coloring(grafo: Graph, cores: list[Color] = ["vermelho", "azul", "verde", "amarelo"]) -> Coloring:
    coloracao = {}
    for vertice in grafo.graph.keys():
        coloracao[vertice] = random.choice(cores)
    return coloracao
