#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from math import hypot
import matplotlib.pyplot as plt
import numpy as np

class MontePithon(object):
    def __init__(self, iterations=100000,radius=1):
        self.radius = radius
        self.iterations = iterations
        self.coordinates = []
        self.hits = []
        self.misses = []
        self.approximation = self.approximate()

    def random_coord(self):
        return random.uniform(-self.radius, self.radius)

    def piplot(self):
        if self.iterations == 0:
            return
        caption = "Pi apprx. " + str(self.approximation) + " after " \
                + str(self.iterations) + " iterations"
        plt.scatter(*zip(*self.hits),c='r')
        plt.scatter(*zip(*self.misses))
        plt.gcf().gca().add_artist(plt.Circle((0,0),self.radius,color='r',
                                   alpha=.25))
        plt.axis('equal')
        plt.axis([-self.radius,self.radius,-self.radius,self.radius])
        plt.title("Monte Pithon")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.figtext(.015,.015,caption)
        plt.show()

    def approximate(self):
        if self.iterations == 0:
            return 0

        hit = 0.
        for total in range(self.iterations + 1):
            x = self.random_coord()
            y = self.random_coord()
            self.coordinates.append((x,y))
            if hypot(x, y) < self.radius: # if in circle
                hit += 1
                self.hits.append((x,y))
            else:
                self.misses.append((x,y))

        return (hit/total)*4 # h/m * 2 * Diameter
