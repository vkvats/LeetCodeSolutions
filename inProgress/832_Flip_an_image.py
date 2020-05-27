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
    A = [[1,1,0],[1,0,1],[0,0,0]]
    # A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    print(flipAndInvertImageLC(A))