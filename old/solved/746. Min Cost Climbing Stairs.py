
# from discussion
def minCostClimbingStairsDiscussion(cost):
    n = len(cost)

    for i in range(2, n):
        cost[i] = min(cost[i - 1], cost[i - 2]) + cost[i]

    return min(cost[-1], cost[-2])

# From solutions
def minCostClimbingStairsSol(cost):
    f1 = f2 = 0
    for x in reversed(cost):
        f1, f2 = x + min(f1, f2), f1
    return min(f1, f2)

# fastest solution on leetcode
def minCostClimbingStairsFast(cost):
    prevprev = cost[0]
    prev = cost[1]
    for i in range(2, len(cost)):
        curr = cost[i] + min(prevprev, prev)
        prevprev = prev
        prev = curr
    return min(prevprev, prev)

if __name__ == '__main__':
    # cost = [10, 15, 20]
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    # cost = [0,2,2,1]
    print("cost: ", minCostClimbingStairs(cost))
