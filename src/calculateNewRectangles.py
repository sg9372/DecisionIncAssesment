from collections import deque
import math

def calculateNewRectangles(rectangles):
    """
    Determined  vertically stacked rectangles to form original rectangle outline 
    in the same number of bars or less 

    Args:
        rectangles (List[List]): Original, randomly generated, adjacent rectangles structure.

    Returns:
        newRectangles (List[List]): vertically stacked rectangles matching original rectangle's outline 
    """
    # Process all original rectangles as one 'island'
    newRectangles = processIsland(rectangles, 0)
    return newRectangles

def processIsland(island, floorY):
    # Get min height in current island.
    newRectangles = []
    minHeight=math.inf
    for rectangle in island:
        if rectangle[1]<minHeight:
            minHeight=rectangle[1]

    # The code finds the bar which goes along the bottom, so new  x values are min & max of current island
    newx0 = island[0][0]
    newx1 = island[len(island)-1][2]
    for rectangle in island:
        rectangle[1]-=minHeight  # Subtract minimum element's value from each height
    
    # Keep track of the new lower y value for all remaining rectangles
    newfloorY = floorY+minHeight
    newRectangles.append([newx0, newfloorY, newx1, floorY]) # Add new bottom rectangle to list

    # Split remaining parts into 'islands' split by zero height blocks, and recursivley call to process
    if len(island)!=1:
        newIslands = findNewIslands(island)
        for newIsland in newIslands:
            newIslandRectangles = processIsland(newIsland, newfloorY)
            for rect in newIslandRectangles:
                newRectangles.append(rect)
    
    return newRectangles

def findNewIslands(island):
    # Initialize variables
    newIslands = []
    currentIsland = []
    for rectangle in island:
        if rectangle[1]<=0:                     # Means this island is zero, need to split here.
            if currentIsland:
                newIslands.append(currentIsland)
                currentIsland = []
        else:                                   # Keep building current island with rectangles.
            currentIsland.append(rectangle)
    if currentIsland:                           # If an island in currentIsland, make sure to add it.
        newIslands.append(currentIsland)
    
    return newIslands