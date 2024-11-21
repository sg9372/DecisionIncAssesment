from collections import deque
import math

def calculateNewRectangles(rectangles):
    newRectangles = processIsland(rectangles, [], 0)
    return newRectangles

def processIsland(island, floorY):
    # Get min height in current island.
    newRectangles = []
    minHeight=math.inf
    for rectangle in island:
        if rectangle[1]<minHeight:
            minHeight=rectangle[1]

    newx0 = island[0][0]
    newx1 = island[len(island)-1][2]
    for rectangle in island:
        rectangle[1]-=minHeight  # Subtract minimum element's value from each height.
    
    newfloorY = floorY+minHeight
    newRectangles.append([newx0, newfloorY, newx1, floorY])

    if len(island)!=1:
        newIslands = findNewIslands(island)
        for newIsland in newIslands:
            newIslandRectangles = processIsland(newIsland, newfloorY)
            for rect in newIslandRectangles:
                newRectangles.append(rect)
    
    return newRectangles

def findNewIslands(island):
    newIslands = []
    currentIsland = []
    for rectangle in island:
        if rectangle[1]<=0:                     # Means this island is zero, need to split here.
            if currentIsland:
                newIslands.append(currentIsland)
                currentIsland = []
        else:                                   # Keep building current island.
            currentIsland.append(rectangle)
    if currentIsland:
        newIslands.append(currentIsland)
    
    return newIslands