#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''wgetdb

Usage:
  wgetdb database_path label url
  wgetdb -h | --help
  wgetdb --version

Options:
  -h --help     Show this screen.
  --version     Show version.
'''

from __future__ import unicode_literals, print_function
from docopt import docopt

__version__ = "0.1.0"
__author__ = "Akira Kozakai"
__license__ = "MIT"


def main():
    '''Main entry point for the wgetdb CLI.'''
    args = docopt(__doc__, version=__version__)
    print(args)


if __name__ == '__main__':
    main()
