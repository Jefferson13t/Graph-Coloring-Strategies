import numpy as np
import matplotlib.pyplot as plt
import time as tm
from classes.strategies.strategies import ColoringStrategy
from classes.graph import Graph
from classes.coloring import Color

class ColoringStrategiesBenchmark:

    def _calculate_strategy_execution_time(self, strategy: ColoringStrategy, graph: Graph, colors: list[Color]) -> float:
        start_time = tm.time()
        _, __ = strategy.color(graph, colors)
        end_time = tm.time()
        return end_time - start_time


    def _plot_execution_times(self, strategies: list[ColoringStrategy], times: dict[ColoringStrategy, list[float]], filename: str) -> None:
        plt.figure(figsize=(10, 6))

        all_times = np.concatenate([times[strategy] for strategy in strategies if len(times[strategy]) > 0])
        unique_times = np.sort(np.unique(all_times))

        if len(unique_times) == 0:
            print("There is no time data to show.")
            return

        for strategy in strategies:
            strategy_times = np.array(times[strategy])

            if len(strategy_times) == 0:
                plt.plot(unique_times, np.zeros_like(unique_times), label=strategy, marker='o')
                continue

            percentages = [(strategy_times <= t).sum() / len(strategy_times) * 100 for t in unique_times]
            plt.plot(unique_times, percentages, label=strategy, marker='o')

        plt.xlabel('Time (seconds)')
        plt.ylabel('% of solutions found')
        plt.title('Solution Distribution found over time')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(filename)
        plt.show()


    def evaluate_strategies(self, graph: Graph, colors: list[Color], runs: int, filename: str, strategies: list[ColoringStrategy]) -> None:
        strategy_times: dict[ColoringStrategy, list[float]] = {}

        for strategy in strategies:
            strategy_times[strategy] = []

        for strategy in strategies:
            for i in range(runs):
                print(f"Evaluating {strategy} iteration {i} of {runs}", end='\r', flush=True)
                time = self._calculate_strategy_execution_time(strategy, graph, colors)
                strategy_times[strategy].append(time)

        self._plot_execution_times(strategies, strategy_times, filename)
