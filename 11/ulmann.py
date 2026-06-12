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
    
    def size_(self):
        return (len(self.graph_matrix), len(self.graph_matrix[0]))
    
    def vertex_deg (self, vertex):
        neighbours = self.neighbours(vertex)
        return len(neighbours)
    
class Matrix:
    def __init__(self, matrix, val = 0):
        if isinstance (matrix, tuple):
            rows, cols = matrix
            matrix_ = []
            for i in range (rows):
                row = []
                for j in range (cols):
                    row.append(val)
                matrix_.append(row)
            self.__matrix = matrix_
        else:
            self.__matrix = matrix
            
    def __str__(self):
        output = ""
        for row in self.__matrix:
             output+= str(row)+"\n"
        return output
        
    def __eq__(self, other):
        m1 = self.__matrix
        m2 = other._Matrix__matrix
        if self.size() != other.size():
            return False
        else:
            rows = self.size()[0]
            cols = self.size()[1]
            for i in range (rows):
                for j in range (cols):
                    if m1[i][j]!=m2[i][j]:
                        return False
            return True
            
    def __add__(self, other):
        m1 = self.__matrix
        m2 = other._Matrix__matrix
        if self.size() != other.size():
            raise TypeError("Incorrect matrix shape!")
        rows = self.size()[0]
        cols = self.size()[1]
        matrix_ = []
        for i in range (rows):  
            row = []
            for j in range (cols):
                row.append(m1[i][j] + m2[i][j])
            matrix_.append(row)
        return Matrix(matrix_)
        
    def __getitem__(self, index):
        return self.__matrix[index]
        
    def __mul__(self, other):
        m1 = self.__matrix
        m2 = other._Matrix__matrix
        if self.size()[1] != other.size()[0]:
            raise TypeError("Incorrect matrix shape!")
        mul_matrix = Matrix((self.size()[0], other.size()[1]))
        for i in range (0, mul_matrix.size()[0]):
            for j in range (0, mul_matrix.size()[1]):
                for k in range (0, self.size()[1]):
                    mul_matrix[i][j] += m1[i][k] * m2[k][j]
        return mul_matrix
               
    def size(self):
        rows = len(self.__matrix)
        cols = len(self.__matrix[0])
        return(rows, cols)
    
    def copy_(self):
        copied_matrix = []
        for row in self.__matrix:
            copied_matrix.append(row.copy())
        return Matrix(copied_matrix)
        
def transpose_matrix(matrix):
    if not isinstance (matrix, Matrix):
        raise TypeError("This object is not a matrix")
    transposed_matrix = Matrix((matrix.size()[1], matrix.size()[0]))
    for i in range (0, matrix.size()[1]):
        for j in range (0, matrix.size()[0]):
            transposed_matrix[i][j] = matrix[j][i]
    return transposed_matrix

def ullman(used, current_row: int, M: Matrix, wywolan, P: Graph_matrix, G: Graph_matrix, izo):
    if current_row == M.size()[0]:
        P_pairs = []
        P_vertices = P.vertices()
        for vertex in P_vertices:
            neighbours = P.neighbours(vertex)
            for neighbour in neighbours:
                P_pairs.append((vertex, neighbour[0]))
        for pair in P_pairs:
            i = pair[0]
            j=pair[1]
            for _ in range (M.size()[1]):
                if M[i][_]==1:
                    G_vert = _
                if M[j][_]==1:
                    G_vert2 = _
            G_neighbours = [n[0] for n in G.neighbours(G_vert)]
            if G_vert2 in G_neighbours:
                continue
            else:
                break
        else:
            izo+=1
        return izo, wywolan
    
    for col in range (M.size()[1]):
        if used[col]==False:
            used[col]=True
            for j in range (M.size()[1]):
                if j==col:
                    M[current_row][j]=1
                else:
                    M[current_row][j]=0
            wywolan+=1
            izo, wywolan = ullman(used, current_row+1, M, wywolan, P, G, izo)
            used[col]=False
    return izo, wywolan

