def wordPattern( pattern: str, str: str) -> bool:
        string = str.split(" ")
        pattern_dict, str_dict = {},{}
        if len(pattern) != len(string):
            return False
        for p, s in zip(pattern, string):
            if p not in pattern_dict:
                pattern_dict[p]= s
            if s not in str_dict:
                str_dict[s]= p
            if str_dict[s] != p or  pattern_dict[p] != s:
                return False
        return True


pattern, str = "abba", "dog cat cat fish"
print(wordPattern(pattern, str))