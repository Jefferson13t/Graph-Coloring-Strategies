import random
from classes.strategies.coloring_strategy import ColoringStrategy
from classes.graph import Graph
from classes.coloring import Color, Coloring
from classes.utils import get_conflicts

class FirstImprovementAC(ColoringStrategy):
    '''First Improvement with Any Conflict selects a conflicting variable and changes its color for the color that most reduces conflicts...'''

    initial_coloring: Coloring = {}
    max_iter: int = 0

    def __init__(self, initial_coloring: Coloring, max_iter: int) -> None:
        self.initial_coloring = initial_coloring
        self.max_iter = max_iter

    def color(self, graph: Graph, colors: list[Color]) -> tuple[Coloring, int]:
        coloring = self.initial_coloring.copy()
        conflicts, conflicting_vertex = get_conflicts(graph, coloring)

        if(conflicts == 0):
            return coloring, conflicts

        for _ in range(self.max_iter):

            vertice = random.choice(conflicting_vertex)

            for color in colors:
                new_coloring = coloring.copy()
                new_coloring[vertice] = color

                new_conflicts, new_conflicting_vertex = get_conflicts(graph, new_coloring)

                if(new_conflicts < conflicts):
                    conflicts = new_conflicts
                    coloring = new_coloring
                    conflicting_vertex = new_conflicting_vertex

                    if(conflicts == 0):
                        return coloring, conflicts

        return coloring, conflicts
