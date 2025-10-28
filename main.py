from classes.graph import Graph
from classes.utils import generate_random_coloring
from classes.coloring import Color
from classes.strategies.strategies import RandomWalk, SimulatedAnnealing, GeneticAlgorithm, BestImprovement, DSatur, FirstImprovementAC
from classes.benchmark import ColoringStrategiesBenchmark

def main() -> int:

    ''''This is the entry point of this project. It starts by creating a instance of a graph and its edges, then instanciate each coloring algorithm with its parameters and then plots a benchmark for each algorithm.'''

    graph = Graph()
    graph.add_undirected_edge("V1", "V2", 1)
    graph.add_undirected_edge("V1", "V3", 1)
    graph.add_undirected_edge("V1", "V6", 1)
    graph.add_undirected_edge("V1", "V7", 1)
    graph.add_undirected_edge("V2", "V5", 1)
    graph.add_undirected_edge("V3", "V4", 1)
    graph.add_undirected_edge("V3", "V6", 1)
    graph.add_undirected_edge("V3", "V7", 1)
    graph.add_undirected_edge("V4", "V5", 1)
    graph.add_undirected_edge("V4", "V6", 1)
    graph.add_undirected_edge("V5", "V7", 1)
    graph.add_undirected_edge("V5", "V8", 1)
    graph.add_undirected_edge("V5", "V10", 1)
    graph.add_undirected_edge("V6", "V7", 1)
    graph.add_undirected_edge("V6", "V9", 1)
    graph.add_undirected_edge("V8", "V10", 1)
    graph.add_undirected_edge("V9", "V10", 1)

    COLORS = ["vermelho", "azul", "verde", "amarelo"]

    initial_coloring = generate_random_coloring(graph, COLORS)
    MAX_ITER = 1000

    randomWalk = RandomWalk(initial_coloring, MAX_ITER)

    bestImprovement = BestImprovement(initial_coloring, MAX_ITER)

    firstImprovementAC = FirstImprovementAC(initial_coloring, MAX_ITER)

    dSatur = DSatur(MAX_ITER)

    INITIAL_TEMPERATURE = 10
    COOLING_RATE = 0.9
    simulatedAnnealing = SimulatedAnnealing(initial_coloring, MAX_ITER, INITIAL_TEMPERATURE, COOLING_RATE)

    INDIVIDUAL_NUMBER = 100
    GENERATION_NUMBER = 500
    MUTATION_RATE = 0.05
    INITIAL_TEMPERATURE = 10
    geneticAlgorithm = GeneticAlgorithm(INDIVIDUAL_NUMBER, GENERATION_NUMBER, MUTATION_RATE, INITIAL_TEMPERATURE, COOLING_RATE)

    coloringStrategiesBenchmark = ColoringStrategiesBenchmark() 

    NUMBER_OF_RUNS = 20
    coloringStrategiesBenchmark.evaluate_strategies(
        graph,
        COLORS,
        NUMBER_OF_RUNS,
        [
            randomWalk,
            bestImprovement,
            firstImprovementAC,
            dSatur,
            simulatedAnnealing,
            geneticAlgorithm,
        ]
    )

    return 0

main()