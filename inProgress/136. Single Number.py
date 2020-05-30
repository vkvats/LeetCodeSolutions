#Naive method
def singleNumber(nums):
    count = {}
    for num in nums:
        count[num]= count.get(num, 0) + 1
    for key, value in count.items():
        if value ==1:
            return key
# math approach
def singleNumberMath(nums):
    return 2 * sum(set(nums)) - sum(nums)

# best solution of leetcode
def singleNumberBest(nums):
    my_dict = dict()
    for i in nums:
        if i in my_dict:
            my_dict.pop(i)
        else:
            my_dict[i] = 1

    for i in my_dict:
        return i

if __name__ == '__main__':
    nums = [2,2,1]
    print(singleNumberMath(nums))