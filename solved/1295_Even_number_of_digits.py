def findNumbers(nums):
    count_list = [1 for num in nums if len(str(num)) % 2 ==0]
    return sum(count_list)

# same work in one line
def findNumbers(nums):
    return sum([1 for num in nums if len(str(num)) % 2 ==0])

if __name__ == "__main__":
    nums = [5553,9013,4823,1771]
    print(findNumbers(nums))