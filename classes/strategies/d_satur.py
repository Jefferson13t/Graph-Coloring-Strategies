from classes.strategies.coloring_strategy import ColoringStrategy
from classes.graph import Graph
from classes.coloring import Color, Coloring
from classes.utils import get_conflicts

class DSatur(ColoringStrategy):
    '''DSatur chooses the variable with the highest saturation (number of colored neighbors) and select the first color available for it.'''

    max_iter = 0

    def __init__(self, max_iter: int) -> None:
        self.max_iter = max_iter

    def _calculate_saturation(self, graph: Graph, vertex: str, current_coloring: Coloring) -> tuple[int, set[Color]]:
        neighbor_colors = {
            current_coloring[v]
            for v in graph.get_neighbors(vertex)
            if current_coloring[v] is not None
        }
        return len(neighbor_colors), neighbor_colors

    def _accept_vertex(self, graph: Graph, highest_saturation: int, saturation: int, most_saturated_vertex: str | None, vertex: str) -> bool:
        if(most_saturated_vertex is None): 
            return True
        
        if(highest_saturation < saturation):
            return True
        
        if(highest_saturation == saturation):    
            most_saturated_vertex_degree = graph.in_degree(most_saturated_vertex) + graph.out_degree(most_saturated_vertex)
            vertex_degree = graph.in_degree(vertex) + graph.out_degree(vertex)

            if(most_saturated_vertex_degree <= vertex_degree):
                return True
       
        return False

    def color(self, graph: Graph, colors: list[Color]) -> tuple[Coloring, int]:

        coloring = {}
        for edge in graph.get_edges():
            if(edge.u not in coloring):
                coloring[edge.u] = None
            if(edge.v not in coloring):
                coloring[edge.v] = None

        for _ in range(self.max_iter):
            highest_saturation = 0
            most_saturated_vertex = None
            best_available_colors  = []
        
            for vertex in coloring.keys():
                if(coloring[vertex] is not None):
                    continue

                saturation, cores_indisponiveis = self._calculate_saturation(graph, vertex, coloring)

                if(self._accept_vertex(graph, highest_saturation, saturation, most_saturated_vertex, vertex)):
                    highest_saturation = saturation
                    most_saturated_vertex = vertex
                    best_available_colors = cores_indisponiveis

            if(most_saturated_vertex is None):
                break

            for color in colors:
                if(color not in best_available_colors):
                    coloring[most_saturated_vertex] = color
                    break

        conflitos, _ = get_conflicts(graph, coloring)
        return coloring, conflitos