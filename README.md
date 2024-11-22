## Rectangles Challenge
This application generates a set of random horizontal rectangles with adjacent heights and widths, calculates the vertical rectangles that form the same outline, and displays both sets on the same canvas for comparison.

It fulfills the requirements of the Rectangles Challenge as outlined by Decision Inc.

## Features
-   Randomized Generation: Accepts user input for the number of rectangles (3 to 10) and generates      horizontal rectangles with random widths and heights.
-   Outline Matching: Computes the equivalent vertical rectangles that replicate the outline of the original rectangles.
-   Graphical Comparison: Displays both sets of rectangles on the same canvas using Tkinter, with distinct colors for clarity.

## Requirements
- Python Version: Python 3.8 or above

## Dependencies:
- Pillow (Python Imaging Library)
- Refer to the requirements.txt file for the specific version of dependencies.

## Installation
1.  Clone the Repository:
    git clone https://github.com/your-username/rectangles-challenge.git
    cd rectangles-challenge

2.  Set Up a Virtual Environment (Optional but Recommended):
    
    Windows:
    python -m venv .venv
    .venv\Scripts\activate
    
    macOS/Linux:
    python3 -m venv .venv
    source .venv/bin/activate

## Compiled Executable

For convenience, a compiled version of the program is available.

The executable is located in the `dist/` folder:
- **Windows**: `dist\main.exe`
- **macOS/Linux**: `dist/main`

1. Navigate to the `dist` directory ("cd dist")
   
2. Example cmd input: "main 4"
   Example VS code terminal input: "./main 4""

## Install Dependencies:

    pip install -r requirements.txt