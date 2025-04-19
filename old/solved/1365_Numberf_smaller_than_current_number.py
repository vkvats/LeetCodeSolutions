
# Naive solution
def smallerNumbersThanCurrent(nums):
    output = []
    for num in nums:
        count = 0
        for num2 in nums:
            if num != num2 and num2 < num:
                count +=1
        output.append(count)
    return output

# using filter function
def using_filter(nums):
    output = []
    for num in nums:
        val = filter(lambda x: x < num, nums)
        output.append(len([v for v in val]))
    return output

# using dictionary and enumerate
class Solution:
    def smallerNumbersThanCurrent(self, nums: [int]) -> [int]:
        indices = {}
        for idx, num in enumerate(sorted(nums)): # O(n.log n) + O(n)
            # set the default value to the first index encountered
            # if key in already present, it does nothing.
            indices.setdefault(num,idx)
            # # this is same as doing
            # if num not in count:
            #     count[num] = idx
        return [indices[num] for num in nums]


if __name__ == '__main__':
    nums = [8, 1, 2, 2, 3]
    # nums = [7, 7, 7, 7]
    print(using_filter(nums))