def ullman_2(used, current_row: int, M: Matrix, wywolan, P: Graph_matrix, G: Graph_matrix, izo):
    if current_row == M.size()[0]:
        P_pairs = []
        P_vertices = P.vertices()
        for vertex in P_vertices:
            neighbours = P.neighbours(vertex)
            for neighbour in neighbours:
                P_pairs.append((vertex, neighbour[0]))
        for pair in P_pairs:
            i = pair[0]
            j=pair[1]
            for _ in range (M.size()[1]):
                if M[i][_]==1:
                    G_vert = _
                if M[j][_]==1:
                    G_vert2 = _
            G_neighbours = [n[0] for n in G.neighbours(G_vert)]
            if G_vert2 in G_neighbours:
                continue
            else:
                break
        else:
            izo+=1
        return izo, wywolan
    for col in range (M.size()[1]):
        if used[col]==False and M[current_row][col]!=0:
            M_ = M.copy_()
            used[col]=True
            for j in range (M_.size()[1]):
                if j==col:
                    M_[current_row][j]=1
                else:
                    M_[current_row][j]=0
            wywolan+=1
            izo, wywolan = ullman_2(used, current_row+1, M_, wywolan, P, G, izo)
            used[col]=False
    return izo, wywolan            

def create_M0_matrix(P: Graph_matrix, G: Graph_matrix) -> Matrix:
    rows = P.size()
    cols = G.size()
    M = Matrix((rows,cols))
    for i in range (rows):
        for j in range (cols):
            deg_i = P.vertex_deg(i)
            deg_j = G.vertex_deg(j)
            if deg_j>=deg_i:
                M[i][j]=1
    return M

def create_graph_from_array(graph_: Graph_matrix, arr):
    for i in range (0, len(arr)):
        Vertex1 = Vertex(arr[i][0])
        Vertex2 = Vertex(arr[i][1])
        distance = arr[i][2]
        graph_.insert_vertex(Vertex1)
        graph_.insert_vertex(Vertex2)
        graph_.insert_edge(Vertex1,Vertex2,distance)
        graph_.insert_edge(Vertex2,Vertex1,distance)

def create_graph_from_array_alphabetic_edges(graph_: Graph_matrix, arr):
    vertices_set = set()
    for i in range(len(arr)):
        vertices_set.add(arr[i][0])
        vertices_set.add(arr[i][1])
    sorted_vertices = sorted(list(vertices_set))
    for v_name in sorted_vertices:
        graph_.insert_vertex(Vertex(v_name))
    for i in range(len(arr)):
        Vertex1 = Vertex(arr[i][0])
        Vertex2 = Vertex(arr[i][1])
        distance = arr[i][2]
        graph_.insert_edge(Vertex1, Vertex2, distance)
        graph_.insert_edge(Vertex2, Vertex1, distance)


def main():

    graph_G = [ ('A','B',1), ('B','F',1), ('B','C',1), ('C','D',1), ('C','E',1), ('D','E',1)]
    graph_P = [ ('A','B',1), ('B','C',1), ('A','C',1)]

    grafG_a = Graph_matrix()
    grafP_a = Graph_matrix()
    create_graph_from_array_alphabetic_edges(grafG_a, graph_G)
    create_graph_from_array_alphabetic_edges(grafP_a, graph_P)

    M = Matrix((3,6))
    used_ = [False for _ in range(M.size()[1])]
    wywolan = 0
    izometri = 0
    wynik_=ullman(used_, 0, M, wywolan, grafP_a, grafG_a, izometri)

    # for i in range(5):
    #     print('\n')
    grafG = Graph_matrix()
    grafP = Graph_matrix()
    create_graph_from_array(grafG, graph_G)
    create_graph_from_array(grafP, graph_P)
    
    M = Matrix((3,6))
    used_ = [False for _ in range(M.size()[1])]
    wywolan = 0
    wynik = ullman(used_, 0, M, wywolan, grafP, grafG, izometri)
    # print(wynik_)
    print(wynik)

    M = create_M0_matrix(grafP_a, grafG_a)
    used_ = [False for _ in range(M.size()[1])]
    wywolan = 0
    wynik_=ullman_2(used_, 0, M, wywolan, grafP_a, grafG_a, izometri)

    # for i in range(5):
    #     print('\n')
    
    M = create_M0_matrix(grafP, grafG)
    used_ = [False for _ in range(M.size()[1])]
    wywolan = 0
    wynik = ullman_2(used_, 0, M, wywolan, grafP, grafG, izometri)
    # print(wynik_)
    print(wynik)

if __name__ == "__main__":
    main()