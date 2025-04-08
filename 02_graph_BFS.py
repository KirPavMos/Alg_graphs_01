# 02 Напишите функцию для обхода ориентированного графа
# в ширину (Breadth-First Search, BFS)

from collections import deque

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

    def bfs(self, start_vertex):
        if start_vertex not in self.adjacency_list:
            return []

        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)
        result = []

        while queue:
            current_vertex = queue.popleft()
            result.append(current_vertex)

            for neighbor in self.adjacency_list[current_vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result

    def __str__(self):
        return "\n".join(
            f"{vertex} -> {neighbors}"
            for vertex, neighbors in self.adjacency_list.items()
        )

graph = DirectedGraph()

graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")

graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "E")
graph.add_edge("D", "E")

print("Ориентированный граф:")
print(graph)

start_vertex = "A"
bfs_result = graph.bfs(start_vertex)
print(f"\nBFS, начиная с {start_vertex}: {bfs_result}")