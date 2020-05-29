def transpose(A):
    col_num = len(A[0])
    row_num = len(A)
    output = [[None for _ in range(row_num)] for _ in range(col_num)]
    for i in range(row_num):
        for j in range(col_num):
            output[j][i] = A[i][j]
    return output

if __name__ =='__main__':
    A= [[1,2,3],[4,5,6],[7,8,9]]
    A= [[1, 2, 3], [4, 5, 6]]
    print(transpose(A))


    # B = [row[:] for row in A] ## how to make deepcopy of nested list.