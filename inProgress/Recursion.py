# Simple recusive function
def printFun(test):
    if (test < 1): return
    else:
        print( test, end = " ")
        printFun(test-1)
        print(test, end = " ")
        return
test = 3
print(printFun(test))

# claculation of floor of log N base 2
def fun1(n):
    if(n == 1):
        return 0
    else:
        return 1 + fun1(n//2)
#
# print(fun1(9))

# double recursive call
def fun(x):

    if(x > 0):
        x -= 1
        fun(x)
        print(x)
        x -= 1
        fun(x)

# Driver code
a = 4
fun(a)