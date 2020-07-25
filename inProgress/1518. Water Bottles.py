class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        if numExchange > numBottles:
            return numBottles
        drink = 0
        carry = 0
        while numBottles > 0:
            drink += numBottles
            x = (numBottles + carry) // numExchange
            carry = (numBottles + carry) % numExchange
            numBottles = x

# Solution from leetcode
class SolutionF1:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        emp = numBottles
        while emp >= numExchange:
            total += emp // numExchange
            emp = emp // numExchange + emp % numExchange

        return total