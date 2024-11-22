from defineRectangles import defineRectangles
from drawRectangles import drawRectangles
from calculateNewRectangles import calculateNewRectangles
import copy

def main(n):
    rectangles = defineRectangles(n)
    rectangles = [[0, 4, 6, 0], [6, 2, 9, 0], [9, 5, 19, 0], [19, 3, 27, 0], [27, 7, 29, 0]]    
    vertRectangles = calculateNewRectangles(copy.deepcopy(rectangles))

    drawRectangles(rectangles, vertRectangles)




if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Too many input arguments, example usage:")
        print("'python src/main.py 4'")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
    except:
        print("Wrong data type.")
        print("Please enter an integer from 3 to 10 inclusive.")
        sys.exit(1)

    main(n)