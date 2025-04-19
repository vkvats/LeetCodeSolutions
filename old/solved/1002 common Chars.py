# New solution
from collections import defaultdict
class Solution:
    def commonChars(self, A: [str]) -> [str]:
        counter = defaultdict(list)
        output = ""
        for word in A:
            for char in set(word):
                counter[char].append(word.count(char))
        for key, val in counter.items():
            if len(val) == len(A):
                t = min(val)
                output += key*t
        return list(output)



# Naive solution
def commonChars(A):
    out_char = ""
    for char in A[0]:
        len_A = len(A)
        for word in A:
            word_list = list(word)
            out_char_list = list(out_char)
            if len(out_char) !=0:
             for char2 in out_char_list:
                 word_list.remove(char2)
            if char in word_list:
                len_A -=1
            else: break
        if len_A ==0:
            out_char = out_char + char
    return list(out_char)



if __name__ =='__main__':
    A = ["bella","label","roller"]
    # A= ["cool","lock","cook"]
    print(Solution().commonChars(A))