class Solution:
    def printVertically(self, s: str) -> [str]:
        s_arr = s.split()
        print(s_arr)
        max_len = max([len(word) for word in s_arr])
        i = 0
        output = []
        while i < max_len:
            new_word = ""
            for word in s_arr:
                if i < len(word):
                    new_word += word[i]
                    continue
                else:
                    new_word += " "
                    continue
            i += 1
            output.append(new_word)
        return [word.strip() for word in output]

if __name__ == '__main__':
    s = "CONTEST IS COMING"
    print(Solution().printVertically(s))