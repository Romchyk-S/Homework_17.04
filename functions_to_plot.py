# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:27:29 2024

@author: romas
"""

import numpy as np

# function analysis available here: https://colab.research.google.com/drive/1IFx38U1hP3ZZWU7mY3bHc2tr00MjvCVg

def func_0():
    
    x = np.arange(-10, 10, 0.1)    
    
    x_asymptote = None
    
    y_asymptote = None
    
    obl_asymptote = (0, 0+1, 1)
    
    inflexion_point_x = None
    
    inflexion_point_y = None
    
    max_point = None
    
    f_max = None
    
    min_point = None
    
    f_min = None
    
    zero_point = -1
    
    f_zero = (zero_point**2-1)/(zero_point-1)
    
    label = "$x\in(-∞;1) \cup (1;+\infty)$"
    
    title = "$y = (x^2-1)/(x-1)$"
    
    y = (np.piecewise(x, [(x < 0.99), ((x >= 0.99) & (x <= 1.01)), (x>1.01)],
                          [lambda x: (x**2-1)/(x-1), np.nan, lambda x: (x**2-1)/(x-1)]))

    return x, y, label, title, x_asymptote, y_asymptote, obl_asymptote, {'x': inflexion_point_x, 'y': inflexion_point_y}, {'x': max_point, 'y': f_max}, {'x': min_point, 'y': f_min}, {'x': zero_point, 'y': f_zero}

def func_1():
    
    x = np.arange(0.01, 10, 0.01)    
    
    x_asymptote = None
    
    y_asymptote = None
    
    obl_asymptote = None
    
    label = "$x>0$"
    
    inflexion_point_x = None
    
    inflexion_point_y = None
    
    max_point = None
    
    f_max = None
    
    min_point = None
    
    f_min = None
    
    zero_point = None
    
    f_zero = None
    
    title = "$y = 0.5^{log_2x}$"
    
    return x, 0.5**np.log2(x), label, title, x_asymptote, y_asymptote, obl_asymptote, {'x': inflexion_point_x, 'y': inflexion_point_y}, {'x': max_point, 'y': f_max}, {'x': min_point, 'y': f_min}, {'x': zero_point, 'y': f_zero}

def func_2():
    
    x = np.arange(0.01, 10, 0.1)    
    
    x_asymptote = None
    
    y_asymptote = None
    
    obl_asymptote = None

    inflexion_point_x = None
    
    inflexion_point_y = None
    
    max_point = None
    
    f_max = None
    
    min_point = None
    
    f_min = None
    
    zero_point = None
    
    f_zero = None
    
    label = "$x \in (0;1) \cup (1;+\infty) $"
    
    y = (np.piecewise(x, [(x < 0.99), ((x >= 0.99) & (x <= 1.01)), (x>1.01)],
                          [lambda x: np.emath.logn(x, x**2), np.nan, lambda x: np.emath.logn(x, x**2)]))
    
    title = "$y = log_xx^2$"
    
    return x, y, label, title, x_asymptote, y_asymptote, obl_asymptote, {'x': inflexion_point_x, 'y': inflexion_point_y}, {'x': max_point, 'y': f_max}, {'x': min_point, 'y': f_min}, {'x': zero_point, 'y': f_zero}

def func_3():
    
    x = np.arange(0.01, 10, 0.1)    
    
    x_asymptote = None
    
    y_asymptote = None
    
    obl_asymptote = None
        
    inflexion_point_x = None
    
    inflexion_point_y = None
    
    max_point = None
    
    f_max = None
    
    min_point = None
    
    f_min = None
    
    zero_point = None
    
    f_zero = None
    
    label = "$x \in (0;1) \cup (1;+\infty) $"
    
    y = (np.piecewise(x, [(x < 0.99), ((x >= 0.99) & (x <= 1.01)), (x>1.01)],
                          [lambda x: np.emath.logn(x**2, x), np.nan, lambda x: np.emath.logn(x**2, x)]))

    title = "$y = log_{x^2}x$"
    
    return x, y, label, title, x_asymptote, y_asymptote, obl_asymptote, {'x': inflexion_point_x, 'y': inflexion_point_y}, {'x': max_point, 'y': f_max}, {'x': min_point, 'y': f_min}, {'x': zero_point, 'y': f_zero}

def func_4():
    
    x = np.arange(-10, 10, 0.1)    
    
    x_asymptote = None
    
    y_asymptote = None
    
    obl_asymptote = None
    
    inflexion_point_x = None
    
    inflexion_point_y = None
    
    max_point = None
    
    f_max = None
    
    min_point = None
    
    f_min = None
    
    zero_point = None
    
    f_zero = None
    
    label = "$x \in (-\infty;-1) \cup (-1;0) \cup (0;1) \cup (1;+\infty)$"
    
    y = (np.piecewise(x, [(x < -1.01), ((x >= -1.01) & (x <= -0.99)), ((x > -0.99) & (x < -0.01)), ((x >= -0.01) & (x <= 0.01)), 
                          ((x > 0.01) & (x < 0.99)), ((x >= 0.99) & (x <= 1.01)), (x>1.01)], 
         [lambda x: np.emath.logn(x**2, x**2), np.nan, lambda x: np.emath.logn(x**2, x**2), np.nan, lambda x: np.emath.logn(x**2, x**2), np.nan, 
          lambda x: np.emath.logn(x**2, x**2)]))

    title = "$y = log_{x^2}x^2$"
    
    return x, y, label, title, x_asymptote, y_asymptote, obl_asymptote, {'x': inflexion_point_x, 'y': inflexion_point_y}, {'x': max_point, 'y': f_max}, {'x': min_point, 'y': f_min}, {'x': zero_point, 'y': f_zero}
