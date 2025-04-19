# iterative solution
class Solution:
    def getRow(self, rowIndex: int) -> [int]:
        # if rowIndex ==0: return []
        if rowIndex ==0: return [1]
        output = [[1], [1,1]]
        n = 2
        while n <= rowIndex:
            tmp = [1]
            last_row = output[-1]
            for i in range(1,len(output[-1])):
                tmp.append(sum(last_row[i-1: i+1]))
            output.append(tmp + [1])
            n += 1
        return output[-1]