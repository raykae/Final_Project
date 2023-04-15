"""Plots polynomials on the command line"""

from argparse import ArgumentParser
from sys import argv

class Polynomial: 
    """stores information about the polynomial and its derivative"""
    
    def __init__(self,coefficents):
        """Initalizing coefficents of Polynomial object.
            
            Args:
                 coefficents(list): list of coefficents 
                 
                 
        """
        
        self.coefficents = coefficents
        
    def evaluate(self, x):
        """
        Evaluates the polynomial at the given x value.
        
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
        deriv_coefficents = [i * self.coefficents[i] for i in range(1, len(self.coefficents))]
        return Polynomial(deriv_coefficents)


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
     



def draw_plot(plot, polynomial: Polynomial, X, Y):
    """Insert characters into a blank plot.
    
    Args:
        plot (list of list of str): an empty two dimensional list, result of blank_plot.
        polynomial (Polynomial): the polynomial to be plotted. 
        X (tup of int): range for x values (inclusive).
        Y (tup of int): range for y values (inclusive).
    
    Side effects:
        Modifies plot by inserting characters.
        
    Returns:
        list of list of str: the plotted function.
    """
    x1, x2 = X
    y1, y2 = Y
    for x in range(x1, x2 + 1):
        y = polynomial.evaluate(x)
        if y1 <= y and y <= y2:
            char = slope_char(polynomial.derivative().evaluate(x))
            plot[x - x1][y2 - y] = char
    return plot

def main(coords, polynomial):
    # Parse command line arguments
    x1, x2, y1, y2 = coords
    
    # Generate a blank plot
    plot = blank_plot(x1, x2, y1, y2)
    
    # TODO: plot the polynomial on the plot
    
    # Print the plot
    for row in plot:
        print(''.join(row))
        
def blank_plot(x1, x2, y1, y2):
    # Determine the dimensions of the plot
    width = int(abs(x2 - x1) * 10) + 1
    height = int(abs(y2 - y1) * 10) + 1
    
    # Create the blank plot
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
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(argv[1:])
    main(args.polynomial, args.x1, args.x2, args.y1, args.y2)
