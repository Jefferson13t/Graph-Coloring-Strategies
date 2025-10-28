from __future__ import annotations
from typing import Dict, List

class Edge:
    def __init__(self, u: str, v: str, w: float) -> None:
        self.u: str = u
        self.v: str = v
        self.w: float = w

    def __lt__(self, other: Edge) -> bool:
        return self.w < other.w

    def __str__(self) -> str:
        return f"{self.u} -> {self.v} ({self.w})"

    def __repr__(self) -> str:
        return self.__str__()


class Graph:
    def __init__(self) -> None:
        self.graph: Dict[str, List[Edge]] = {}

    def add_edge(self, u: str, v: str, w: float) -> None:
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(Edge(u, v, w))

    def add_undirected_edge(self, u: str, v: str, w: float) -> None:
        self.add_edge(u, v, w)
        self.add_edge(v, u, w)

    def __str__(self) -> str:
        result: List[str] = []
        for u in self.graph:
            for edge in self.graph[u]:
                result.append(str(edge))
        return "\n".join(result)

    def get_edges(self) -> List[Edge]:
        edges: List[Edge] = []
        for u in self.graph:
            edges.extend(self.graph[u])
        return edges

    def out_degree(self, u: str) -> int:
        if u in self.graph:
            return len(self.graph[u])
        raise ValueError(f"Vertex {u} not found in the graph.")

    def in_degree(self, v: str) -> int:
        in_deg: int = 0
        for u in self.graph:
            for edge in self.graph[u]:
                if edge.v == v:
                    in_deg += 1
        return in_deg

    def get_neighbors(self, u: str) -> List[str]:
        if u in self.graph:
            return [edge.v for edge in self.graph[u]]
        raise ValueError(f"Vertex {u} not found in the graph.")
