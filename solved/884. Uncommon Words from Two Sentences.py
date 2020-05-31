def uncommonFromSentences(A, B):
    freq = {}
    output = []
    for word in A.split(" "):
        freq[word] = freq.get(word, 0) +1
    # for key, value in freq.items():
    #     if value ==1:
    #         output.append(key)
    # freq.clear()
    for word in B.split(" "):
        freq[word] = freq.get(word, 0) + 1
    for key, value in freq.items():
        if value ==1:
            output.append(key)
    return output

# best solution on leetcode
def uncommonFromSentencesBest(A,B):
    A_split = A.split()
    B_split = B.split()

    words = A_split + B_split

    unique = {}

    for word in words:
        if word not in unique:
            unique[word] = 1
        else:
            unique[word] = 0

    ans = []

    for word in unique.keys():
        if unique[word]: ans.append(word)

    return ans

if __name__ == '__main__':
    A = "this apple is sweet"
    B = "this apple is sour"
    print(uncommonFromSentences(A, B))