def allCellsDistOrder(R, C, r0, c0):
    from collections import defaultdict
    dist_dict = defaultdict(list)
    for i in range(R):
        for j in range(C):
            manhattan_dist = abs(r0 - i) + abs(c0 - j)
            dist_dict[manhattan_dist].append([i,j])
    key_values = list(dist_dict.items())
    key_values.sort(key= lambda x: x[0])
    output = []
    for pair in key_values:
        output.extend(pair[1])
    return output


#best solution from leetcode
def allCellsDistOrderFast(R, C, r0, c0):
    ans = [[i,j] for i in range(R) for j in range(C)]
    return sorted(ans, key = lambda ans: abs(ans[0]- r0) +abs(ans[1]- c0))


if __name__ == '__main__':
    R = 2
    C = 3
    r0 = 1
    c0 = 2
    print(allCellsDistOrder(R, C, r0, c0))