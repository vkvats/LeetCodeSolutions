# New solution without using array
class Solution:
    def findTheDistanceValue(self, arr1: [int], arr2: [int], d: int) -> int:
        count = 0
        n = len(arr2)
        for a1 in arr1:
            tmp = 0
            for a2 in arr2:
                if abs(a1 - a2) > d:
                    tmp += 1
                else:
                    break
            if tmp == n: count += 1
        return count


# first thought: using dictionary to story count and then fetcing it as per sorted order but,
# #two keys becomes same. so can't be done using dict.

# Second thought:
def kWeakestRows(mat, K):
    strength = [sum(row) for row in mat]
    order = [i[0] for i in sorted(enumerate(strength), key=lambda x: x[1])]
    return order[:k]

if __name__ == '__main__':
    mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
    k = 3
    print(kWeakestRows(mat, k))