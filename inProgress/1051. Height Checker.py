# First thought
def heightChecker(heights):
    ordered_heights = heights[:]
    ordered_heights.sort()
    number_of_changes= 0
    for x,y in zip(ordered_heights, heights):
        if x-y !=0:
            number_of_changes +=1
    return number_of_changes

if __name__ == '__main__':
    # heights = [1,1,4,2,1,3]
    heights = [5, 1, 2, 3, 4]
    print(heightChecker(heights))


