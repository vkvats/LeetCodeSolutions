class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 1
        length = len(flowerbed)
        if len(flowerbed) == 1 and flowerbed[0] == 0 and n <= 1:
            return True
        if len(flowerbed) == 1 and flowerbed[0] != 0 and n != 0: return False
        if len(flowerbed) == 1 and flowerbed[0] != 0 and n == 0: return True
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            n -= 1
            i += 1
        if len(flowerbed) > 2:
            if flowerbed[-2] == 0 and flowerbed[-1] == 0:
                n -= 1
                length -= 1

        while i < length - 1 and n > 0:

            prev = flowerbed[i - 1]
            next_ = flowerbed[i + 1]
            current = flowerbed[i]
            if prev == 0 and next_ == 0 and current == 0:
                n -= 1
                i += 1
            i += 1
        return n <= 0

# Solution from leetcode
class SolutionF1:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if not n:
                return True
            if not flowerbed[i]:
                if not i or (i - 1 > 0 and not flowerbed[i - 1]):
                    if i + 1 == len(flowerbed) or (i + 1 < len(flowerbed) and not flowerbed[i + 1]):
                        flowerbed[i] = 1
                        n -= 1
        return n == 0
# Solution from leetcode
class SolutionF2:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # For last position, flowerbed: 1, 0, 0, Planted as: 1, 0, 1
        flowerbed.append(0)
        # For start position, flowerbed: 0, 0, 1, Planted as: 1, 0, 1
        flowerbed.insert(0, 0)

        num = 0
        res = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                num += 1
            else:
                num = 0
            if num == 3:
                n -= 1
                num = 1
            if n == 0:
                return True
        return False

# Solution form leetcode
class SolutionF3:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if not n:
                return True
            if not flowerbed[i]:
                if not i or (i - 1 > 0 and not flowerbed[i - 1]):
                    if i + 1 == len(flowerbed) or (i + 1 < len(flowerbed) and not flowerbed[i + 1]):
                        flowerbed[i] = 1
                        n -= 1
        return n == 0