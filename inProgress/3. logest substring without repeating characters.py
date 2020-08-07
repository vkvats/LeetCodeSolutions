class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0

        output = []
        i, j = 0,1
        while j < len(s):
            new_s = s[i]
            for char in s[i+1:]:
                if char not in new_s:
                    new_s += char
                    j +=1
                    if j == len(s):
                        output.append(len(new_s))
                else:
                    output.append(len(new_s))
                    new_s = s[j]
                    i = j
                    j += 1
            if len(new_s) == 1:
                output.append(1)
                i = j
        return max(output)

if __name__ == '__main__':
    s = " "
    print(Solution().lengthOfLongestSubstring(s))