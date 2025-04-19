def canThreePartsEqualSum(A):
    total_sum = sum(A)
    if total_sum %3 !=0:
        return False
    part_sum = total_sum/3
    part_gen = 0
    temp_sum = 0
    for num in A:
        temp_sum = temp_sum + num
        if temp_sum == part_sum:
            temp_sum =0
            part_gen +=1
    if part_gen ==3:
        return True
    else:
        return False

if __name__ == '__main__':
    # A = [0,2,1,-6,6,-7,9,1,2,0,1]
    # A = [0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]
    # A = [3, 3, 6, 5, -2, 2, 5, 1, -9, 4]
    A = [10,-10,10,-10,10,-10,10,-10] # stuck here.

    print(canThreePartsEqualSum(A))