def backspaceCompare(S, T):
    def operate(string):
        new_s = ""
        for ele in string:
            if ele != "#":
                new_s += ele
            else:
                if len(new_s) == 0:
                    continue
                else:
                    new_s = new_s[:len(new_s)-1]
        return new_s
    S = operate(S)
    T = operate(T)
    return S, T, S==T

# solution from leetcode
def backspaceCompareStack(S, T):
    def finder(L):
        ans = []
        for i in L:
            if i != "#":
                ans.append(i)
            elif ans:
                ans.pop()
        return "".join(ans)

    return finder(S) == finder(T)



if __name__ == '__main__':
    # S = "ab#c"
    # T = "ad#c"
    # S = "ab##"
    # T = "c#d#"
    # S = "a##c"
    # T = "#a#c"
    S = "oi###mupo##rszty#s#xu###bxx##dqc#gdjz"
    T = "oi###mu#ueo##pk#o##rsztu#y#s#xu###bxx##dqc#gz#djz"
    print(backspaceCompare(S,T))
