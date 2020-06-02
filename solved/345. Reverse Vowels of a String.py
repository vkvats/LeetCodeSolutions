def reverseVowels(s):
    vowels = ""
    string = s
    for alpha in s:
        if alpha in "aeiouAEIOU":
            vowels += alpha
            string = string.replace(alpha, "_", 1)
    for vow in vowels[::-1]:
        string = string.replace("_", vow, 1)
    return string

# best solution on leetcode
import re
def reverseVowelsBest(s):
    vowels = re.findall('(?i)[aeiou]', s)
    return re.sub('(?i)[aeiou]', lambda x: vowels.pop(), s)


if __name__ == '__main__':
    s = "hello"
    s = "leetcode"
    s = "aA"
    print(reverseVowels(s))