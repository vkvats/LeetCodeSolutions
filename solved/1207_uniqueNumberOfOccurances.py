# Imports
from collections import Counter


def uniqueOccurrences(arr) -> bool:
    flag = False
    frequency_dict = {}
    for key in arr:
        frequency_dict[key] = frequency_dict.get(key, 0) + 1
    if len(frequency_dict.values()) == len(set(frequency_dict.values())):
        flag = True

    return flag

# fast method
def uniqueOccurenceFast(arr):
    flag = False
    count_dict = Counter(arr)
    if len(count_dict.values()) == len(set(count_dict.values())):
        flag = True
    return flag

# less line of code
def uniqueOccurenceLessCode(arr):
    return len(Counter(arr).values()) == len(set(Counter(arr).values()))

if __name__ == '__main__':
    # arr = [1, 2, 2, 1, 1, 3]
    # arr = [1, 2]
    arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
    # arr = []
    # print(uniqueOccurrences(arr))
    # print(uniqueOccurenceFast(arr))
    print(uniqueOccurenceLessCode(arr))
