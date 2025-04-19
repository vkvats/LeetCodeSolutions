def calPoints(ops):
    score = []
    for op in ops:
        if op == "C":
            _ = score.pop()
        elif op == "D":
            last_valid = score[-1]
            score.append(2*last_valid)
        elif op == "+":
            last, second_last = score[-1], score[-2]
            score.append(last + second_last)
        else:
            score.append(int(op))
    return sum(score)

# best solution from leetcode
def calPointsBest(ops):
    stack = []

    for o in ops:
        if o == "+":
            stack.append(sum(stack[-2:]))
        elif o == "D":
            stack.append(2 * stack[-1])
        elif o == "C":
            stack.pop()
        else:
            stack.append(int(o))
    return sum(stack)

if __name__ == '__main__':
    # ops = ["5","2","C","D","+"]
    ops = ["5","-2","4","C","D","9","+","+"]
    print(calPoints(ops))