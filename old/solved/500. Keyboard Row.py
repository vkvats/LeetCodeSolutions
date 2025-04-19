# new Solution
# using subset operation
def findWords(self, words):
    line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
    ret = []
    for word in words:
      w = set(word.lower())
      if w <= line1 or w <= line2 or w <= line3: # this is subset operation

        ret.append(word)
    return ret


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