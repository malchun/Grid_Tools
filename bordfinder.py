#!/usr/bin/env python3

import sys

import plot


def find_border(coords, elements):
    """Finds borders of points cloud

    coords - list of points
    elements - list of elements

    returns: list of border points
    """
    pass


def write_border(filename, border):
    """ Writes border into file

    filename - name of file (.out)
    border - list of points
    
    return: None
    """
    with open(filename, "w") as outf:
        print(len(border), file=outf)
        for coord in border:
            print(' '.join(coord), file=outf)


def main():
    if len(sys.argv) < 2:
        raise TypeError("Not enough arguments")
    coords, elements = plot.readfile(sys.argv[1])


if __name__ == "__main__":
    main()
