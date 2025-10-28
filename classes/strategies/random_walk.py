import random
from classes.strategies.coloring_strategy import ColoringStrategy
from classes.graph import Graph
from classes.coloring import Color, Coloring
from classes.utils import get_conflicts

class RandomWalk(ColoringStrategy):
    '''Random walk chooses randomly a variable and changes its color. If it reduces the number of conflicts the change is accepted.'''

    initial_coloring: Coloring = {}
    max_iter: int = 0
    
    def __init__(self, initial_coloring: Coloring, max_iter: int) -> None:
        self.initial_coloring = initial_coloring
        self.max_iter = max_iter

    def __str__(self) -> str:
        return "Random walk"

    def color(self, graph: Graph, colors: list[Color]) -> tuple[Coloring, int]:
        coloring = self.initial_coloring.copy()
        conflicts, _ = get_conflicts(graph, coloring)

        for _ in range(self.max_iter):
            neighbor = random.choice(list(coloring.keys()))

            new_coloring = coloring.copy()
            new_coloring[neighbor] = random.choice(colors)
            new_conflicts, _ = get_conflicts(graph, new_coloring)

            if(new_conflicts < conflicts):
                coloring = new_coloring
                conflicts = new_conflicts

                if(conflicts == 0):
                    break

        return coloring, conflicts
    