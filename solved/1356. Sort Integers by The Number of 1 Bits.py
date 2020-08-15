# new Method
# using bit manipulation
from collections import defaultdict
class Solution:

    def sortByBits1(self, arr: [int]) -> [int]:
        arr.sort()
        return sorted(arr, key=lambda x: self.count_one(x))


    def sortByBits(self, arr: [int]) -> [int]:
        one_count = defaultdict(list)
        for num in sorted(arr):
            one_count[self.count_one(num)].append(num)
        output = []
        for i in sorted(one_count.keys()):
            output.extend(one_count[i])
        return output

    def count_one(self, n):
        count = 0
        while n != 0:
            count += 1
            n = n & (n - 1)
        return count



def sortByBits(arr):
    from collections import defaultdict
    bit_division = defaultdict(list)
    for num in sorted(arr):
        bit_sum = sum(map(int,list(bin(num)[2:])))
        bit_division[bit_sum].append(num)

    key_values = list(bit_division.items())
    key_values.sort(key=lambda x : x[0])
    output = []
    for value in key_values:
        output.extend(value[1])
    return output


# best solution on leetcode
def sortByBitsFast(arr):
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))


if __name__ == '__main__':
    arr = [1024,512,256,128,64,32,16,8,4,2,1] # [10,100,1000,10000] # [2,3,5,7,11,13,17,19]
    print(sortByBits(arr))