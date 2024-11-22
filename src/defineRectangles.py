import random


## Define rectangles in an array, each element representing one rectangle on a positive x-y axis.
def defineRectangles(n):
# Rectangle form definition = [x0, y0, x1, y1] [topleft, bottomright]

    # Initialize rectangles, preallocating space for efficiency
    rectangles = [[0, 0, 0, 0] for _ in range(n)]

    # Define range of values
    lb = 3      # lowerbound
    ub = 10     # upperbound

    # Define first rectangle
    rectangles[0] = [0, random.randint(lb,ub), random.randint(lb,ub), 0]

    # Define remaining rectangles based on previous rectangles final x point
    for i in range(1,n):
        # Reference last rectangles end point
        startPoint = rectangles[i-1][2]

        rectangles[i][0] = startPoint
        rectangles[i][1] = random.randint(lb,ub)
        rectangles[i][2] = startPoint + random.randint(lb,ub)
        # y1 is always zero so no need to define.

    return rectangles