class Solution:
    def toGoatLatin(self, S: str) -> str:
        if not S: return
        words = S.split()
        # print(words)
        output = ""
        suffix = "a"
        for word in words:
            if word[0] in "aeiouAEIOU":
                word = word + "ma" + suffix
                output = output + " " + word
                suffix += "a"
            else:
                word = word[1:] + word[0] + "ma" + suffix
                output = output + " " + word
                suffix += "a"
        # print(output)
        return output.strip()

# Solution from leetcode
class Solution:
    def toGoatLatin(self, S: str) -> str:

        vowel = ['a', 'e', 'i', 'o', 'u']

        ans = []

        for i, w in enumerate(S.split(), 1):
            if w[0].lower() in vowel:
                ans.append(w + 'ma' + 'a' * i) # such multiplication is possible.
            if w[0].lower() not in vowel:
                ans.append(w[1:] + w[0] + 'ma' + 'a' * i)

        return " ".join(ans)