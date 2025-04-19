class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        num = ""
        for n in digits:
            num = num + str(n)
        num = str(int(num) + 1)
        return [int(n) for n in num]

# solution from leetcode
class SolutionF1:
    def plusOne(self, digits: List[int]) -> List[int]:

        if not digits:
            return [1]
        if digits[-1] < 9:
            return digits[:len(digits) - 1] + [digits[len(digits) - 1] + 1]
        else:
            res = self.plusOne(digits[:len(digits) - 1]) + [0]

        return res

# Using string method
class SolutionF2:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = list(map(str,digits))
        stri = ''.join(digits)
        modNum = int(stri) + 1
        return list(map(int,list(str(modNum))))


if __name__ == '__main__':
    arr = [9]
    print(Solution().plusOne(arr))