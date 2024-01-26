import math
from plotter import *

def get_sin(freq, amplitude, neg=1):
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

p = get_sin(.3, 8)
# s = ""
# for e in p.coefficents:
#     s += str(e) + ","
# s+= "0.0"
print(p.coefficents)
# main(s, (-20, 20, -10, 10))clea