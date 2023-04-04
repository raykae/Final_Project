"""Plots polynomials on the command line"""

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
        
        