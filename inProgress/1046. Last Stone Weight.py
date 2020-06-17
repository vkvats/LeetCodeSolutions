def lastStoneWeight(stones):
    while len(stones) > 1:
        stones.sort()
        y = stones.pop()
        x = stones.pop()
        if x == y:
            stones.insert(0,0)
            stones.sort()
        else:
            stones.insert(0,y-x)
    return stones[0]


# fastest solution on leetcode
def lastStoneWeightFast(stones):
    while len(stones) > 1:
        stones.sort()
        print(stones)
        x, y = stones[-2:]
        if x == y:
            stones = stones[:-2]
        else:
            stones = stones[:-2] + [y - x]

    if not stones:
        return 0
    else:
        return stones[0]


if __name__ == '__main__':
    stones = [2,7,4,1,8,1]
    print(lastStoneWeight(stones))