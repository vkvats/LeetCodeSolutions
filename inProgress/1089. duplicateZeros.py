def duplicateZeros(arr):
    index = 0
    N = len(arr)
    while index < N:
        if arr[index] ==0:
            arr.pop()
            arr.insert(index,0)
            index +=1
        index +=1
    return arr

# best solution: uses deque
def duplicateZerosBest(arr):
    """
    Do not return anything, modify arr in-place instead.
    """
    from collections import deque

    seen = deque()

    for n in arr:
        seen.append(n)

    curr = 0

    while curr < len(arr):
        item = seen.popleft()
        arr[curr] = item

        if item == 0 and curr != len(arr) - 1:
            arr[curr + 1] = item
            curr += 1

        curr += 1
if __name__ =='__main__':
    arr = [1,0,2,3,0,4,5,0]
    print(duplicateZeros(arr))

