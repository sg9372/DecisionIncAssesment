from defineRectangles import defineRectangles
from drawRectangles import drawRectangles
from calculateNewRectangles import calculateNewRectangles

def main(n):
    print("Starting process...")
    rectangles = defineRectangles(n)

    if rectangles==-1:
        print("Please enter an integer from 3 to 10 inclusive.")
    
    canvas = drawRectangles(rectangles)

    calculateNewRectangles(rectangles)




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