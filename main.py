#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse, sys
from montepithon import MontePithon

def _parseArgs(args=sys.argv[1:]):
    """Setup argparser to process arguments and generate help"""

    parser = argparse.ArgumentParser(description="Use Monte Carlo integration \
                                      to approximate PI.")
    parser.add_argument('-i',"--iterations", action='store', type=int,default=100000,
                         help="Number of iterations to use for approximation")
    parser.add_argument('-r',"--radius", action='store', type=float, default=1,
                         help="Radius of circle to use for integration")
    parser.add_argument('-p',"--plot", action='store_true',
                         help='Plot result')
    parser.add_argument('-v',"--verbose", action='store_true',
                         help='Toggle verbose output')

    return parser.parse_args(args)

def main():

    parsed = _parseArgs()

    mp = MontePithon(parsed.iterations,parsed.radius)
    pi = mp.approximate()

    if parsed.verbose:
        print 'Circle radius: ' + str(parsed.radius)
        print 'Appoximation after ' + str(parsed.iterations) + ' iterations:'

    print str(pi)

    if parsed.plot:
        mp.piplot()


if __name__ == '__main__':
    main()
