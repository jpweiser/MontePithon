#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""monte"""

import random
from math import hypot
import matplotlib.pyplot as plt

class MontePithon(object):
    """MontePithon"""
    def __init__(self, iterations=100000, radius=1):
        self.radius = radius
        self.iterations = iterations
        self.coordinates = []
        self.hits = []
        self.misses = []
        self.approximation = self.approximate()

    def random_coord(self):
        """Generates random coordinate in range -radius to radius"""
        return random.uniform(-self.radius, self.radius)

    def piplot(self):
        """Plots randomly generated coordinates during pi approximation"""
        if self.iterations == 0:
            return
        caption = "Pi approximately " + str(self.approximation) + " after " \
                + str(self.iterations) + " iterations"
        plt.scatter(*zip(*self.hits), c='r')
        plt.scatter(*zip(*self.misses))
        plt.gcf().gca().add_artist(plt.Circle((0, 0), self.radius, color='r',
                                              alpha=.25))
        plt.axis([-self.radius, self.radius, -self.radius, self.radius])
        plt.gcf().canvas.set_window_title('Monte Pithon')
        plt.axis('image')
        plt.title("Monte Pithon")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.figtext(.015, .015, caption)
        plt.show()

    def approximate(self):
        """Implements Monte Carlo integration to approximate Pi"""
        if self.iterations == 0:
            return 0

        hit, total = 0., 0.
        for total in range(self.iterations + 1):
            x_coord = self.random_coord()
            y_coord = self.random_coord()
            self.coordinates.append((x_coord, y_coord))
            if hypot(x_coord, y_coord) < self.radius: # if in circle
                hit += 1
                self.hits.append((x_coord, y_coord))
            else:
                self.misses.append((x_coord, y_coord))

        return (hit/total)*4 # h/m * 2 * Diameter
