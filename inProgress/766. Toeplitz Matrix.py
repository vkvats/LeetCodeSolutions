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
    matrix = [
        [1, 2],
        [2, 2]
    ]

    print(isToeplitzMatrix(matrix))
