from defineRectangles import defineRectangles
from drawRectangles import drawRectangles
from calculateNewRectangles import calculateNewRectangles
import copy

def main(n):
    """
    Generates a list, length of users choice, of random rectangles, then determines a vertically stacked
    rectangle layout through repeatedly removing the biggest bottom strip possible, before plotting both
    rectangle configurations simultaneously in a GUI.

    Args:
        n (int): Number of rectangles to generate.

    Returns:
        None.
    """
    rectangles = defineRectangles(n)                                    # Obtain random, adjacent rectangles.
    vertRectangles = calculateNewRectangles(copy.deepcopy(rectangles))  # Determine vertically stacked rectangles.
    drawRectangles(rectangles, vertRectangles)                          # Plot both simultaneously.


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:                                  
        print("Wring ammount of input arguments, example usage:")   # Reject if >1 input argument.
        print("'python src/main.py 4'")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
        if 3<=n<=10:
            main(n)
        else:                                               # Reject if int is outside of 3 to 10 inclusive.
            print("Please enter an integer from 3 to 10 inclusive.")    
    except:
        print("Wrong data type.")                           # Reject if input isn't an int.
        print("Please enter an integer from 3 to 10 inclusive.")
        sys.exit(1)