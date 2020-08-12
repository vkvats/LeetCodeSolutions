# new solutin
# using two pointer
class Solution:
    def majorityElement(self, nums: [int]) -> int:
        nums.sort()
        slow, fast, n = 0,0, len(nums)
        while fast < n:
            slow_num, fast_num = nums[slow], nums[fast]
            while slow_num == fast_num:
                fast += 1
                if fast == n: break
                fast_num = nums[fast]
            if slow_num != fast_num or fast == n:
                if fast - slow > n/2: return slow_num
                else: slow = fast

# using the condition and checking similarity at that index
class Solution:
    def majorityElement(self, nums: [int]) -> int:
        nums.sort()
        n = len(nums)//2
        for i in range(len(nums)):
            if nums[i] == nums[i+ n]: return nums[i]

# Intuitive solution, the majarity element should always exists at the middle
class Solution:
    def majorityElement(self, nums: [int]) -> int:
        return sorted(nums)[len(nums)//2]


def majorityElement(nums):
    frequency_count = {}
    for num in nums:
        frequency_count[num] = frequency_count.get(num, 0) +1
        if frequency_count[num] > len(nums)//2:
            return num

# using counter from collection
def majorityElementCounter(nums):
    from collections import Counter
    return Counter(nums).most_common(1)[0][0]

if __name__ == '__main__':
    nums = [2,2,1,1,1,2,2]
    # nums= [3,2,3]
    print(majorityElement(nums))