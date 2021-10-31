#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 20:18:43 2018

@author: huang
"""

import numpy as np
import matplotlib.pyplot as plt

# Sigmoid function 
x = np.linspace(-10,10,100,endpoint=5)
y = [1/(1 + np.exp(-i)) for i in x]
y2 = [np.sin(i) for i in x ] 

# Plotting
plt.plot(x,y,'r-*')
plt.plot(x,y2, 'b--o', label="cos(x)")
plt.show()
