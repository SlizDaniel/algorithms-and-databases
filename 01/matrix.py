
#Skończone

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
        
def transpose_matrix(matrix):
    if not isinstance (matrix, Matrix):
        raise TypeError("This object is not a matrix")
    transposed_matrix = Matrix((matrix.size()[1], matrix.size()[0]))
    for i in range (0, matrix.size()[1]):
        for j in range (0, matrix.size()[0]):
            transposed_matrix[i][j] = matrix[j][i]
    return transposed_matrix
        
            
def main():
    m1 = Matrix([[1, 0, 2],
                [-1,3,1]])
    print (transpose_matrix(m1))
    
    m2 = Matrix((2,3), 1)
    
    print(m1+m2)
    
    m3 = Matrix([[3,1],
                 [2,1],
                 [1,0]])
    print(m1*m3)
    
if __name__ == "__main__":
    main()
    
                    
            