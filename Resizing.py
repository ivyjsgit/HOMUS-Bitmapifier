def findMaxX(points):
    xs = list(map(lambda point: point[0], points))
    return max(xs)
def findMinX(points):
    xs = list(map(lambda point: point[0], points))
    return min(xs)
def findMaxY(points):
    ys = list(map(lambda point: point[1], points))
    return max(ys)
def findMinY(points):
    ys = list(map(lambda point: point[1], points))
    return min(ys)
def movePointsToCorner(points):
    min_x = findMinX(points)
    max_x = findMaxX(points)
    min_y = findMinY(points)
    max_y = findMaxY(points)

    width = max_x - min_x
    height = max_y - min_y

    centered_points = []
    if (width<height):
        amount_to_scoot = (height-width) / 2.0
        centered_points = list(map(lambda point: ((point[0]+amount_to_scoot),point[1]), points))
    else:
        amount_to_scoot = (width-height) / 2.0
        centered_points = list(map(lambda point: (point[0],(point[1]+amount_to_scoot)), points))
    return centered_points

def scalePoints(points, viewport_size, shrink_factor):
    min_x = findMinX(points)
    max_x = findMaxX(points)

    width = max_x - min_x

    scale = (width/viewport_size) * shrink_factor
    scaled_points = list(map(lambda point: ((point[0]/scale) if point[0]!=0 else 0,(point[1]/scale) if point[1] !=0 else 0), points))
    return scaled_points

def scootPoints(scaled_points, padding):
    min_x = findMinX(scaled_points)
    min_y = findMinY(scaled_points)

    scooted_points = list(map(lambda point: (point[0]-min_x+padding, point[1]-min_y+padding),scaled_points))
    return scooted_points