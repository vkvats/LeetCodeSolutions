def arrayRankTransform(arr):
    output = []
    ranked = {}
    rank = 1
    for num in sorted(arr):
        if num not in ranked:
            ranked[num]= rank
            rank +=1
    for num in arr:
        output.append(ranked[num])
    return output

# from discussion: using set is game changer to use dictionary
# we can give starting point to enumerate with kwargs start=
def arrayRankTransformD(arr):
    ranked = {value: idx for idx, value in enumerate(sorted(set(arr)), start=1)}
    return ([ranked[i] for i in arr])

if __name__ == '__main__':
    arr = [40,10,20,30]
    # arr = [100, 100, 100]
    arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]
    print(arrayRankTransformD(arr))