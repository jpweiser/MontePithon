#!/bin/python

from random import random
from math import hypot

# Assume the radius of the circle be 1
radius = 1

# Demonstrate how the number of random points used improves the approximation
# value
for i in range(7):
    hit = 0;
    for total in range(pow(10,i) + 1):
        if (hypot(random(), random()) < radius): # if in circle
            hit += 1

    if total > 0: # prevent division by zero
        pi = (hit/total)*4*radius # h/m * 2 * Diameter
        print(total, " iterations produces a value of " ,pi)
