#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""main:
"""

import argparse, sys, math
from monte_pithon.monte import MontePithon

def _parse_args(args=sys.argv[1:]):
    """Setup argparser to process arguments and generate help"""

    parser = argparse.ArgumentParser(description="Use Monte Carlo integration \
                                      to approximate PI.")
    parser.add_argument('-i', "--iterations", action='store', type=int, default=100000,
                        help="Number of iterations to use for approximation")
    parser.add_argument('-r', "--radius", action='store', type=float, default=1,
                        help="Radius of circle to use for integration")
    parser.add_argument('-p', "--plot", action='store_true',
                        help='Plot result')
    parser.add_argument('-v', "--verbose", action='store_true',
                        help='Toggle verbose output')

    return parser.parse_args(args)

def main():
    """main"""

    parsed = _parse_args()

    monte = MontePithon(parsed.iterations, parsed.radius)
    monte_pi = monte.approximation

    if parsed.verbose:
        print 'Circle radius: ' + str(parsed.radius)
        print 'Appoximation after ' + str(parsed.iterations) + ' iterations: ' \
              + str(monte_pi)
        print 'Relative error: ' + str(abs(math.pi - monte_pi)/math.pi * 100) \
              + '%'
    else:
        print str(monte_pi)

    if parsed.plot:
        monte.piplot()


if __name__ == '__main__':
    main()
