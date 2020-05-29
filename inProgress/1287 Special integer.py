def findSpecialInteger(arr):
    length = len(arr)
    frequnecy_dict = {}
    for num in arr:
        frequnecy_dict[num] = frequnecy_dict.get(num, 0) + 1
        if frequnecy_dict[num] > length//4:
            return num
# Using list.count() method ## much slower
def findSpecialIntegerCount(arr):
    for num in arr:
        count = arr.count(num)
        if count > len(arr)//4:
            return num
# using Counter module from collection
def fineSpecialIntegerCounter(arr):
    from collections import Counter
    return Counter(arr).most_common(1)[0][0]
if __name__ == '__main__':
    arr = [1,2,2,6,6,6,6,7,10]
    print(fineSpecialIntegerCounter(arr))