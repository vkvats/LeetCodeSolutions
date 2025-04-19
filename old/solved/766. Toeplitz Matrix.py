# new solution
# Using properties of diagonal index
# property 1: right to left diagonal= sum of indicies are same
#  property 2: left to right diagonal => difference of indicies are same. i.e. row - col = constant
def isToeplitzMatrix1(matrix):
    d = {}
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if r-c not in d:
                d[r-c] = matrix[r][c]
            else:
                if d[r-c] != matrix[r][c]:
                    return False
    else:
        return True

# using ALL function
 def isToeplitzMatrix(m):
        return all(m[i][j] == m[i+1][j+1] for i in range(len(m)-1) for j in range(len(m[0])-1))



def isToeplitzMatrix(matrix):
    col_num = len(matrix[0])
    row_num = len(matrix)
    for i in range(1, row_num):
        for j in range(1, col_num):
            if matrix[i][j] != matrix[i-1][j-1]:
                return False
    return True


if __name__ =='__main__':
    matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    # matrix = [
    #     [1, 2],
    #     [2, 2]
    # ]

    print(isToeplitzMatrix1(matrix))
