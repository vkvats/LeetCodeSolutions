# new solution
class Solution:
    def relativeSortArray(self, arr1: [int], arr2: [int]) -> [int]:
        res, cnt = [], Counter(arr1)

        for i in arr2:
            res.extend([i] * cnt.pop(i))

        res.extend(sorted(cnt.elements()))
        return res


# first thought
def relativeSortArray(arr1, arr2):
    frequency = {}
    extra = []
    output =[]
    for num in arr1:
        if num in arr2:
            frequency[num] = frequency.get(num, 0) +1
        else:
            extra.append(num)
    for num in arr2:
        temp = []
        temp.append(num)
        output.extend(temp*frequency[num])
    output.extend(sorted(extra))
    return output
""" Can be solved using ordered dict, try it again after reading ordered dictionary"""

if __name__== '__main__':
    # arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    # arr2 = [2, 1, 4, 3, 9, 6]
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    print(relativeSortArray(arr1, arr2))