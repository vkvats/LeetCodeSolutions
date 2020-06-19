def climbStairs(n):
    steps = [0, 1]
    if n < 2:
        return steps[n]
    last_step = 1
    second_last_step = 0
    for i in range(1, n):
        last_step, second_last_step = last_step + second_last_step, last_step

    return last_step + second_last_step

# fastest solution
class Solution:
    def climbStairs(self, n: int) -> int:
        return self.myclimbStairs(n,dict={})
    def myclimbStairs(self,n,dict):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n-1 in dict.keys():
            c1 = dict[n-1]
        else:
            dict[n-1] = self.myclimbStairs(n-1,dict)
            c1 = dict[n-1]
        if n-2 in dict.keys():
            c2 = dict[n-2]
        else:
            dict[n-2] = self.myclimbStairs(n-2,dict)
            c2 = dict[n-2]
        return c1+c2

# similar solution, written more succinctly
def climbStairsSimilar(n):
    a = b = 1
    for i in range(n):
        a, b = b, a + b
    return a

if __name__ == '__main__':
    n = 6
    print(climbStairs(n))
