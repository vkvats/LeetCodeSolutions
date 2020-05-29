def sumEvenAfterQueries(A, queries):
    output = []
    for value, index in queries:
        A[index] = A[index] + value
        evenSum = sum([x if x%2 ==0 else 0 for x in A])
        output.append(evenSum)
    return output

if __name__ == '__main__':
    A = [1, 2, 3, 4]
    queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
    print(sumEvenAfterQueries(A, queries))