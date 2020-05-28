# first thought: using dictionary to story count and then fetcing it as per sorted order but,
# #two keys becomes same. so can't be done using dict.

# Second thought:
def kWeakestRows(mat, K):
    strength = [sum(row) for row in mat]
    order = [i[0] for i in sorted(enumerate(strength), key=lambda x: x[1])]
    return order[:k]

if __name__ == '__main__':
    mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
    k = 3
    print(kWeakestRows(mat, k))