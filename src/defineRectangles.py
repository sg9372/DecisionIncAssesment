import random

def defineRectangles(n):
    """
    Generates a specified number of random rectangles and stores points in a list.
    Rectangle form definition = [x0, y0, x1, y1] [topleft, bottomright]

    Args:
        num_rectangles (int): Number of rectangles to generate.

    Returns:
        list: A list of rectangles, each defined as [x0, y0, x1, y1].
    """

    # Preallocate memory for rectangles structure
    rectangles = [[0, 0, 0, 0] for _ in range(n)]

    # Define range of values for random variables
    lb = 1      # lowerbound
    ub = 10     # upperbound

    # Define first rectangle
    rectangles[0] = [0, random.randint(lb,ub), random.randint(lb,ub), 0]

    # Define remaining rectangles based on previous rectangles final x-position and random dimensions
    for i in range(1,n):
        # Reference last rectangles end point
        startPoint = rectangles[i-1][2]

        rectangles[i][0] = startPoint
        rectangles[i][1] = random.randint(lb,ub)
        rectangles[i][2] = startPoint + random.randint(lb,ub)
        # y1 (rectangles[i][3]) is always zero so no need to define.

    return rectangles