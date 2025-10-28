from classes.strategies.coloring_strategy import ColoringStrategy
from classes.graph import Graph
from classes.coloring import Color, Coloring
from classes.utils import get_conflicts

class BestImprovement(ColoringStrategy):
    '''Best Improvement tests all changes for fall variables and selects the change that reduces conflicts the most.'''

    initial_coloring: Coloring = {}
    max_iter = 0
    
    def __init__(self, initial_coloring: Coloring, max_iter: int) -> None:
        self.initial_coloring = initial_coloring
        self.max_iter = max_iter

    def __str__(self) -> str:
        return "Best Improvement"

    def color(self, graph: Graph, colors: list[Color]) -> tuple[Coloring, int]:
        coloring = self.initial_coloring.copy()
        conflicts, _ = get_conflicts(graph, coloring)

        for _ in range(self.max_iter):

            best_coloring_improvement = coloring.copy()
            best_improvement = 0

            for vertex in coloring.keys():
                for color in colors:
                    new_coloring = coloring.copy()
                    new_coloring[vertex] = color
                    new_conflicts, _ = get_conflicts(graph, new_coloring)

                    melhora = conflicts - new_conflicts

                    if(best_improvement < melhora):
                        best_coloring_improvement = new_coloring
                        best_improvement = melhora

            coloring = best_coloring_improvement
            conflicts -= best_improvement
            if(conflicts == 0):
                break
        
        return coloring, conflicts