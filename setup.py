#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Approximate pi using Monte Carlo integration.',
    'author': 'J.P. Weiser',
    'url': 'https://github.com/jpweiser/MontePithon',
    'download_url': 'https://github.com/jpweiser/MontePithon/tarball/master',
    'author_email': 'jon@jpweiser.com',
    'version': '0.02.2',
    'install_requires': ['matplotlib'],
    'packages': ['monte_pithon'],
    'scripts': ['bin/monte-pithon'],
    'name': 'MontePithon',
    'classifiers' : [
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"]
}

setup(**config)
