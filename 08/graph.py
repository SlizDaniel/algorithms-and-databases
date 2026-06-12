class Vertex:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        if self.key == other.key:
            return True
        return False

    def __hash__(self):
        return hash(self.key)

    def __repr__(self):
        return (f"{self.key}")

class Graph_matrix:
    def __init__(self, value = 0):
        self.graph_matrix = []
        self.vertices_ = []
        self.value = value

    def size(self):
        return len(self.graph_matrix)

    def is_empty(self):
        if len(self.graph_matrix)==0:
            return True
        return False
    
    def insert_vertex(self, vertex: Vertex):
        if vertex in self.vertices_:
            return
        self.vertices_.append(vertex)
        for i in range (0, self.size()):
            self.graph_matrix[i].append(0)
        vertex_to_append = [0 for i in range(0, len(self.vertices_))]
        self.graph_matrix.append(vertex_to_append)            

    def _get_vertex_id(self, vertex: Vertex):
        return self.vertices_.index(vertex)
    
    def insert_edge(self, vertex1: Vertex, vertex2: Vertex, edge=1):
        vertex1_id = self._get_vertex_id(vertex1)
        vertex2_id = self._get_vertex_id(vertex2)
        self.graph_matrix[vertex1_id][vertex2_id] = edge
        self.graph_matrix[vertex2_id][vertex1_id] = edge
        
    def delete_vertex(self, vertex: Vertex):
        vertex_id = self._get_vertex_id(vertex)
        self.vertices_.pop(vertex_id)
        self.graph_matrix.pop(vertex_id)
        for row in self.graph_matrix:
            row.pop(vertex_id)

    def delete_edge(self, vertex1: Vertex, vertex2: Vertex):
        vertex1_id = self._get_vertex_id(vertex1)
        vertex2_id = self._get_vertex_id(vertex2)
        self.graph_matrix[vertex1_id][vertex2_id] = 0
        self.graph_matrix[vertex2_id][vertex1_id] = 0

    def neighbours(self, vertex_id):
        n_list = []
        i = vertex_id
        for i in range(0, self.size()):
            edge = self.graph_matrix[vertex_id][i]
            if edge!=0:
                n_list.append((i, edge))
        return n_list
    
    def vertices(self):
        v_list = []
        for i in range (0, self.size()):
            v_list.append(i)
        return v_list
    
    def get_vertex(self, vertex_id):
        return self.vertices_[vertex_id]
    
class Graph_list:
    def __init__(self):
        self.graph_dict = {}

    def get_vertex(self, vertex):
        return vertex

    def size(self):
        return len(self.graph_dict)
    
    def is_empty(self):
        if self.size() == 0:
            return True
        return False
    
    def insert_vertex(self, vertex: Vertex):
        if vertex in self.graph_dict:
            return
        self.graph_dict[vertex] = {}

    def insert_edge(self, vertex1: Vertex, vertex2: Vertex, edge=1):
        self.graph_dict[vertex1][vertex2] = edge
        self.graph_dict[vertex2][vertex1] = edge

    def delete_vertex(self, vertex: Vertex):
        for k, v in self.graph_dict.items():
            if vertex in v:
                v.pop(vertex)
        self.graph_dict.pop(vertex)

    def delete_edge(self, vertex1: Vertex, vertex2: Vertex):
        self.graph_dict[vertex1].pop(vertex2)
        self.graph_dict[vertex2].pop(vertex1)

    def neighbours(self, vertex_id):
        neighbours_list = []
        neigh = self.graph_dict[vertex_id]
        for k, v in neigh.items():
            neighbours_list.append((k,v))
        return neighbours_list
            
    def vertices(self):
        vertices_list = []
        for keys in self.graph_dict:
            vertices_list.append(keys)
        return vertices_list

import polska

def main(graph:Graph_list|Graph_matrix):
    edges = polska.graf
    for edge in edges:
        v1, v2 = edge
        v1 = Vertex(v1)
        v2 = Vertex(v2)
        graph.insert_vertex(v1)
        graph.insert_vertex(v2)
        graph.insert_edge(v1,v2)
    polska.draw_map(graph)
    graph.delete_vertex(Vertex('K'))
    graph.delete_edge(Vertex('W'), Vertex('E'))
    polska.draw_map(graph)

if __name__ == "__main__":
    graph_matrix = Graph_matrix()
    graph_list = Graph_list()
    main(graph_matrix)
    main(graph_list)