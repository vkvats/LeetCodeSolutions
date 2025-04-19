# Without using string conversion
def findNumbers(self, nums: [int]) -> int:
    total_count = 0
    for num in nums:
        count = 0
        while num >= 1:
            num = num // 10
            count += 1
        if count % 2 == 0:
            total_count += 1
    return total_count

# same work in one line
def findNumbers(nums):
    return sum([1 for num in nums if len(str(num)) % 2 ==0])

if __name__ == "__main__":
    nums = [5553,9013,4823,1771]
    print(findNumbers(nums))