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
    
    def __setitem__(self, index, value):
        self.__matrix[index] = value
        
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
    
def det_2x2(matrix_: Matrix):
    if matrix_.size()[0] != 2 or matrix_.size()[1] != 2:
        raise TypeError("This is not a 2x2 matrix")
    wyznacznik = matrix_[0][0]*matrix_[1][1]-matrix_[1][0]*matrix_[0][1]
    return wyznacznik

def det_2x2_coef (a00, a10, a01, a11):
    return a00*a11-a01*a10

def chio_reduction(matrix_: Matrix):
    if matrix_.size()[0] != matrix_.size()[1]:
        raise TypeError("Not a square matrix!")
    i = 1
    pivot = False
    unsolvable = False
    while(matrix_[0][0]==0):
        if(i>=matrix_.size()[1]):
            unsolvable = True
            return None, 0, False, True
        matrix_[0], matrix_[i] = matrix_[i], matrix_[0]
        i+=1
        if(not pivot):
            pivot = True
        else:
            pivot = False
    currentRowLength = matrix_.size()[0]
    nextRowLength = currentRowLength - 1
    nextColLength = nextRowLength
    nextMatrix = []
    nextRow = []
    for j in range (0,nextColLength):
        nextRow = []
        for i in range (0, nextRowLength):
            a00 = matrix_[0][0]
            a10 = matrix_[1+j][0]
            a01 = matrix_[0][1+i]
            a11 = matrix_[1+j][1+i]
            nextCoef = det_2x2_coef(a00, a10, a01, a11)
            nextRow.append(nextCoef)
        nextMatrix.append(nextRow)
    resultMatrix = Matrix(nextMatrix)
    multiplier = 1/(matrix_[0][0]**(currentRowLength-2))
    if(pivot):
        multiplier*=(-1)
    return resultMatrix , multiplier, pivot, unsolvable

def chio(matrix_:Matrix):
    if matrix_.size()[0] != matrix_.size()[1]:
        raise TypeError("Not a square matrix!")
    resultMultiplier = 1
    while(matrix_.size()[0]>2):           
        reducedMatrix, multiplier, pivot, unsolvable = chio_reduction(matrix_)
        if(unsolvable or reducedMatrix is None):
            return 0
        resultMultiplier *= multiplier
        matrix_=reducedMatrix
    det = det_2x2(matrix_)   
    result = resultMultiplier * det
    return result


def main():
    A = Matrix([
    [5 , 1 , 1 , 2 , 3],
    [4 , 2 , 1 , 7 , 3],
    [2 , 1 , 2 , 4 , 7],
    [9 , 1 , 0 , 7 , 0],
    [1 , 4 , 7 , 2 , 2]
    ])
    B = Matrix  ([
     [0 , 1 , 1 , 2 , 3],
     [4 , 2 , 1 , 7 , 3],
     [2 , 1 , 2 , 4 , 7],
     [9 , 1 , 0 , 7 , 0],
     [1 , 4 , 7 , 2 , 2]
    ])
    C= Matrix([
     [0 , 0 , 0 , 0 , 0],
     [4 , 2 , 1 , 7 , 3],
     [2 , 1 , 2 , 4 , 7],
     [9 , 1 , 0 , 7 , 0],
     [1 , 4 , 7 , 2 , 2]
    ])
    D = Matrix(  [
     [0 , 1 , 1 , 2 , 3],
     [0 , 2 , 1 , 7 , 3],
     [0 , 1 , 2 , 4 , 7],
     [0 , 1 , 0 , 7 , 0],
     [0 , 4 , 7 , 2 , 2]
    ])
    print(chio(A))
    print(chio(B))
    print(chio(C))
    print(chio(D))

    

if __name__ == "__main__":
    main()
