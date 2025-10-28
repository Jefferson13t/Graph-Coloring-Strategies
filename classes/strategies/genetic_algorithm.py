import math
import random
from classes.strategies.coloring_strategy import ColoringStrategy
from classes.graph import Graph
from classes.coloring import Color, Coloring
from classes.utils import get_conflicts, generate_random_coloring

class GeneticAlgorithm(ColoringStrategy):
    '''Genetic Algorithm simulates the evolution theory. At each generation selects the best fit individuals and mutates them to make a new generation.'''

    individual_number: int = 10
    generation_number: int = 10
    mutation_rate: float = 0
    initial_temperature: float = 0
    cooling_rate: float = 0

    def __init__(self, individual_number: int, generation_number: int, mutation_rate: float, initial_temperature: float, cooling_rate: float) -> None:
        self.individual_number = individual_number
        self.generation_number = generation_number
        self.mutation_rate = mutation_rate
        self.initial_temperature = initial_temperature
        self.cooling_rate = cooling_rate

    def _create_initial_population(self, graph: Graph, available_colors: list[Color]) -> list[Coloring]:
        
        population = []

        for _ in range(self.individual_number):
            coloring = generate_random_coloring(graph, available_colors)
            population.append(coloring)
        
        return population

    def _calculate_fitness(self, individual: Coloring, graph: Graph) -> int:
        fitness, _ = get_conflicts(graph, individual)
        return fitness

    def _accept_changes(self, best_individual_fitness: float, fitness: float, temperature: float) -> bool:
        if fitness <= best_individual_fitness:
            return True
        
        p = math.exp(-(fitness - best_individual_fitness) / temperature)
        return random.random() < p
    
    def _selection_with_annealing(self, population: list[Coloring], graph: Graph, temperature: float) -> tuple[int, int]:

        selected_individual_index = 0
        best_individual_fitness = self._calculate_fitness(population[selected_individual_index], graph)

        for i in range(len(population)):
            fitness = self._calculate_fitness(population[i], graph)

            if(self._accept_changes(best_individual_fitness, fitness, temperature)):
                best_individual_fitness = fitness
                selected_individual_index = i
            
        return selected_individual_index, best_individual_fitness

    def _crossover(self, parent_1: Coloring, parent_2: Coloring) -> tuple[Coloring, Coloring]:
        
        cutoff_point = random.randint(0, len(parent_1) - 1)
        
        child_1 = {}
        child_2 = {}

        i = 0
        for key in parent_1.keys():

            if(i <= cutoff_point):
                child_1[key] = parent_1[key]
                child_2[key] = parent_2[key]
            else:
                child_1[key] = parent_2[key]
                child_2[key] = parent_1[key]
            i += 1
        
        return child_1, child_2

    def _mutation(self, individual: Coloring, colors: list[Color]) -> Coloring:

        if random.random() <= self.mutation_rate:
            gene = random.choice(list(individual))
            current_color = individual[gene]
            available_colors  = [c for c in colors if c != current_color]
            individual[gene] = random.choice(available_colors )
            
        return individual
    
    def color(self, graph: Graph, colors: list[Color]) -> tuple[Coloring, int]:

        population: list[Coloring] = self._create_initial_population(graph, colors)
    
        temperature = self.initial_temperature 

        best_individual, best_fitness = self._selection_with_annealing(population, graph, temperature)

        for _ in range(self.generation_number):
            
            best_individual, best_fitness = self._selection_with_annealing(population, graph, temperature)
            
            if best_fitness == 0:
                return population[best_individual], best_fitness

            new_population = []
            
            for _ in range(self.individual_number // 2):

                parent_1 = population[random.randint(0, len(population) - 1)]
                parent_2 = population[random.randint(0, len(population) - 1)]

                child_1, child_2 = self._crossover(parent_1, parent_2)

                child_1_mutado = self._mutation(child_1, colors)
                child_2_mutado = self._mutation(child_2, colors)

                new_population.extend([child_1_mutado, child_2_mutado])
                
            population = new_population

            temperature *= self.cooling_rate
            
        return population[best_individual], best_fitness

