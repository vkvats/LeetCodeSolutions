# new method
# using Enumerate to define the ranking
class Solution:
    def arrayRankTransform(self, arr: [int]) -> [int]:
        rank =  {val: key for key, val in enumerate(sorted(set(arr)),1)}
        return [rank[x] for x in arr]

# using dictionary and setdefault function
def arrayRankTransform(self, A):
    rank = {}
    for a in sorted(A):
        rank.setdefault(a, len(rank) + 1)
    return map(rank.get, A)



def arrayRankTransform(arr):
    output = []
    ranked = {}
    rank = 1
    for num in sorted(arr):
        if num not in ranked:
            ranked[num]= rank
            rank +=1
    for num in arr:
        output.append(ranked[num])
    return output

# from discussion: using set is game changer to use dictionary
# we can give starting point to enumerate with kwargs start=
def arrayRankTransformD(arr):
    ranked = {value: idx for idx, value in enumerate(sorted(set(arr)), start=1)}
    return ([ranked[i] for i in arr])

if __name__ == '__main__':
    # arr = [40,10,20,30]
    # arr = [100, 100, 100]
    arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]
    print(Solution().arrayRankTransform(arr))