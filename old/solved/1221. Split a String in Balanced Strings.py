# new method.
# shortened code
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        R_count = 0
        balanced_strip = 0
        for alpha in s:
            R_count += 1 if alpha == "R" else -1
            if R_count == 0:
                balanced_strip += 1
        return balanced_strip

# using 'elif' rather than a bunch of 'if' statements improves the running time
def balancedStringSplit(s):
    R_count = 0
    L_count = 0
    balanced_strip =0
    for alpha in s:
        if alpha == "R":
            R_count +=1
        elif alpha == "L": # use 'elif'
            L_count +=1
        if R_count == L_count:
            R_count, L_count = 0,0
            balanced_strip +=1
    return balanced_strip


if __name__ == '__main__':
    # s = "RLRRLLRLRL"
    # s = "LLLLRRRR"
    s = "RLRRRLLRLL"
    print(balancedStringSplit(s))