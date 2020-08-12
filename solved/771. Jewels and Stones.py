def numJewelsInStones(J, S):
    counts = {}
    for s in S:
        counts[s] = counts.get(s,0) + 1
    total_jweles = 0
    for j in J:
        total_jweles += counts.get(j,0)
    return total_jweles

def numJewelsInStonesBest(J, S):
    val = [count in J for count in S]
    return sum(val) # find the meaning

# using map function
def numJewelsInStones(self, J, S):
    return sum(map(S.count, J))


if __name__ == '__main__':
    J = "aA"
    S = "aAAbbbb"
    print(numJewelsInStonesBest(J,S))