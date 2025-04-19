def destCity(paths):
    origin = []
    dest = []
    for pair in paths:
        origin.append(pair[0])
        dest.append(pair[1])
    return list(set(dest) - set(origin))[0]

# best solution from leetcode
from collections import defaultdict
def destCityBest(paths):
    arr = defaultdict(lambda: 0)

    for path in paths:
        arr[path[0]] += 1
        arr[path[1]] -= 1

    for i in arr:
        if arr[i] == -1:
            return i

if __name__ == '__main__':
    paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    print(destCityBest(paths))