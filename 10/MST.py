class Edge:
    def __init__(self, value):
        self.value = value
        
    def __repr__(self):
        return f"{self.value}"
    
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

    def get_edge(self, vertex1: Vertex, vertex2: Vertex):
        vertex1_id = self.get_vertex_id(vertex1)
        vertex2_id = self.get_vertex_id(vertex2)
        edge = self.graph_matrix[vertex1_id][vertex2_id]
        if edge == 0:
            return None
        return edge

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

    def get_vertex_id(self, vertex: Vertex):
        return self.vertices_.index(vertex)
    
    def insert_edge(self, vertex1: Vertex, vertex2: Vertex, edge=1):
        vertex1_id = self.get_vertex_id(vertex1)
        vertex2_id = self.get_vertex_id(vertex2)
        self.graph_matrix[vertex1_id][vertex2_id] = edge
        
    def delete_vertex(self, vertex: Vertex):
        vertex_id = self.get_vertex_id(vertex)
        self.vertices_.pop(vertex_id)
        self.graph_matrix.pop(vertex_id)
        for row in self.graph_matrix:
            row.pop(vertex_id)

    def delete_edge(self, vertex1: Vertex, vertex2: Vertex):
        vertex1_id = self.get_vertex_id(vertex1)
        vertex2_id = self.get_vertex_id(vertex2)
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

    def get_edge(self, vertex1, vertex2):
        if vertex1 not in self.graph_dict:
            return None
        if vertex2 not in self.graph_dict[vertex1]:
            return None
        return self.graph_dict[vertex1][vertex2]

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

    def insert_edge(self, vertex1: Vertex, vertex2: Vertex, edge:Edge|int=1):
        self.graph_dict[vertex1][vertex2] = edge

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
    
    def get_vertex_id(self, vertex):
        return vertex
    
    def insert_2ways_edge(self, vertex1: Vertex, vertex2: Vertex, length:Edge|int):
        self.insert_edge(vertex1,vertex2,length)
        self.insert_edge(vertex2,vertex1,length)

def prim_MST(graph: Graph_list):
    size_of_tree = 0
    vertexes = graph.vertices()
    intree = {}
    distance = {}
    parent = {}
    Mst_ = Graph_list()
    for vertex in vertexes:
        intree[vertex] = False
        distance[vertex] = float('inf')
        parent[vertex] = None
        Mst_.insert_vertex(vertex)
    current_vertex = vertexes[0]
    distance[current_vertex]=0
    while(current_vertex is not None and intree[current_vertex] == False):
        intree[current_vertex] = True
        if parent[current_vertex] is not None:
            dist = distance[current_vertex]
            Mst_.insert_2ways_edge(current_vertex,parent[current_vertex],dist)
            size_of_tree+=dist
        neighbours = graph.neighbours(current_vertex)
        for neighbour, edge in neighbours:
            if intree[neighbour] == False:
                if edge < distance[neighbour]:
                    distance[neighbour] = edge
                    parent[neighbour] = current_vertex
        next_vertex = None
        next_distance = float('inf')
        for vertex in vertexes:
            if intree[vertex]==False and distance[vertex]<next_distance:
                next_distance = distance[vertex]
                next_vertex = vertex
        current_vertex = next_vertex
    return  Mst_, size_of_tree

def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")

def main():
    graf = [ ('A','B',4), ('A','C',1), ('A','D',4),
         ('B','E',9), ('B','F',9), ('B','G',7), ('B','C',5),
         ('C','G',9), ('C','D',3),
         ('D', 'G', 10), ('D', 'J', 18),
         ('E', 'I', 6), ('E', 'H', 4), ('E', 'F', 2),
         ('F', 'H', 2), ('F', 'G', 8),
         ('G', 'H', 9), ('G', 'J', 8),
         ('H', 'I', 3), ('H','J',9),
         ('I', 'J', 9)
        ]
    graf_ = Graph_list()
    for i in range (0, len(graf)):
        Vertex1 = Vertex(graf[i][0])
        Vertex2 = Vertex(graf[i][1])
        distance = graf[i][2]
        graf_.insert_vertex(Vertex1)
        graf_.insert_vertex(Vertex2)
        graf_.insert_2ways_edge(Vertex1,Vertex2,distance)

    Mst_, distance_ = prim_MST(graf_)
    printGraph(Mst_)
    # print(distance_)

    return

if __name__ == "__main__":
    main()