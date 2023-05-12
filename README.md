# Final_Project
INST326 Final Project
    Members: Andrew,  Bemenet, Diwash , Rachael

**Polynomial Plotter**

# Diwash:
    I have created a class named as Polynomial then created magic method called\
     "__init__()" and two functions : evaluate() and derivative() inside it.

   # Class Polynomial:  
            stores information about polynomial and its derivative.
   # 1  __init__() method:
           Initializes the list of coefficients representing polynomial and \
           stores them as an attribute. They are stored in descending power of\
            x i.e, first element has highest power of x.                                                                      
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





#
table_header = "| Methods/Functions | Primary Author| Techniques demonstrated|\n"
table_divider = "| --------------   | --- ----------| ---   ---------------  |\n"
table_row_1 = "| evaluate()         | Diwash Ban    | List Comprehnsion      |\n"
table_row_2 = "| derivative()       | Diwash Ban    | Conditional Expression |\n"
table_row_3 = "|                    |               |                        |\n"
table_row_4 = "|                    |               |                        |\n"
table_row_5 = "|                    |               |                        |\n"         
table_row_6 = "|                    |               |                        |\n"
table_row_7 = "|                    |               |                        |\n"
table_row_8 = "|                    |               |                        |\n"


table = table_header + table_divider + table_row_1 + table_row_2 + table_row_3+ table_row_4 + table_row_5 + table_row_6+ table_row_7 + table_row_8

with open('README.md', 'w') as f:
    f.write(table)




		
		
		
		
		
		
		
				
		
		
		
		
		
		
		
		
				
		
		
		
		
		
		
		
		
		

