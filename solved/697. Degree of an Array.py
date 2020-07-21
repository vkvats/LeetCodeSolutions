def findShortestSubArray(nums):
    from collections import Counter
    if len(nums) <= 1:
        return len(nums)
    freqs = Counter(nums)
    freq_count = max( freqs.values())
    values = [val for val, count in freqs.items() if count == freq_count]
    output = []
    for val in values:
        first_index = nums.index(val)
        # reversing the list gives the index as per original indexing.
        last_idx = len(nums) - nums[::-1].index(val)
        output.append(last_idx - first_index)
    return min(output)



if __name__ == '__main__':
    A = [1,2,2,3,1]
    # A = [1,2,2,3,1,4,2, 2,2,2,2]
    # A = [2,1]
    # A= [1,2,1]
    print(findShortestSubArray(A))