def bitwiseComplement(N):
    binary = bin(N).replace("0b", "")
    complement = ""
    for b in binary:
        if b =='1':
            complement = complement + '0'
        else:
            complement = complement + "1"
    return int(complement,2)

# best solution on leetcode
def bitwiseComplementBest(N):
    X = 1
    while N > X:
        X = X * 2 + 1
    return X - N

if __name__ == '__main__':
    N = 7
    print(bitwiseComplementBest(N))

