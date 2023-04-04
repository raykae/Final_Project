"""Plots polynomials on the command line"""

from argparse import ArgumentParser
from sys import argv

class Polynomial: 
    """stores information about the polynomial and its derivative"""
    
    def __init__(self,coefficents,x,y):
        """Initalizing coefficents, x-interval and y-interval attributes
            
            Args:
                 coefficents(list): list of coefficents 
                 x(tuple): values of x-interval 
                 y(tuple): values of  y-interval
                 
        """
        
        self.coefficents = coefficents
        self.x = x
        self.y = y
        
        

def draw_plot(plot, polynomial):
    pass        

def main():
    pass

def parse_args(arglist):
    """Parse command line arguments.
    
    Args:
        arglist (list of str): command line arguments.
    
    Returns:
        namespace: parsed arguments
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