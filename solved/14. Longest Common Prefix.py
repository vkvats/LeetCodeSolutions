class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs and "" not in strs:
            match = strs[0]
            for word in strs[1:]:
                if match[0] == word[0]:
                    for i in range(len(match),-1,-1):
                        # print(match[0:i])
                        if match[0:i] in word[0:i]:
                            match = match[0:i]
                            break
                else: return ""
            if match:
                return match
            else: return ""
        else: return ""
