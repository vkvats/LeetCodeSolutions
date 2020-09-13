class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> [int]:
        if N==1 : return range(10)
        self.output = []
        stack = []
        for n in range(1,10):
            stack.append(n)
            while stack:
                num = stack.pop(0)
                num2 = num
                while num:
                    if (num% 10) + K < 10 :
                        num = self.increase(num, N, K)
                        if self.check2(num, N):
                            stack.append(num)
                    elif (num%10) - K >= 0 :
                        num = self.decrease(num, N,K)
                        if self.check2(num, N):
                            stack.append(num)
                    else: num = False
                    if self.check(num, N):
                        if num in self.output: num = False
                        else: self.output.append(num)
                        num = False
                    if num > 10**N: num = False

                while num2:
                    if (num2%10) - K >= 0 :
                        num2 = self.decrease(num2, N,K)
                        if self.check2(num2, N):
                            stack.append(num2)
                    elif (num2% 10) + K < 10 :
                        num2 = self.increase(num2, N, K)
                        if self.check2(num2, N):
                            stack.append(num2)
                    else: num2 = False
                    if self.check(num2, N):
                        if num2 in self.output: num2 = False
                        else: self.output.append(num2)
                        num2 = False
                    if num2 > 10 ** N: num2 = False
        return self.output

    def increase(self, num, N, K):
        if (num%10) + K < 10:
            num = num*10 + (num%10 + K)
        return num

    def decrease(self, num, N, K):
        if (num % 10) - K >= 0:
            num = num * 10 + (num % 10 - K)
        return num

    def check(self, num, N):
        if 10 ** (N - 1) <= num < 10 ** N:
            return True
        else: return False

    def check2(self, num, N):
        if num <= 10**(N-1):
            return True

if __name__ == '__main__':
    N, K = 2, 1 #2, 1 #3, 7
    print(len(Solution().numsSameConsecDiff(N,K)))
    print(len([101, 121, 123, 210, 212, 232, 234, 321, 323, 343, 345, 432, 434, 454, 456, 543, 545, 565, 567, 654, 656, 676, 678,
     765, 767, 787, 789, 876, 878, 898, 987, 989]))