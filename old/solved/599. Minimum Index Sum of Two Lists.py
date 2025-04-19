def findRestaurant(list1, list2):
    common_resturants = set(list1).intersection(set(list2))
    index_dict = {}
    for index, rest in enumerate(list1):
        if rest in common_resturants:
            index_dict[rest] = index
    for index, rest in enumerate(list2):
        if rest in common_resturants:
            index_dict[rest]= index_dict[rest]+index
    min_index_sum = min(index_dict.values())
    output=[]
    for key,value in index_dict.items():
        if value == min_index_sum:
            output.append(key)
    return output

if __name__ == '__main__':
    # list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    # list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    list1= ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["KFC", "Shogun", "Burger King"]
    print(findRestaurant(list1, list2))