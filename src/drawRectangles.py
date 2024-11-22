import tkinter as tk
from PIL import Image, ImageTk

def drawRectangles(rectangles, vertRectangles):
    print(rectangles)
    # Create root window.
    root = tk.Tk()
    root.title('Rectangles')

    # Define scale
    scale = 25

    # Determine x-offset
    totalLength = rectangles[len(rectangles)-1][2]*scale
    maxHeight = 10*scale
    
    canvasWidth = totalLength+100
    canvasHeight = maxHeight+50
    middle = canvasWidth/2
    xOffset = middle-(totalLength/2)

    # Build canvas
    canvas = tk.Canvas(root, width=canvasWidth, height=canvasHeight)
    canvas.pack(padx = 10, pady=10, side="bottom")

    # Loop through each rectangle in the "rectangles" matrix
    for rect in rectangles:
        x0, y0, x1, y1 = rect  # Unpack rectangle coordinates
        
        # Offset x values
        x0 = xOffset+x0*scale
        x1 = xOffset+x1*scale

        # Offset y values
        print(y0, y1)
        y0 = maxHeight-(y0*scale)
        y1 = maxHeight-(y1*scale)
        print(x0, y0, x1, y1)

        # Add to canvas
        canvas.create_rectangle(x0, y0, x1, y1, outline="grey", width=4)

    # Do the same for the vertRectangles.
    # Loop through each rectangle in the "rectangles" matrix
    for rect in vertRectangles:
        x0, y0, x1, y1 = rect  # Unpack rectangle coordinates
        
        # Offset x values
        x0 = xOffset+x0*scale
        x1 = xOffset+x1*scale

        # Offset y values
        y0 = maxHeight-(y0*scale)
        y1 = maxHeight-(y1*scale)

        print(x0, y0, x1, y1)
        # Add to canvas
        canvas.create_rectangle(x0, y0, x1, y1, outline="blue", width=2)


    # Run the Tkinter event loop
    root.mainloop()

    return canvas