# new method
class Solution:
    def sortArrayByParityII(self, A: [int]) -> [int]:
        # two pointer method
        j = 1 # odd pointer
        for i in range(0, len(A), 2): # even pointer
            if A[i] % 2: # odd check condition, 0 is False in python.
                while A[j] % 2:
                    j += 2
                A[i], A[j] = A[j], A[i] # swap when both are misplaced
        return A


# new Solution
class Solution:
    def sortArrayByParityII(self, A: [int]) -> [int]:
        output = [0]*len(A) # create array of required length and fill is as per condition
        e, o = 0,1
        for val in A:
            if val %2 ==0:
                output[e] = val
                e += 2
            else:
                output[o] = val
                o += 2
        return output


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