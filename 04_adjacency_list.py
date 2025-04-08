# 04 Напишите функции для создания списка смежности из списка
# ребер. Реализуйте функции для добавления вершины и ребра
# в граф, представленный в виде списка смежности

class AdjacencyListGraph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex not in self.adj_list:
            self.add_vertex(from_vertex)
        if to_vertex not in self.adj_list:
            self.add_vertex(to_vertex)
        self.adj_list[from_vertex].append(to_vertex)

    @classmethod
    def from_edge_list(cls, edge_list):
        graph = cls()
        for from_vertex, to_vertex in edge_list:
            graph.add_edge(from_vertex, to_vertex)
        return graph

    def print_adj_list(self):
        print("Список смежности:")
        for vertex, neighbors in self.adj_list.items():
            print(f"{vertex} -> {neighbors}")

edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "E"), ("D", "E")]
graph = AdjacencyListGraph.from_edge_list(edges)

graph.print_adj_list()

graph.add_vertex("F")
graph.add_edge("E", "F")

print("\nПосле добавления вершины F и ребра E -> F:")
graph.print_adj_list()