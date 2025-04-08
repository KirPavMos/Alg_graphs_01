# 01 Напишите класс DirectedGraph, который реализует
# ориентированный граф с методами добавления вершины
# (add_vertex) и добавления ребра (add_edge). Протестируйте
# реализацию на примере

class DirectedGraph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex not in self.adjacency_list:
            self.add_vertex(from_vertex)
        if to_vertex not in self.adjacency_list:
            self.add_vertex(to_vertex)
        self.adjacency_list[from_vertex].append(to_vertex)

    def __str__(self):
        return "\n".join(
            f"{vertex} -> {neighbors}"
            for vertex, neighbors in self.adjacency_list.items()
        )

graph = DirectedGraph()

graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")

graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("C", "A")
graph.add_edge("A", "C")

print("Ориентированный граф:")
print(graph)