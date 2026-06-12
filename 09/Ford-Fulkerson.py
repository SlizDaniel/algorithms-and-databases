class Edge:
    def __init__(self, volume, flag):
        self.volume = volume
        self.flag = flag
        if self.flag == "NR":
            self.rest_value = volume
            self.flow = 0
        elif self.flag == "R":
            self.rest_value = 0
            self.flow = 0
        else:
            raise TypeError("incorrect edge type")
        
    def __repr__(self):
        if self.flag == "NR":
            flag_to_return = False
        else:
            flag_to_return = True
        return(f"{self.volume} {self.flow} {self.rest_value} {flag_to_return}")
    
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

def BFS_algorithm(graph: Graph_matrix|Graph_list, initial_vertex: Vertex, out_vertex: Vertex|None = None):
    visited = set()
    parent = {}
    queue = []
    queue.append(initial_vertex)
    visited.add(initial_vertex)
    out_reached = False
    while(len(queue)>0 and not out_reached):
        current_vertex = queue.pop(0)
        if current_vertex == out_vertex:
            out_reached = True
            break
        vertex_id = graph.get_vertex_id(current_vertex)
        neighbours = graph.neighbours(vertex_id)
        for neighbour, edge in neighbours:
            if type(neighbour) == int:
                neighbour = graph.get_vertex(neighbour)
            if edge is not None and edge.rest_value is not None:
                if neighbour not in visited and edge.rest_value > 0:
                    queue.append(neighbour)
                    visited.add(neighbour)
                    parent[neighbour] = current_vertex
    return parent

def min_volume(graph: Graph_list|Graph_matrix, start_vertex: Vertex, fin_vertex: Vertex, parent: dict):
    if fin_vertex not in parent:
        return 0
    start_vertex_reached = False
    current_parent = parent[fin_vertex]
    edge = graph.get_edge(current_parent, fin_vertex)
    if edge is None:
        return 0
    current_min_volume = edge.rest_value
    while(not start_vertex_reached):
        current_vertex = current_parent
        if current_vertex == start_vertex:
            start_vertex_reached = True
            return current_min_volume
        current_parent = parent[current_vertex]
        current_edge = graph.get_edge(current_parent, current_vertex)
        if current_edge is None:
            return 0
        if current_min_volume>current_edge.rest_value:
            current_min_volume = current_edge.rest_value
    return current_min_volume

def path_augmentation(graph: Graph_list|Graph_matrix, start_vertex: Vertex, fin_vertex: Vertex, parent: dict, min_volume):
    if min_volume == 0 or fin_vertex not in parent:
        return
    current_vertex = fin_vertex
    while current_vertex!=start_vertex:
        current_parrent = parent[current_vertex]
        edge_forward = graph.get_edge(current_parrent, current_vertex)
        edge_backward = graph.get_edge(current_vertex, current_parrent)
        if edge_forward is not None and edge_backward is not None:
            edge_forward.rest_value-=min_volume
            edge_backward.rest_value+=min_volume
            if edge_forward.flag == "NR":
                edge_forward.flow+=min_volume
            elif edge_forward.flag == "R":
                edge_backward.flow-=min_volume
        current_vertex = current_parrent

def ford_fulkerson_algorithm(graph: Graph_list|Graph_matrix, start_vertex: Vertex, fin_vertex: Vertex):
    out_reached = False
    while(not out_reached):
        parent = BFS_algorithm(graph, start_vertex, fin_vertex)
        if fin_vertex not in parent:
            out_reached = True
            break
        min_volume_ = min_volume(graph, start_vertex, fin_vertex, parent)
        path_augmentation(graph, start_vertex, fin_vertex, parent, min_volume_)
    final_flow = 0
    vertices = graph.vertices()
    for v in vertices:
        if type(v)==int:
            v = graph.get_vertex(v)
        if not isinstance(v, (Vertex)):
            raise TypeError("in case v is not type vertex")
        edge = graph.get_edge(v, fin_vertex) 
        if edge is not None and edge.flag == "NR":
            final_flow+=edge.flow
    return final_flow   

def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")


def main():
    graf_0 = [ ('s','u',2), ('u','t',1), ('u','v',3), ('s','v',1), ('v','t',2)]
    graf_1 = [ ('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4) ]
    graf_2 = [ ('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6), ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
    graf_3 = [('s', 'a', 3), ('s', 'd', 2), ('a', 'b', 4), ('b', 'c', 5), ('c', 't', 6), ('a', 'f', 3),  ('f', 't', 3), ('d', 'e', 2), ('e','f',2)]
    graphs_to_test = [graf_0, graf_1, graf_2, graf_3]
    for graph in graphs_to_test:
        list_graph = Graph_list()
        vertexes = {}
        for i in range(0, len(graph)):
            Vertex1 = Vertex(graph[i][0])
            Vertex2 = Vertex(graph[i][1])
            if graph[i][0] not in vertexes:
                vertexes[graph[i][0]] = Vertex1
                list_graph.insert_vertex(Vertex1)
            if graph[i][1] not in vertexes:
                vertexes[graph[i][1]]= Vertex2
                list_graph.insert_vertex(Vertex2)
            edge1 = Edge(graph[i][2],"NR")
            edge2 = Edge(graph[i][2],"R")
            list_graph.insert_edge(Vertex1, Vertex2, edge1)
            list_graph.insert_edge(Vertex2, Vertex1, edge2)
        
        print(ford_fulkerson_algorithm(list_graph,vertexes['s'],vertexes['t']))
        printGraph(list_graph)
        flow_to_return = 0
        if 'a' not in vertexes:
            current_vertex = vertexes['u']
        else:
            current_vertex = vertexes['a']
        neighbours = list_graph.neighbours(current_vertex)
        for neigbour, edge in neighbours:
            if edge is not None:
                if edge.flag == "NR":
                    flow_to_return+=edge.flow
        print(flow_to_return)  
    return

if __name__ == "__main__":
    main()