### first solution: works fine on leetcode.




### second solution: This solution exceeds the memory limit on leetcode but works fine 

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        first = [x for x in range(c+1)]
        second = [x for x in range(c, -1, -1)]
        pairs = zip(first, second)
        for first, second in pairs:
            if self.perfectSquare(first) is True and self.perfectSquare(second) is True:
                return True
        return False


    def perfectSquare(self, num):
        if num in (0, 1):
            return True
        if num < 0:
            return False
        if num % 10 not in (1, 4, 5, 6, 9, 0):
            return False
        # now will do binary search.
        start = 1
        end = num
        while start <= end:
            mid_num = start + (end - start) // 2
            if mid_num * mid_num == num:
                return True
            elif mid_num * mid_num > num:
                end = mid_num - 1
            elif mid_num * mid_num < num:
                start = mid_num + 1
        return False
