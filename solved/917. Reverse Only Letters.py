def reverseOnlyLetters(S):
    indicies = []
    string = ""
    for index, alpha in enumerate(S):
        if alpha.isalpha():
            string += alpha
        else:
            indicies.append((index,alpha))
    reversed_string = list(string[::-1])
    for x in indicies:
        reversed_string.insert(x[0], x[1])
    return "".join(reversed_string)

# best solution from leetcode
def reverseOnlyLettersBest(S):
    start, end = 0, -1
    S = list(S)
    while start - end < len(S):

        if not S[start].isalpha():
            start += 1
        elif not S[end].isalpha():
            end -= 1
        else:
            S[start], S[end] = S[end], S[start]
            start += 1
            end -= 1

    return ''.join(S)

if __name__ == '__main__':
    S= "ab-cd"
    S = "Test1ng-Leet=code-Q!"
    print(reverseOnlyLetters(S))