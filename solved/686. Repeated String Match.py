def repeatedStringMatch(A, B):
    lenA = len(A)
    lenB = len(B)
    order = lenB//lenA
    add_term = [A] * order
    finalA = "".join(add_term)
    for value in range(6):
        if B in finalA:
            return order
        else:
            finalA += A
            order +=1
    else: return -1

# best solution on leetcode
# same thinking, faster implementation
import math
def repeatedStringMatchBest(self, A: str, B: str) -> int:
    if not set(B).issubset(set(A)):
        return -1

    base = math.ceil(len(B) / len(A))
    for i in range(2):
        if B in A * (base + i):
            return base + i
    return -1


if __name__ == '__main__':
    # A = "abcd"
    # B = "cdabcdab"
    # A = "a"
    # B = "aa"
    A = "abc"
    B = "cabcabca"
    print(repeatedStringMatch(A, B))