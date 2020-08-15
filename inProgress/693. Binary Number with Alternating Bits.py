class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b = f'{n:b}'
        for i in range(0, len(b)-1):
            if int(b[i]) ^ int(b[i+1]): return False
        else: return True

# intuitive solution from leetcode
def hasAlternatingBits(self, n):
    return '00' not in bin(n) and '11' not in bin(n)



if __name__ == '__main__':
    n = 5
    print(Solution().hasAlternatingBits(n))