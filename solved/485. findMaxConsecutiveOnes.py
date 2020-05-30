def findMaxConsecutiveOnes(nums):
    counter = 0
    max_count = 0
    for num in nums:
        if num ==1:
            counter +=1
        else:
            counter =0
        if max_count< counter:
            max_count = counter
    return max_count

if __name__ == '__main__':
    nums = [1,1,0,1,1,1]
    nums = [1,0,1,1,0,1]
    print(findMaxConsecutiveOnes(nums))