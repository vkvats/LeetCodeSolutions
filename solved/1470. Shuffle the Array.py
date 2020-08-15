# New method
# using ZIP function
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = []
        for i,j in zip(nums[:n],nums[n:]):
            output += [i,j]
        return output



def shuffle(nums, n):
    output = []
    for index in range(n):
        output.append(nums[index])
        output.append(nums[index+n])
    return output

# best solution on leetcode
def shuffleBest(nums,n):
    soln = []
    for i in range(2 * n):
        if i % 2 == 0:
            soln.append(nums[i // 2])
        else:
            soln.append(nums[n + i // 2])

    return soln


if __name__ == '__main__':
    # nums = [2, 5, 1, 3, 4, 7]
    # n = 3
    nums = [1, 2, 3, 4, 4, 3, 2, 1]
    n = 4
    print(shuffle(nums, n))
