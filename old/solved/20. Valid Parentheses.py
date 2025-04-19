def isValid(s):
    #using stack
    stack = []
    for index, p in enumerate(s):
        if p in "({[":
            stack.append(p)
            if index == len(s)-1:
                return False
        else:
            if len(stack) ==0:
                return False
            else:
                out_p = stack.pop()
                if out_p == "(" and p == ")":
                    continue
                elif out_p == "{" and p == "}":
                    continue
                elif out_p == "[" and p == "]":
                    continue
                else:
                    return False
    if len(stack) != 0: # stack != []
        return False
    else:
        return True

# best solution on leetcode
def isValidBest(self, s: str) -> bool:

    stack = []
    left = "([{"
    right = ")]}"

    if s == "":
        return True

    elif len(s) % 2 != 0 or s[0] == ")" or s[0] == "]" or s[0] == "}":
        return False

    for i in range(len(s)):
        if s[i] in left:
            stack.append(s[i])
        elif s[i] in right:
            if s[i] == ")":
                if stack.pop() != left[0]:
                    return False
            elif s[i] == "]":
                if stack.pop() != left[1]:
                    return False
            elif s[i] == "}":
                if stack.pop() != left[2]:
                    return False
    if stack != []:
        return False
    return True
if __name__ == '__main__':
    s = "([]"
    print(isValid(s))