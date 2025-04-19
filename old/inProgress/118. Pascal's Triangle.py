
# Iterative solution 
class Solution:
    def generate(self, numRows: int) -> [[int]]:
        if numRows == 0: return []
        if numRows == 1: return [[1]]
        output = [[1], [1, 1]]
        n = 2
        while n < numRows:
            tmp = [1]
            last_row = output[-1]
            for i in range(1, len(output[-1])):
                tmp.append(sum(last_row[i - 1: i + 1]))
            output.append(tmp + [1])
            n += 1
        return output


if __name__ == '__main__':
    n = 5
    print(Solution().generate(n))