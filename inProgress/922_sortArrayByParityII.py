# first thought
def sortArrayByParityII(A):
    even=[]
    odd = []
    output = []
    [even.append(x) if x%2==0 else odd.append(x) for x in A]
    for i in range(len(A)):
        if i%2 ==0:
            output.append(even[i//2])
        else:
            output.append(odd[i//2])
    return output

if __name__=='__main__':
    A=[4,2,5,7]
    print(sortArrayByParityII(A))