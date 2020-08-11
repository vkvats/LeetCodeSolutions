# new solution
class Solution:
    def sumZero(self, n: int) -> [int]:
        arr =[]
        if n % 2 !=0:
            arr.append(0)
        for i in range(1, n//2 + 1):
            arr.extend([-i, i])
        return arr

# from leetcode solution
class Solutionf1:
    def sumZero(self, n: int) -> [int]:
        return (list(range(1 - n, n, 2)))

# first thought
def sumZero(n):
    arr =[]
    if n % 2 !=0:
        num = -1* (n//2)
        for i in range(n):
            arr.append(num)
            num +=1
    else:
        num = -1*(n//2)
        for i in range(n):
            if num ==0:
                num +=1
            arr.append(num)
            num +=1
    return arr, sum(arr)



if __name__ == '__main__':
    n = 6
    print(sumZero(n))
