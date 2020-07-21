import collections
class Solution:
    def findLHS(self, nums: [int]) -> int:
        v = collections.Counter(nums)
        output = 0
        for i in v:
            if i-1 in v:
                output = max(output, v[i]+v[i-1])
        return output

# Solution from leetcode
class SolutionFast1:
    def findLHS(self, nums: [int]) -> int:
        c=collections.Counter(nums)
        sum=0
        for i in c:
            if i+1 in c and c[i+1]+c[i]>sum:
                sum=c[i+1]+c[i]
        return sum


if __name__ == '__main__':
    # nums = [1,3,2,2,5,2,3,7]
    nums = [1,1,1,1,2]
    # nums = [1,2,3,3,1,-14,13,4]
    # nums= [3,2,2,3,2,1,3,3,3,-2,0,3,2,1,0,3,1,0,1,3,0,3,3]

    print(Solution().findLHS(nums))