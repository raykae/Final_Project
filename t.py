from plotter import *
import math
import time
import os

# p = Polynomial([1,2])
# d = p.derivative()
# print(d.coefficents)

def get_coef(p, a, neg=1):
    # odd
    max_degree = 91
    s = ""
    pos = True
    if neg == -1:
        pos = False
    for d in range(max_degree):
        if pos:
            sign = "" 
        else: 
            sign = "-"
        if d % 2 == 1:
            c = a*p**d/math.factorial(d)
            s += sign + str(c)
            pos = not pos
            if d!= max_degree -2:
                s += (",")
        elif d != max_degree - 1:
            s += "0,"
    return s

def get_p(p, a, neg):
    plist = get_coef(p, a, neg).split(",")
    return Polynomial([float(c) for c in plist])
    
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

def scale():
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
    # del coeflist[::4]
    framelen = len(coeflist)
    
    for e in coeflist:
        
        offsetlist.append((15*e)**2)
        # p = get_coef(e, neg=-1)
        # os.system("cls")
        # main(p, (-40, 40, -10, 10))
        # time.sleep(0.005)
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
                    plot = draw_ploto(plot, p, (x1, x2), (y1, y2), offsetlist[i])
                else:
                    plot = draw_ploto(plot, p, (x1, x2), (y1, y2), -offsetlist[i])
            i += 1
            if i >= slidelen:
                i = 0
            
            os.system("cls||clear")
            for row in plot:
                # print(''.join(row))
                rw = ""
                for c in row:
                    rw += " " + c
                print(rw)

def scroll():  
    for o in range(-100,100):
    # for o in ([n*0.01 for n in list(range(1,60))] + [n*0.01 for n in list(range(1,60))][::-1]):
        p_str = get_coef(.1)
        p = p_str.split(",")
        p = Polynomial([float(c) for c in p])
        
        plot = blank_plot(o - 40, o + 40, -10, 10)
        plot = draw_ploto(plot, p, (-40, 40), (-10, 10), o)
        # p2_str = get_coef(0.2)
        # p2 = p2_str.split(",")
        # p2 = Polynomial([float(c) for c in p2])
        # plot = draw_ploto(plot, p2, (-40, 40), (-10, 10), 0*o)
        # p3_str = get_coef(0.1)
        # p2 = p3_str.split(",")
        # p2 = Polynomial([float(c) for c in p2])
        # plot = draw_ploto(plot, p2, (-40, 40), (-10, 10), 1*o)
        
        os.system("cls")
        for row in plot:
            # print(''.join(row))
            r = ""
            for c in row:
                r += " " + c
            print(r)
        
        
        time.sleep(0.001)
        
scale()