def stringMatching(words):
    output = []
    for word1 in words:
        for word2 in words:
            if word1 != word2 and word1 in word2:
                output.append(word1)
                break
    return output

# best solution on leetcode
def stringMatchingBest(words):
    out = []
    all_words = '_'.join(words)

    for word in words:
        if all_words.count(word) >= 2:
            out.append(word)

    return out


if __name__ == '__main__':
    words = ["mass", "as", "hero", "superhero"]
    words = ["leetcode", "et", "code"]
    words = ["blue", "green", "bu"]
    words = ["as", "ss", "aa", "sa", "sss"]
    print(stringMatchingBest(words))