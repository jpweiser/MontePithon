#!/bin/python

from random import random

#range
a = -1
b = 1

for i in range(6):
    hit = 0;
    for total in range(pow(10,i)):
        x = a + random()*(b-a); # x coord
        y = random(); # y coord
        if (x*x+y*y <=1): # if in circle
            hit += 1

    if total > 0:
        pi = (hit/total)*(b-a)*2;
        print(total, " iterations produces a value of " ,pi)
