class Undirected_Graph:
    def __init__(self):
        self.vertices = {}
        self.adjacency_list = []

    def add_vertex(self, vertex):
        if (vertex not in self.vertices):
            next_index = len(self.vertices)
            self.vertices[vertex] = next_index
            self.adjacency_list.append([])

    def add_edge(self, vertex1, vertex2, weight):
        index1 = self.vertices[vertex1]
        index2 = self.vertices[vertex2]
        self.adjacency_list[index1].append((vertex2, weight))
        self.adjacency_list[index2].append((vertex1, weight))

    def get_vertices(self):
        return list(self.vertices.keys())

    def get_neighbours(self, vertex):
        vertex_index = self.vertices[vertex]
        return self.adjacency_list[vertex_index]
    
    def set_neighbours(self, vertex, neighbours):
        vertex_index = self.vertices[vertex]
        self.adjacency_list[vertex_index] = neighbours
