from classes.graph import Graph
from classes.utils import generate_random_coloring
from classes.coloring import Color
from classes.strategies.strategies import (
    RandomWalk,
    SimulatedAnnealing,
    GeneticAlgorithm,
    BestImprovement,
    DSatur,
    FirstImprovementAC,
)
from classes.benchmark import ColoringStrategiesBenchmark


def build_graph() -> Graph:
    """Creates and returns a graph instance with predefined edges."""
    graph = Graph()
    edges = [
        ("V1", "V2"), ("V1", "V3"), ("V1", "V6"), ("V1", "V7"),
        ("V2", "V5"), ("V3", "V4"), ("V3", "V6"), ("V3", "V7"),
        ("V4", "V5"), ("V4", "V6"), ("V5", "V7"), ("V5", "V8"),
        ("V5", "V10"), ("V6", "V7"), ("V6", "V9"), ("V8", "V10"),
        ("V9", "V10"),
    ]
    for u, v in edges:
        graph.add_undirected_edge(u, v, 1)
    return graph


def build_strategies(graph: Graph, colors: list[Color]) -> list:
    """Creates and returns a list of coloring strategy instances."""
    MAX_ITER = 1000
    INITIAL_TEMPERATURE = 10
    COOLING_RATE = 0.9
    INDIVIDUAL_NUMBER = 100
    GENERATION_NUMBER = 500
    MUTATION_RATE = 0.05

    initial_coloring = generate_random_coloring(graph, colors)

    return [
        RandomWalk(initial_coloring, MAX_ITER),
        BestImprovement(initial_coloring, MAX_ITER),
        FirstImprovementAC(initial_coloring, MAX_ITER),
        DSatur(MAX_ITER),
        SimulatedAnnealing(initial_coloring, MAX_ITER, INITIAL_TEMPERATURE, COOLING_RATE),
        GeneticAlgorithm(INDIVIDUAL_NUMBER, GENERATION_NUMBER, MUTATION_RATE, INITIAL_TEMPERATURE, COOLING_RATE),
    ]


def main() -> int:
    """
    Entry point of the project.
    Creates a graph, initializes strategies, and benchmarks them.
    """
    COLORS = ["vermelho", "azul", "verde", "amarelo"]
    NUMBER_OF_RUNS = 20
    OUTPUT_FILE = "img/benchmark.png"

    graph = build_graph()
    strategies = build_strategies(graph, COLORS)

    benchmark = ColoringStrategiesBenchmark()
    benchmark.evaluate_strategies(graph, COLORS, NUMBER_OF_RUNS, OUTPUT_FILE, strategies)

    return 0


if __name__ == "__main__":
    main()
