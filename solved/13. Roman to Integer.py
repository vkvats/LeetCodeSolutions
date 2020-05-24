class Solution:

    def romanToInt(self, s: str) -> int:
        values = {'I': 1,'V': 5,'X': 10,'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400,'CM': 900}
        # start parsing from right to left.
        integer = 0
        itr = len(s) -1
        while itr >= 0:
            if s[itr] in "VXLCDM" and s[itr-1] + s[itr] in ("IV","IX","XL","XC","CD","CM") and itr-1 >=0:
                integer += values[s[itr-1] + s[itr]]
                itr = itr - 2
            elif s[itr] in"IVXLCDM":
                integer += values[s[itr]]  
                itr = itr - 1            

        return integer
