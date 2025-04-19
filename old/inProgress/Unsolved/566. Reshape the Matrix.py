class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        one_d = []
        for arr in nums:
            one_d.extend(arr)
        if len(one_d) < r*c: return nums
        output = []
        for row_num in range(r):
            output.append(one_d[row_num*c : row_num*c + c])
        return output
# Solution from leetcode
class SolutionF1:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(nums)
        col = len(nums[0])
        if r * c != row * col:
            return nums
        else:
            w = []
            for i in range(row):
                for j in range(col):
                    w.append(nums[i][j])

            ret = []
            t = 0
            for i in range(r):
                temp = []
                for j in range(c):
                    temp.append(w[t])
                    t += 1
                ret.append(temp)
            return ret

#Solution from leetcode
class SolutionF2:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        A = [x for row in nums for x in row]
        if r*c==len(A):
            return[A[i*c : (i + 1)*c] for i in range(r)]
        else:
            return nums