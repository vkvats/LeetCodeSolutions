# first thought
def replaceElements(arr):
    for i in range(len(arr)-1):
        arr[i] = max(arr[i+1:])
    arr[-1] = -1
    return arr
# from discussion
def replaceElementsFAST(arr):
    max_so_far = -1
    for i, current_num in enumerate(arr[::-1]):
        candidate = current_num
        arr[i] = max_so_far
        max_so_far = max(max_so_far, candidate)
    return arr[::-1]

if __name__ == '__main__':
    arr = [17, 18, 5, 4, 6, 1]
    print(replaceElements(arr))