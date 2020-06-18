def twoCitySchedCost(costs):
    costs.sort(key=lambda x : x[1]-x[0])
    n = len(costs)//2
    total_cost = 0
    for cost in costs[:n]:
        total_cost += cost[1]
    for cost in costs[n:]:
        total_cost += cost[0]
    return total_cost

# fastest on leetcode
def twoCitySchedCostFast(costs):
    return sum([x[int(i >= len(costs) // 2)] for i, x in enumerate(sorted(costs, key=lambda x: (x[0] - x[1])))])


if __name__ == '__main__':
    costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]] # [[10,20],[30,200],[400,50],[30,20]]
    print(twoCitySchedCost(costs))