def findOcurrences(text, first, second):
    word_list = text.split(" ")
    output = []
    for i in range(len(word_list)-2):
        if word_list[i] == first and word_list[i+1] ==second:
            output.append(word_list[i+2])
    return output

if __name__ == '__main__':
    # text = "alice is a good girl she is a good student"
    # first = "a"
    # second = "good"
    text = "we will we will rock you"
    first = "we"
    second = "will"
    print(findOcurrences(text, first, second))
