#!/usr/bin/env python3

import sys

import plot


def tetrahedrons_as_sets(tetr_list):
    """Generator. Makes sets of faces for each tetra-element in list
    
    tetr_list - list of 4-point tethrahedrons

    return: sets of 3-point faces
    """
    def faces(tetr):
        sorted_tetr = sorted(tetr)
    
        yield (tetr[0], tetr[1], tetr[2])
        yield (tetr[1], tetr[2], tetr[3])
        yield (tetr[0], tetr[2], tetr[3])
        yield (tetr[0], tetr[1], tetr[3])
    
    yield from (set(faces(tetr)) for tetr in tetr_list)


def find_border_faces(elements):
    """Finds borders faces

    elements - list of elements

    return: set of border faces
    """
    
    yield from (reduce(xor, tetrahedrons_as_sets(tetr_list)))


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
    raise IOError("Can't write border to file")


def main():
    if len(sys.argv) < 2:
        raise TypeError("Not enough arguments")
    coords, elements = plot.readfile(sys.argv[1])


if __name__ == "__main__":
    main()
