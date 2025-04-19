class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        visited.add(n)
        while n != 1:
            n_string = str(n)
            n = 0
            for char in n_string:
                n += int(char) ** 2
            if n not in visited:
                visited.add(n)
            else:
                return False
        return True

# Solution from leetcode ( without using string operation)
class SolutionF1:
    def isHappy(self, n: int) -> bool:
        def new_num(n):
            rem = 0
            while n != 0:
                rem += (n % 10) ** 2
                n = n // 10
            return rem

        visited = []
        while True:
            visited.append(n)
            n = new_num(n)
            if n == 1:
                return True
                break
            elif n in visited:
                return False
                break