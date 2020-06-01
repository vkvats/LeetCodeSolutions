# it should work but time limit exceeded
def countBinarySubstrings(s):
    total_count = 0
    count_string = "01"
    rev_count_string = "10"
    while len(count_string)<=len(s):
        total_count += s.count(count_string)
        total_count += s.count(rev_count_string)
        count_string = "0" + count_string + "1"
        rev_count_string = "1" + rev_count_string + "0"
    return total_count

# from discussion
def countBinarySubstringsFD(s):
    if s.count("0")==0 or s.count("1")==0:
        return 0
    s=s.replace("01","0 1")
    s=s.replace("10","1 0")
    s=s.split(" ")
    print(s)
    count=0
    for i in range(len(s)-1):
        count+=min(len(s[i]),len(s[i+1]))
    return count

if __name__ == '__main__':
    s = "00110011"
    # s = "10101"
    print(countBinarySubstringsFD(s))