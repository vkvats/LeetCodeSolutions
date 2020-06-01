def mostCommonWord(paragraph, banned):
    import re
    new_para = paragraph.lower()
    for word in banned:
        new_para = new_para.replace(word, "_")
    frequency = {}
    word_list = re.split(r'(\W+)', new_para)
    for word in word_list:
        if word.isalpha():
            frequency[word] = frequency.get(word, 0) + 1
    max_count = max(list(frequency.values()))
    for key, value in frequency.items():
        if value == max_count:
            return key
# best solution on leetcode
def mostCommonWordBest(paragraph, banned):
    import re, collections
    words = re.findall(r'\w+', paragraph.lower())

    return collections.Counter(w for w in words if w not in banned).most_common(1)[0][0]


if __name__ == '__main__':
    # paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    # banned = ["hit"]
    paragraph = "abc abc? abcd the jeff!"
    banned = ["abc", "abcd", "jeff"]
    print(mostCommonWordBest(paragraph, banned))