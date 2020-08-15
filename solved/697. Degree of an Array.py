# New Method
# using dictionary for couting and storing index
from collections import defaultdict, Counter
class Solution:
    def findShortestSubArray(self, nums: [int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        '''
        # next segment can be done in one pass.
        for i, num in enumerate(nums): 
            index_dict[num].append(i)
            f = freqs.get(num,0)+1
            freqs[num] = f
            if f > freq_count: freq_count = f
        '''
        index_dict = defaultdict(list)
        for i, num in enumerate(nums):
            index_dict[num].append(i)
        freqs = Counter(nums)
        _, freq_count = freqs.most_common(1)[0]

        output = len(nums)
        for key, val in freqs.items():
            if val == freq_count:
                mn, mx = index_dict[key][0], index_dict[key][-1]
                o = mx - mn + 1
                if o < output:
                    output = o
        return output

# improvement on last solution
    # in one pass, order N
    def findShortestSubArray(self, A):
        first, count, res, degree = {}, {}, 0, 0
        for i, a in enumerate(A):
            first.setdefault(a, i)
            count[a] = count.get(a, 0) + 1
            if count[a] > degree:
                degree = count[a]
                res = i - first[a] + 1
            elif count[a] == degree:
                res = min(res, i - first[a] + 1)
        return res


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