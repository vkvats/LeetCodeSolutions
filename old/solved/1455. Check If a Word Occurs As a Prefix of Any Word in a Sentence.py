def isPrefixOfWord(sentence, searchWord):
    words = sentence.split(" ")
    for index, word in enumerate(words, start=1):
        if word.startswith(searchWord):
            return index
    return -1

if __name__ == '__main__':
    # sentence = "i love eating burger"
    # searchWord = "burg"
    # sentence = "this problem is an easy problem"
    # searchWord = "pro"
    sentence = "i am tired"
    searchWord = "you"
    print(isPrefixOfWord(sentence, searchWord))