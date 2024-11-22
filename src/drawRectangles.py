import tkinter as tk

def drawRectangles(rectangles, vertRectangles):
    """
    Shows random horizonally adjacent rectangles and optimised vertically stacked rectangles simultaneously.

    Args:
        rectangles (List[List]): list of random, horizontally adjacent rectangles.
        vertRectangles (List[List]): list of optimised, vertically stacked rectangles.

    Returns:
        None.
    """
    # Create root window.
    root = tk.Tk()
    root.title('Rectangles')

    # Define scale
    scale = 10

    # Determine limits and margins for selecting canvas dimensions
    totalLength = rectangles[len(rectangles)-1][2]*scale
    maxHeight = 10*scale
    xMargin = 100
    yMargin = 25

    # Determine canvas dimensions
    canvasWidth = totalLength+xMargin
    canvasHeight = (maxHeight*1.2)+yMargin
    middle = canvasWidth/2
    xOffset = middle-(totalLength/2)

    # Build canvas
    canvas = tk.Canvas(root, width=canvasWidth, height=canvasHeight)
    canvas.pack(side="bottom")

    # Loop through each rectangle in the "rectangles" matrix
    for rect in rectangles:
        x0, y0, x1, y1 = rect  # Unpack rectangle coordinates
        
        # Offset x values to align to centre
        x0 = xOffset+x0*scale
        x1 = xOffset+x1*scale

        # Offset y values
        y0 = canvasHeight-(y0*scale)-yMargin
        y1 = canvasHeight-(y1*scale)-yMargin

        # Add to canvas
        canvas.create_rectangle(x0, y0, x1, y1, outline="grey", width=4)

    # Loop through each rectangle in the "vertRectangles" matrix
    for rect in vertRectangles:
        x0, y0, x1, y1 = rect  # Unpack rectangle coordinates
        
        # Offset x values to align to centre
        x0 = xOffset+x0*scale
        x1 = xOffset+x1*scale

        # Offset y values
        y0 = canvasHeight-(y0*scale)-yMargin
        y1 = canvasHeight-(y1*scale)-yMargin

        # Add to canvas
        canvas.create_rectangle(x0, y0, x1, y1, outline="blue", width=2)

    # Run the Tkinter event loop
    root.mainloop()

    return canvas