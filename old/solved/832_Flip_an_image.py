# Understanding list comprehension
def list_comprehension(A):
    #method 1 # Doubly nested list
    m1 = [[val for val in row[::-1]] for row in A] # format for nested list
    #method 2 # 1-D list
    m2 = [val for row in A for val in row[::-1]] # format for single list
    #method 3
    # m3 = [val for val in row for row in A] # wrong implementation
    #Method 4 # generating 3D list
    m4 = [[[val for val in range(3)] for _ in range(4)] for _ in range(5)]
    #method 5 Converting 3D list into 1D
    m5 = [val for f in A for x in f for val in x]
    #method 6 Converting 3D into 2D
    m6 = [[val for val in x] for f in A for x in f]
    return m4




# first thought
def flipAndInvertImage(A):
    output =[]
    for row in A:
        out1 = []
        for element in reversed(row):
            element = 1- element
            out1.append(element)
        output.append(out1)
    return output

# second thought Numpy
import numpy as np
def flipAndInvertImageNP(A):
    flipped = np.array([x[::-1] for x in A])
    flipped = np.abs(flipped - 1)
    return flipped

# trying list comprehension: Nice method
def flipAndInvertImageLC(A):
    return [[1-element for element in row[::-1]] for row in A]

if __name__ == '__main__':
    # A = [[1,1,0]]
    # A = [[1,2,3],[4,5,6],[7,8,9]]
    # A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    A = [[[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]]
    print(list_comprehension(A))