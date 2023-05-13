"""Plots polynomials on the command line"""

from argparse import ArgumentParser
from sys import argv
import math
import os

class Polynomial: 
    """stores information about the polynomial and its derivative"""
    
    def __init__(self,coefficents):
        """Initalizing coefficents of Polynomial object.
            
            Args:
                 coefficents(list): list of coefficents 
                 
                 
        """
        
        self.coefficents = coefficents
        
    def __call__(self, x):
        """
        Call the polynomial at the given x value.
        
        Args:
            x (float): Given value to evaluate the polynomial.
        
        Returns:
            float: The value of the polynomial at x.
        """
        
        
        p = sum(self.coefficents[i] * x ** i for i in range(len(self.coefficents)))
        return p if len(self.coefficents) > 0 else None

            
    def derivative(self):
        """
        Returns a new Polynomial object that represents the derivative of the current polynomial.
        
        Returns:
            Polynomial: The derivative of the current polynomial.
        """
        deriv_coefficents = []
        for i in range(1, len(self.coefficents)):
            deriv_coefficents.append(i * self.coefficents[i])
        return Polynomial(deriv_coefficents) if len(deriv_coefficents) >= 1 \
        else Polynomial([0])


def slope_char(slope):
    """Takes the derivative and converts to a character.

    Args:
        slope(int): given slope at a point in a graph 

    Returns:
        character that the derivative value corresponds to
    """
    if slope >= -0.5 and slope <= 0.5:
        return "-"
    if slope > 0.5 and slope < 3:
        return "/"
    if slope < -0.5 and slope >= -3:
        return " \ "
    else:
        return "|"
     
def display_plot(plot, write = False):
    """Takes the plot as an argument and prints or writes it to a file.

    Args:
        plot (list of list of str): an empty two dimensional list, result of blank_plot
        write(txt)

    Prints:
        the plot in the terminal or writes it to the file. 

    """
    if write:
        with open("blankfile.txt", "w") as file:
            for row in plot:
                formatted_row = ""
                for line_char in row:
                    formatted_row += f" {line_char}"
                file.write(f"{formatted_row}\n")
    else:
        for row in plot:
            formatted_row = ""
            print(''.join(row))
            for line_char in row:
                formatted_row += f" {line_char}"
        
        



def draw_plot(plot, polynomial: Polynomial, X, Y, offset=0):
    """Insert characters into a plot. Plot may or may not be blank.
    
    Args:
        plot (list of list of str): an empty two dimensional list, result of blank_plot.
        polynomial (Polynomial): the polynomial to be plotted. 
        X (tup of int): range for x values (inclusive).
        Y (tup of int): range for y values (inclusive).
        offset (float): offset for x values.
    
    Side effects:
        Modifies plot by inserting characters.
        
    Returns:
        list of list of str: the plotted function.
    """
    x1, x2 = X
    y1, y2 = Y
    for x in range(x1, x2 + 1):
        y = polynomial(x - offset)
        if y1 <= y and y <= y2:
            char = slope_char(polynomial.derivative()(x - offset))
            plot[y2 - int(y)][int(x) - x1] = char
    return plot

def get_sin(freq, amplitude, neg=1):
    """Generates Polynomial with coefficients for a sine approximation.
    
    Args:
        freq (float): frequency of the sine wave.
        amplitude (float): amplitude of the sine wave.
        neg (int): 1 or -1, reverses the wave on the x-axis.
        
    Returns:
        Polynomial: a polynomial approximation for a sine wave.
    """
    # odd
    max_degree = 91
    sign = 1*neg
    l = []
    for degree in range(max_degree):
        if degree % 2 == 1:
            l.append(float(sign*amplitude*freq**degree/math.factorial(degree)))
            sign *= -1
        else:
            l.append(float(0))
    return Polynomial(l)

def scale():
    """Displays sine wave animation. (Use -a, other args don't matter but must be present.)
    
    Side effects:
        Prints multiple plots on the command line.
    """
    r = list(range(30))
    x1 = -18
    x2 = 18
    y1 = -13
    y2 = 13
    amp = 12
    num_curves = 5
    slides = []
    offsetlist = []
    
    coeflist = [n*0.01 for n in r]
    framelen = len(coeflist)
    
    for e in coeflist:
        offsetlist.append((15*e)**2)
        rev = 1
        plist = []
        for i in [(num_curves - i)/num_curves for i in range(num_curves) for _ in (0,1)]:
            plist.append(get_sin(e, amp*i, rev))
            rev *= -1
        slides.append(plist)
    
    slides += slides[::-1]
    slides += slides
    
    offsetlist += offsetlist[::-1]
    offsetlist += offsetlist
    
    slidelen = len(slides)

    for t in range(33):
        i = 0
        for e in range(framelen*4):
            plot = blank_plot(x1,x2,y1,y2)
            
            curr_plots = slides[i]
            for p in curr_plots:
                if i > slidelen/2:
                    plot = draw_plot(plot, p, (x1, x2), (y1, y2), offsetlist[i])
                else:
                    plot = draw_plot(plot, p, (x1, x2), (y1, y2), -offsetlist[i])
            i += 1
            if i >= slidelen:
                i = 0
            
            os.system("cls||clear")
            for row in plot:
                print(" ".join(row))

def main(polynomial, coords, animate=False, file=False):
    """
    Generates a plot of a polynomial function and displays it or saves it to a file.

    Args:
        polynomial (str): A string representation of the polynomial coefficients separated by commas.
        coords (tuple): A tuple containing the coordinates of the plot area in the form (x1, x2, y1, y2).
        animate (bool, optional): If True, scales the plot and returns without displaying or saving. Defaults to False.
        file (bool, optional): If True, saves the plot to a file. Defaults to False.

    Returns:
        None
    """
    if animate:
        scale()
        return

    x1, x2, y1, y2 = coords

    plist = polynomial.split(",")
    plist = [float(c) for c in plist]
    p = Polynomial(plist)

    plot = blank_plot(x1, x2, y1, y2)
    plot = draw_plot(plot, p, (x1, x2), (y1, y2))

    display_plot(plot, file)

        
def blank_plot(x1, x2, y1, y2):
    """
    Generates a blank plot with the specified dimensions.

    Args:
        x1 (float): The leftmost x-coordinate of the plot.
        x2 (float): The rightmost x-coordinate of the plot.
        y1 (float): The bottommost y-coordinate of the plot.
        y2 (float): The topmost y-coordinate of the plot.

    Returns:
        list: A 2D list representing the blank plot.
    """
    width = int(abs(x2 - x1)) + 1
    height = int(abs(y2 - y1)) + 1

    plot = [[' ' for _ in range(width)] for _ in range(height)]

    return plot


def parse_args(arglist):
    """Parse command line arguments.
    
    Args:
        arglist (list of str): command line arguments.
    
    Returns:
        namespace: polynomial, x1, x2, y1, y2.
    """
    parser = ArgumentParser()
    parser.add_argument("polynomial", type=str, help="coefficients separated by comma, start x^0")
    parser.add_argument("x1", type=int, help="x-axis left bound")
    parser.add_argument("x2", type=int, help="x-axis right bound")
    parser.add_argument("y1", type=int, help="y-axis lower bound")
    parser.add_argument("y2", type=int, help="y-axis upper bound")
    parser.add_argument("-a", "--animate", action="store_true")
    parser.add_argument("-f", "--file", action="store_true")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(argv[1:])
    main(args.polynomial, (args.x1, args.x2, args.y1, args.y2), args.animate, args.file)
