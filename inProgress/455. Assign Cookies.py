def findContentChildren(g, s):
    g.sort()
    s.sort()
    satisfied = 0
    for greed in g:
        if greed in s:
            satisfied +=1
            s.remove(greed)
        else:
            for satisfaction in s:
                if satisfaction > greed:
                    satisfied +=1
                    s.remove(satisfaction)
                    s.append(satisfaction - greed)
                    break
    return satisfied

def findContentChildren1(g, s):
    g.sort()
    s.sort()
    g_ptr = s_ptr = 0
    while g_ptr < len(g) and s_ptr < len(s):
        if g[g_ptr] <= s[s_ptr]:
            g_ptr += 1
            s_ptr += 1
        else:
            s_ptr += 1
    return g_ptr

# descriptive solution
def findContentChildren2(g, s):
    # give the largest cookie to the greediest child
    # If can't appease him, then give to the next greediest child

    # sort cookies, since we need to know the largest size of the cookie in order to give it to children
    # sort children, only then we can give the largest size cookie to the greediest child
    g.sort()
    s.sort()

    children, i, j = 0, len(g) - 1, len(s) - 1

    # we are traversing from reverse in order to follow the greedy approach..
    while (i >= 0 and j >= 0):
        # If cookie size is greater or equal to children's content, then decrease i & j, and take a count of children
        if (s[j] >= g[i]):
            children += 1

            i -= 1
            j -= 1
        else:
            # Else, move to next child, as we could not gratify the last child it may be possible to satisfy next child
            i -= 1

        # Finally return the gratified children count!!!
    return children

if __name__ == '__main__':
    g = [1,2,3]
    s = [3]
    # g = [262,437,433,102,438,346,131,160,281,34,219,373,466,275,51,118,209,32,108,57,385,514,439,73,271,442,366,515,284,425,491,466,322,34,484,231,450,355,106,279,496,312,96,461,446,422,143,98,444,461,142,234,416,45,271,344,446,364,216,16,431,370,120,463,377,106,113,406,406,481,304,41,2,174,81,220,158,104,119,95,479,323,145,205,218,482,345,324,253,368,214,379,343,375,134,145,268,56,206]
    # s = [149,79,388,251,417,82,233,377,95,309,418,400,501,349,348,400,461,495,104,330,155,483,334,436,512,232,511,40,343,334,307,56,164,276,399,337,59,440,3,458,417,291,354,419,516,4,370,106,469,254,274,163,345,513,130,292,330,198,142,95,18,295,126,131,339,171,347,199,244,428,383,43,315,353,91,289,466,178,425,112,420,85,159,360,241,300,295,285,310,76,69,297,155,416,333,416,226,262,63,445,77,151,368,406,171,13,198,30,446,142,329,245,505,238,352,113,485,296,337,507,91,437,366,511,414,46,78,399,283,106,202,494,380,479,522,479,438,21,130,293,422,440,71,321,446,358,39,447,427,6,33,429,324,76,396,444,519,159,45,403,243,251,373,251,23,140,7,356,194,499,276,251,311,10,147,30,276,430,151,519,36,354,162,451,524,312,447,77,170,428,23,283,249,466,39,58,424,68,481,2,173,179,382,334,430,84,151,293,95,522,358,505,63,524,143,119,325,401,6,361,284,418,169,256,221,330,23,72,185,376,515,84,319,27,66,497]
    print(findContentChildren1(g,s))