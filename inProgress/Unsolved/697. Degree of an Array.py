def findShortestSubArray(nums):
    length_nums = len(nums)
    def frequency(array):
        frequncy = {}
        for num in array:
            frequncy[num] = frequncy.get(num,0) + 1
        degree = max(frequncy.values())
        return degree

    degree_of_nums = frequency(nums)
    if degree_of_nums == len(nums):
        return nums
    increased_len = 0
    while increased_len < length_nums - degree_of_nums:
        for index in range(length_nums- degree_of_nums - increased_len+1):
            if degree_of_nums == frequency(nums[index: index+ degree_of_nums+increased_len]):
                return len(nums[index: index+ degree_of_nums+increased_len])
        increased_len +=1

if __name__ == '__main__':
    A = [1, 2, 2, 3, 1]
    # A = [1,2,2,3,1,4,2]
    A = [1]
    A= [1,2,1]
    print(findShortestSubArray(A))