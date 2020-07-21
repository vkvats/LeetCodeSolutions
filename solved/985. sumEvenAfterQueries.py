def sumEvenAfterQueries(A, queries):
    output = []
    sum = 0
    for num in A:
        if num % 2 == 0:
            sum += num

    for value, index in queries:
        a_idx = A[index]
        if a_idx % 2 == 0:
            sum -= a_idx
        a_idx = a_idx + value
        A[index] = a_idx
        if a_idx % 2 == 0:
            sum += a_idx
        output.append(sum)
    return output

if __name__ == '__main__':
    A = [1, 2, 3, 4]
    queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
    print(sumEvenAfterQueries(A, queries))