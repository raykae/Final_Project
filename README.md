# Final_Project
INST326 Final Project  
Members: Andrew, Bemenet, Diwash, Rachel

# **Polynomial Plotter**

Our program FinalProject.py plots polynomials on the command line, or alternatively, writes a plot to a file. Plotting is achieved by evaluating the function to decide position, taking the derivative to choose which text character to use, and printing the result.

FinalProject.py: contains all code for handling input and plotting  
blankfile.txt: optionally save a plot to this file

## Usage
Run the program with py FinalProject.py [polymial] [window] [options]. The polynomial is a string list of coefficients in order of increasing degree. Window is four boundaries for xmin, xmax, ymin, and ymax.

For example, if you wish to plot f(x) = 3x - x^2 + 4x^4 on x=[-10,10], y=[-5, 5], you would write  

`py FinalProject.py "0,3,-1,0,4" -10 10 -5 5`

To write to a file instead of printing, use the -f / --file option. The file should be located in the current directory and have the name "blankfile.txt"

`py FinalProject.py "0,3,-1,0,4" -10 10 -5 5 -f`

There is also an option to display an animation of sine waves in their approximate polynomial form, -a / --animate. In this case polynomial and window must be present but do not influence what is displayed. If the animation does not appear smooth, ensure the console window is large enough to display the entire plot.

`py FinalProject.py "0" 0 0 0 0 -a`

## Table of Functions and Techniques

| Function/Method | Team Member | Technique |
| - | - | - |
| __init__ | Diwash |  |
| __call__ | Diwash | conditional expr |
| derivative | Diwash | magic method |
| slope_char | Bemenet |  |
| display_plot | Bemenet | with statement & f-strings |
| parse_args | Andrew | ArgumentParser |
| draw_plot | Andrew | optional parameter |
| get_sin | Andrew |  |
| scale | Andrew |  |
| main | Rachel | sequence unpacking |
| blank_plot | Rachel | list comprehension |
