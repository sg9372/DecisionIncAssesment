import tkinter as tk

def drawRectangles(rectangles):
    # Create root window.
    root = tk.Tk()
    root.title('Rectangles')

    # Define scale
    scale = 10

    # Determine x offset
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
        y0 = canvasHeight-((y0-y1)*scale)
        y1 = canvasHeight

        # Add to canvas
        canvas.create_rectangle(x0, y0, x1, y1, outline="grey", fill="white", width=4)

    # Run the Tkinter event loop
    root.mainloop()

    return canvas