# New Method
# using Bit Manipulation
class Solution:
    """
    dong XOR will only keep the bits where either one of them is 1,
    which will take care of the fact that the bits were different.
    For counting value of 1, we take bit wise AND of X with X-1
    """
    def hammingDistance(self, x: int, y: int) -> int:
        x_y = y ^ x
        count = 0
        while x_y != 0:
            x_y = x_y & (x_y -1)
            count += 1
        return count

class Solution1:
    def hammingDistance(self, x: int, y: int) -> int:
        bin_x = bin(x)[2:]
        bin_y = bin(y)[2:]
        lenx = len(bin_x)
        leny = len(bin_y)
        if lenx > leny:
            diff = lenx - leny
            bin_y = "0" * diff + bin_y
        elif leny > lenx:
            diff = leny - lenx
            bin_x = "0" * diff + bin_x
        count = 0
        for i in range(len(bin_x)):
            diff = int(bin_x[i]) - int(bin_y[i])
            if diff != 0:
                count += 1
        return count

# uysing XOR
class SolutionF1:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x^y
        num = str(bin(xor))
        count =0
        for i in num:
            if(i =='1'):
                count= count+1
        return count
