def freqAlphabets(s):
    length = len(s)
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    code = range(1, 27)
    mapping = dict(zip(code, alphabets))
    index = length-1
    output = ""
    while index >=0:
        if s[index] == '#':
            output = mapping[int(s[index-2: index])] + output
            index -=3
        else:
            output = mapping[int(s[index])] + output
            index -=1
    return output

if __name__ == '__main__':
    s = "10#11#12" ## "jkab"
    s = "1326#" ## "acz"
    s = "25#"
    s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
    print(freqAlphabets(s))
