# New Solution
# Two pointer, Slow and fast runner
class Solution:
    def findSpecialInteger(self, arr: [int]) -> int:
        n = len(arr)
        slow, fast = 0,0
        while fast < n:
            slow_num = arr[slow]
            fast_num = arr[fast]
            while slow_num == fast_num:
                fast += 1
                if fast == n: break
                fast_num = arr[fast]
            if fast_num != slow_num or fast == n:
                if fast-slow > n/4: return slow_num
                else: slow = fast

# Most voted solution
def findSpecialInteger(self, arr: [int]) -> int:
    n = len(arr) // 4
    for i in range(len(arr)):
        if arr[i] == arr[i + n]:
            return arr[i]



def findSpecialInteger(arr):
    length = len(arr)
    frequnecy_dict = {}
    for num in arr:
        frequnecy_dict[num] = frequnecy_dict.get(num, 0) + 1
        if frequnecy_dict[num] > length//4:
            return num
# Using list.count() method ## much slower
def findSpecialIntegerCount(arr):
    for num in arr:
        count = arr.count(num)
        if count > len(arr)//4:
            return num
# using Counter module from collectiona
def fineSpecialIntegerCounter(arr):
    from collections import Counter
    return Counter(arr).most_common(1)[0][0]
if __name__ == '__main__':
    arr = [1,1] # [1,2,2,6,6,6,6,7,10]
    print(Solution().findSpecialInteger(arr))