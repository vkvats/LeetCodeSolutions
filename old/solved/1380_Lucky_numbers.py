# first thought
def luckyNumbers(matrix):
    lucky = []
    for row in matrix:
        row_min = min(row)
        col_index = row.index(row_min)
        col =[]
        for row2 in matrix:
            col.append(row2[col_index])
            col_max = max(col)
        if row_min == col_max:
            lucky.append(row_min)
    return lucky

# from discussion
def luckyNumbersD(matrix):
    a = [min(arr) for arr in matrix]
    # to get all columns in a tuple
    # c = [val for val in zip(*matrix)] # zip unpacking
    # c = map(list, zip(*matrix))
    # c = [val for val in c]
    b = [max(arr) for arr in zip(*matrix)]
    # using zip(*arg) does the job of unzipping, in this case it will give colum values in tuples.
    return [i for i in a if i in b]

if __name__ == '__main__':
    # matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
    matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
    print(luckyNumbersD(matrix))
