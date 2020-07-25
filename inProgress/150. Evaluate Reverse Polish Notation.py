import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = { "+": operator.add, "-": operator.sub, "*":operator.mul, "/":operator.truediv }
        stored = []
        while  tokens:
            tok = tokens.pop(0)
            if tok not in "+-*/":
                stored.append(tok)
            else:
                val2 = stored.pop()
                val1 = stored.pop()
                new_val = ops[tok](int(val1), int(val2))
                stored.append(new_val)
        return int(stored[0])

# solutions from leetcode
