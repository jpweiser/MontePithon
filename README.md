MontePithon
===========

Implementing Monte Carlo integration to calculate an approximation of π

π is a mathematical constant, representing the ratio of a circle’s circumference to its diameter. It is an
irrational number, and as such has a never ending decimal approximation.
Approximating π was once done geometrically until methods involving infinite series were introduced.
More recently, however, computational methods have been introduced that take advantage of ever improving
processing power.

One such method, Monte Carlo integration, is an interesting numerical technique for solving integrals
using a hit or miss approach. To approximate π, a circle of a certain diameter and a box
with dimensions that match the diameter are considered. A number of random coordinates pass through a
conditional statement. If the random coordinate falls within the circle based on a right handed rectangular
Cartesian coordinate system. then one is added to the total of successes. In the end, this number of successes
is compared to the total number of random coordinates. The result should yield an approximation of π.

Running the Program:

Requirements: Python 2.x

From terminal:

    python MontePithon.py
