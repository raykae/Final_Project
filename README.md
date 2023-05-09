# Final_Project
INST326 Final Project
    Members: Andrew,  Bemenet, Diwash , Rachael

**Polynomial Plotter**

# Diwash:
    I have created a class named as Polynomial then created magic method called "__init__()" and two functions : evaluate() and derivative() inside it.

   # Class Polynomial:  
            stores information about polynomial and its derivative.
   # 1  __init__() method:
           Initializes the list of coefficients representing polynomial and stores them as an attribute. They are stored in descending power of x i.e, first element has highest power of x.                                                                      
           Ex:-  f(x) = 4x^3 + 3x^2 + 2x + 1
   # 2 evaluate() function: 
            calculate the polynomial at given x value using list comprehension.
            Ex:- f(2) = 4*2^3 + 3*2^2 + 2*2 + 1 = 49
  # 3 derivative() function: 
            compute the new polynomial from current polynomial by multiplying \
            each coefficients by given power of x and decreasing power by 1. If\
             the coefficient is constant, it returns 0. This function also uses\
              Conditional Expression to return the new derivative polynomial.
            Ex:- f’(x) = 12x^2 + 6x + 2 








+----------------------------------------------------------------------------+
| **Method/Function**  | **primary author**   | **Techniques Demonstrated**|
+----------------------------------------------------------------------------+
|       evalaute()     |      Diwash Ban      |   List Comprehension       |
+-----------------------------------------------------------------------------+
|       derivative()   |      Diwash Ban      |    Conditional Expression  |
+-----------------------------------------------------------------------------+
|                      |                      |                            |

|                      |                      |                            |

|                      |                      |                            |

|                      |                      |                             |

