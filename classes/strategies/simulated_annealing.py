import math
import random
from classes.strategies.coloring_strategy import ColoringStrategy
from classes.graph import Graph
from classes.coloring import Color, Coloring
from classes.utils import get_conflicts

class SimulatedAnnealing(ColoringStrategy):
    '''Simulated Annealing is simmilar to First Improvement, but can accept worse colors with a given possibility that reduces over time.'''

    initial_temperature: float = 0
    cooling_rate: float = 0
    initial_coloring: Coloring = {}
    max_iter: int = 0

    def __init__(self, initial_coloring: Coloring, max_iter: int, initial_temperature: float, cooling_rate: float) -> None:
        self.initial_temperature = initial_temperature
        self.cooling_rate = cooling_rate
        self.initial_coloring = initial_coloring
        self.max_iter = max_iter

    def _accept_changes(self, new_conflicts: int, conflicts: int, temperature: float):
        if new_conflicts <= conflicts:
            return True
        
        p = math.exp(-(new_conflicts - conflicts) / temperature)
        return random.random() < p
    
    
    def color(self, graph: Graph, colors: list[Color]) -> tuple[Coloring, int]:
        coloring = self.initial_coloring.copy()
        conflicts, conflicting_vertices = get_conflicts(graph, coloring)
        temperature = self.initial_temperature

        if(conflicts == 0):
            return coloring, conflicts

        for _ in range(self.max_iter):

            vertex = random.choice(conflicting_vertices)

            for color in colors:
                new_coloring = coloring.copy()
                new_coloring[vertex] = color

                new_conflicts, new_conflicting_vertices = get_conflicts(graph, new_coloring)

                if(self._accept_changes(new_conflicts, conflicts, temperature)):
                    conflicts = new_conflicts
                    coloring = new_coloring
                    if(conflicts == 0):
                        break

                    conflicting_vertices = new_conflicting_vertices

            temperature = temperature * self.cooling_rate

        return coloring, conflicts