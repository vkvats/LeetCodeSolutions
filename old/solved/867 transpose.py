# For square matrix ONLY
class Solution:
    def transpose(self, A: [[int]]) -> [[int]]:
        for i in range(len(A)):
            for j in range(i+1, len(A[0])):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        return A

# for all types of matricies
# using zip unpacking
class Solution:
    def transpose(self, A):
        return zip(*A)

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