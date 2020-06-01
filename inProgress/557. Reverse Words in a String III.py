def reverseWords(s):
    output = []
    arr = s.split(" ")
    for word in arr:
        output.append("".join(reversed(list(word))))
    return " ".join(output)

# best solution on leetcode
""" did same thing in place. It makes if faster."""
def reverseWordsBest(s):
    s = s.split()
    for j in range(len(s)):
        s[j] = s[j][::-1]

    return " ".join(s)

if __name__ == '__main__':
    s = "Let's take LeetCode contest" ## "s'teL ekat edoCteeL tsetnoc"
    print(reverseWordsBest(s))