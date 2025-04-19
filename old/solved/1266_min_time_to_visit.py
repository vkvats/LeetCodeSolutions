# new solution
class Solution:
    def minTimeToVisitAllPoints(self, points: [[int]]) -> int:
        t = 0
        x1, y1 = points[0]
        for x2, y2 in points[1:]:
            diag = max(abs(x2 - x1), abs(y2 - y1))
            t += diag
            x1, y1 = x2, y2
        return t


# first thought
def minTimeToVisitAllPoints(points):
    time = 0
    startX, startY = points[0]
    for index in range(1, len(points)):
        endX, endY = points[index]
        x_dist = abs(endX-startX)
        y_dist = abs(endY-startY)
        step_time = min(x_dist, y_dist) + abs(x_dist - y_dist)
        time = time + step_time
        startX, startY = endX, endY
    return time

if __name__ == '__main__':
    # points = [[1, 1], [3, 4], [-1, 0]]
    points = [[3, 2], [-2, 2]]
    print(minTimeToVisitAllPoints(points))