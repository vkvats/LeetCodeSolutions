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