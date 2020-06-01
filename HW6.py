#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 18:03:33 2020

@author: alyxandrahoberg
"""

import matplotlib.pyplot as plt

# DataSet 
height = [35, 45, 95, 65] 
bars = ('Lonzo Ball', 'Loren Gray', 'Ben Grudzien', 'George Lopez')


# colors and formatting 
colors = ('darkorange', 'yellowgreen', 'aqua', 'magenta')
width = [0.1, 0.8, 1, 0.3]
ticks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


plt.bar(bars, height, width = width, align = 'center', color = colors)


plt.xlabel('People')
plt.xticks(bars)

plt.ylabel('Coolness Level')
plt.yticks(ticks)

plt.title('How cool is Ben? (100 coolness = coolest person to ever live)')


plt.show()