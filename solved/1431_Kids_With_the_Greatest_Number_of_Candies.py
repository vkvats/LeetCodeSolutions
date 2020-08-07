def kidsWithCandies(candies, extraCandies) :
    bool_list= []
    # sanity check
    assert(len(candies) >=2 and len(candies) <=100)
    assert(extraCandies >=1 and extraCandies <=50)

    max_condy = max(candies)
    for candy in candies:
        if candy + extraCandies >= max_condy:
            bool_list.append(True)
        else:
            bool_list.append(False)
    return bool_list

# using numpy
def kidsWithCandiesNumpy(candies, extracandies):
    import numpy as np
    candies_np = np.array(candies)
    max_candy = np.max(candies_np)
    with_extracandy = candies_np + extracandies
    with_extracandy = with_extracandy >=max_candy
    return with_extracandy

# using list comprehension
def kidsWithCandiesListComprehension(candies, extraCandies):
    return [candy + extraCandies >= max(candies) for candy in candies]

# using MAP function:
def using_map(candies, extraCandies):
    max_val = max(candies)
    return map(lambda x: x + extraCandies >= max_val, candies)

if __name__ == '__main__':
    # candies = [2, 3, 5, 1, 3]
    # extraCandies = 3
    candies = [12, 1, 12]
    extraCandies = 10
    # print(kidsWithCandiesNumpy(candies, extraCandies))
    # print(kidsWithCandies(candies, extraCandies))
    print(kidsWithCandiesListComprehension(candies, extraCandies))