def findWords(words):
    first_row = set("qwertyuiop")
    second_row = set("asdfghjkl")
    third_row = set("zxcvbnm")
    output = []
    for word in words:
        if len(set(word.lower()) - first_row)==0:
            output.append(word)
        elif len(set(word.lower()) - second_row) ==0:
            output.append(word)
        elif len(set(word.lower()) - third_row) == 0:
            output.append(word)
    return output


if __name__ == '__main__':
    words = ["Hello", "Alaska", "Dad", "Peace"]
    print(findWords(words))