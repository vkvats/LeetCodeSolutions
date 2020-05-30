def distanceBetweenBusStops(distance, start, destination):
    total_distance = sum(distance)
    if start == destination:
        return 0
    if start > destination:
        start, destination = destination, start
    # starting_point = min(start, destination)
    # end_point = max(start, destination)
    clockwise_distance = sum(distance[start:destination])
    counter_clockwise_distance = total_distance - clockwise_distance
    return min(clockwise_distance, counter_clockwise_distance)



    return None

if __name__ == '__main__':
    distance = [1, 2, 3, 4]
    start = 0
    destination = 3
    print(distanceBetweenBusStops(distance, start, destination))