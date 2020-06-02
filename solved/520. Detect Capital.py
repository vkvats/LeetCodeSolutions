def detectCapitalUse(word):
    if word.isupper():
        return True
    elif word.islower():
        return True
    elif word.istitle():
        return True
    else:
        return False

# best solution of leetcoe
def detectCapitalUseBest(word):
    upper_count = 0

    for c in word:
        if str.isupper(c):
            upper_count += 1

    return upper_count == len(word) or upper_count == 0 or upper_count == 1 and str.isupper(word[0])

if __name__ == '__main__':
    word = "USA"
    word = "VibHas"
    print(detectCapitalUse(word))