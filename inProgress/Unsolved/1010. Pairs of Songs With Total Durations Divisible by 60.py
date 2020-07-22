# Time limit exceeted
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        if len(time) <= 1: return 0
        count = 0
        i = 0
        while True:
            val = time[i]
            if i+1 >= len(time):
                break
            for val2 in time[i+1:]:
                if (val + val2) % 60 == 0:
                    count += 1
            i += 1
        return count