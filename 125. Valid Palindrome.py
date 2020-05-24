class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_ = ''.join([i for i in s if i.isalpha() or i.isnumeric()]).lower()
        s_reverse = s_[len(s_)-1::-1]
        if s_ == s_reverse:
            return True
        else:
            return False
