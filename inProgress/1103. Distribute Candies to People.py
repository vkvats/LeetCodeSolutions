def distributeCandies(candies, num_people):
    dist = [0]*num_people
    candy_to_give = 1
    while candies>0:
        for person in range(num_people):
            if candies - candy_to_give>=0:
                dist[person] = dist[person] + candy_to_give
                candies -= candy_to_give
                candy_to_give += 1
            else:
                dist[person] = dist[person] + candies
                candies =0
                break
    return dist
# good solution from leetcode
"""same line of thought, different implementation and faster as well"""
def distributeCandies1(candies, num_people):
    res = [0] * num_people
    num = 1
    while candies > 0:
        for i in range(num_people):
            res[i] += num
            candies -= num
            if candies <= 0:
                res[i] -= abs(candies)
                break
            num += 1
    return res


if __name__ == '__main__':
    candies = 10 # 7
    num_people = 3 # 4
    print(distributeCandies(candies, num_people))