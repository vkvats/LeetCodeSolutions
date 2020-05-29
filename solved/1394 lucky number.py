"""Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.
Return a lucky integer in the array. If there are multiple lucky integers return the largest of them.
If there is no lucky integer return -1."""

def findLucky(arr):
    freq_dict = {}
    lucky = []
    for num in arr:
        freq_dict[num] = freq_dict.get(num,0) +1
    for key, value in freq_dict.items():
        if key == value:
            lucky.append(key)
    if len(lucky) != 0:
        return max(lucky)
    else:
        return -1

if __name__ == '__main__':
    arr = [2, 2, 3, 4]
    arr = [1,2,2,3,3,3]
    arr = [2, 2, 2, 3, 3]
    arr = [5]
    arr = [7, 7, 7, 7, 7, 7, 7]
    print(findLucky(arr))
