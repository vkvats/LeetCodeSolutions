# using double comparison in one line
class Solution:
    def busyStudent(self, startTime: [int], endTime: [int], queryTime: int) -> int:
        count = 0
        for i in range(len(startTime)): # we can also use zip here.
            if startTime[i] <= queryTime <= endTime[i]: # we can write something like this as well.
                count +=1
        return count



# first thought
def busyStudent(startTime, endTime, queryTime):
    count = 0
    for i in range(len(startTime)):
        if queryTime in range(startTime[i], endTime[i]+1):
            count +=1
    return count

if __name__ == '__main__':
    # startTime = [1, 2, 3]
    # endTime = [3, 2, 7]
    # queryTime = 4
    # startTime = [4]
    # endTime = [4]
    # queryTime = 5
    startTime = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    endTime = [10, 10, 10, 10, 10, 10, 10, 10, 10]
    queryTime = 5
    print(busyStudent(startTime, endTime, queryTime))