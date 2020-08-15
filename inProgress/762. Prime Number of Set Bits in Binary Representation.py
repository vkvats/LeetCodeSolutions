class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        primes = {2,3,5,7,11,13,17,19,23}
        count = 0
        for num in range(L, R+1):
            # using bin() make sit faster
            ones = bin(num).count('1') #self.count_ones(num)
            if ones in primes:
                count += 1
        return count


    def count_ones(self, num):
        count = 0
        while num != 0:
            num = num & (num-1)
            count += 1
        return count


if __name__ == '__main__':
    L, R = 10, 15
    print(Solution().countPrimeSetBits(L,R))