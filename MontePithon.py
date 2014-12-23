#!/bin/python

from random import random

a = -1
b = 1

for i in range(6):
    Nu = 0;
    for N in range(pow(10,i)):
        x = a + random()*(b-a);
        y = random();
        if (x*x+y*y <=1):
            Nu += 1

    if N > 0:
        pi = (Nu/N)*(b-a)*2;
        print(N, " iterations produces a value of " ,pi)
