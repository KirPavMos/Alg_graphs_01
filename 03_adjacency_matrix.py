# 03 Напишите функцию для создания матрицы смежности из
# списка ребер. Реализуйте функции для добавления вершины
# и ребра в граф, представленный в виде матрицы смежности

class AdjacencyMatrixGraph:
    def __init__(self):
        self.vertices = []
        self.adj_matrix = []

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            for row in self.adj_matrix:
                row.append(0)
            new_row = [0] * len(self.vertices)
            self.adj_matrix.append(new_row)

    def add_edge(self, from_vertex, to_vertex, weight=1):
        if from_vertex not in self.vertices:
            self.add_vertex(from_vertex)
        if to_vertex not in self.vertices:
            self.add_vertex(to_vertex)

        from_idx = self.vertices.index(from_vertex)
        to_idx = self.vertices.index(to_vertex)
        self.adj_matrix[from_idx][to_idx] = weight

    @classmethod
    def from_edge_list(cls, edge_list):
        graph = cls()
        for from_vertex, to_vertex in edge_list:
            graph.add_edge(from_vertex, to_vertex)
        return graph

    def print_matrix(self):
        print("Матрица смежности:")
        print("   ", "  ".join(self.vertices))
        for i, row in enumerate(self.adj_matrix):
            print(f"{self.vertices[i]} |", "  ".join(map(str, row)))

edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "E"), ("D", "E")]
graph = AdjacencyMatrixGraph.from_edge_list(edges)

graph.print_matrix()

graph.add_vertex("F")
graph.add_edge("E", "F")

print("\nПосле добавления вершины F и ребра E -> F:")
graph.print_matrix()