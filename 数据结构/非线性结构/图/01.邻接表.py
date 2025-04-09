class Vertex:
    def __init__(self,key):
        self.key = key
        self.neighbors = {}

    def get_neighbor(self,key):
        return self.neighbors.get(key,None)

    def add_neighbor(self,key,neighbor):
        self.neighbors[key] = neighbor

    def __repr__(self):
        return f"Vertex({self.key})"

    def __str__(self):
        return f"Vertex({self.key})"

    def get_neighbors(self):
        return self.neighbors.keys()

    def get_key(self):
        return self.key

    class Graph:
        def __init__(self,vertices):
            self.vertices = {}

        def set_vertices(self,key):
            self.vertices[key] = Vertex(key)

        def get_vertex(self,key):
            return self.vertices.get(key,None)

        def add_edge(self,from_vert,to_vert,weight):
            if from_vert not in self.vertices:
                self.vertices[from_vert] = Vertex(from_vert)
            if to_vert not in self.vertices:
                self.vertices[to_vert] = Vertex(to_vert)
            self.vertices[from_vert].add_neighbor(to_vert,weight)

        def get_vertices(self):
            return self.vertices.keys()

        def __iter__(self):
             return iter(self.vertices.values())























