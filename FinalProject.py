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
        

def parse_arguments(arglist):
    """Parse command line arguments.
    
    Args:
        arglist (list of str): command line arguments.
    
    Returns:
        namespace: parsed arguments
    """
    parser = ArgumentParser()
    parser.add_argument("polynomial", help="string of coefficients")
    parser.add_argument("x1", help="x-axis left bound")
    parser.add_argument("x2", help="x-axis right bound")
    parser.add_argument("y1", help="y-axis lower bound")
    parser.add_argument("y2", help="y-axis upper bound")
    return parser.parse_args(arglist)