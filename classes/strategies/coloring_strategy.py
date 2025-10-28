from abc import ABC, abstractmethod
from classes.graph import Graph
from classes.coloring import Color, Coloring

class ColoringStrategy(ABC):
    '''Base class for the coloring strategies'''

    @abstractmethod
    def color(self, graph: Graph, colors: list[Color]) -> tuple[Coloring, int]:
        raise NotImplementedError
    