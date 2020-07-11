import numpy as np
class Solution:
    def dailyTemperatures(self, T: [int]) -> [int]:
        t = np.array(T)
        result = []
        for idx, value in enumerate(T):
            new_t = list(t - value)
            if 1 in new_t:
                index = new_t[idx:].index(1)
                result.append(index)
            else:
                result.append(0)



        return result

if __name__ == '__main__':
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    sol = Solution().dailyTemperatures(T)
    print(sol)