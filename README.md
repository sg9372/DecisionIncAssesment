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
- Refer to the requirements.txt file for the specific version of dependencies.

## Compiled Executable

For convenience, a compiled version of the program is available.
The compiled code as been emailed to Natalie, and can be downloaded and ran by:

1. Navigate to `main.py`'s directory in cmd window (using "cd")
   
2. Run the code, example cmd input: "main 4"

## Source Code Installation
1.  Clone the Repository:
    git clone https://github.com/sg9372/DecisionIncAssesment
    cd DecisionIncAssesment

2.  Set Up a Virtual Environment (Optional but Recommended):
    
    Windows:
    python -m venv .venv
    .venv\Scripts\activate
    
    macOS/Linux:
    python3 -m venv .venv
    source .venv/bin/activate

3. Run code using, for example: "python src/main.py 10"

## Install Dependencies:

    pip install -r requirements.txt