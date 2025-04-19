def lengthOfLastWord(s):
    if len(s) !=0:
        return len(s.split()[-1])
    return 0

# best mothod on leetcode
def lengthOfLastWordBest(self, s: str) -> int:
    if not s:
        return 0
    count = 0
    s = s.strip()
    for c in s[::-1]:
        count += 1
        if c == ' ':
            count -= 1
            break
    return count


if __name__ == '__main__':
    s = "hello world"
    print(lengthOfLastWord(s))