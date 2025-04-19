class Solution:
    def customSortString(self, S: str, T: str) -> str:
        count_t = {}
        not_in_s = ""
        for char in T:
            count_t[char] = count_t.get(char, 0) + 1
            if char not in S:
                not_in_s += char
        output = ""
        for char in S:
            if char in T:
                output += char * count_t[char]
        return output + not_in_s

# solution from leetcode
