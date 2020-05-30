def numJewelsInStones(J, S):
    counts = {}
    for s in S:
        counts[s] = counts.get(s,0) + 1
    total_jweles = 0
    for j in J:
        total_jweles += counts.get(j,0)
    return total_jweles


if __name__ == '__main__':
    J = "aA"
    S = "aAAbbbb"
    print(numJewelsInStones(J,S))