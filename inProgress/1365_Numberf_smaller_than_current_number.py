
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

# list comprehension
def smallerNumbersThanCurrentListComprehension(nums):
    count = 0
    return [count + 1 for num2 for num in nums]


if __name__ == '__main__':
    # nums = [8, 1, 2, 2, 3]
    nums = [7, 7, 7, 7]
    print(smallerNumbersThanCurrentListComprehension(nums))
