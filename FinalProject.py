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
        deriv_coefficents = [i * self.coeffs[i] for i in range(1, len(self.coefficents))]
        return Polynomial(deriv_coefficents)


def slope_char(slope):
    pass

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
