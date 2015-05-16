#!/usr/bin/env python3

import sys
from functools import reduce
from operator import xor

import plot


def tetrahedrons_as_sets(tetr_list):
    """Generator. Makes sets of faces for each tetra-element in list
    
    tetr_list - list of 4-point tethrahedrons

    return: sets of 3-point faces
    """
    def faces(tetr):
        sorted_tetr = sorted(tetr[:4])
        
        yield (sorted_tetr[0], sorted_tetr[1], sorted_tetr[2])
        yield (sorted_tetr[1], sorted_tetr[2], sorted_tetr[3])
        yield (sorted_tetr[0], sorted_tetr[2], sorted_tetr[3])
        yield (sorted_tetr[0], sorted_tetr[1], sorted_tetr[3])

    yield from (set(faces(tetr)) for tetr in tetr_list)


def find_border_faces(elements):
    """Finds borders faces. This function finds
    faces that occured only in one element.

    elements - list of elements

    return: set of border faces
    """
    
    yield from (reduce(xor, tetrahedrons_as_sets(elements)))


def write_border(filename, border):
    """Writes border into file

    filename - name of file (.out)
    border - list of points
    
    return: None
    """
    with open(filename, "w") as outf:
        print(len(border), file=outf)
        for coord in border:
            print(str(' '.join(str(x) for x in coord)), file=outf)
    raise IOError("Can't write border to file")


def read_border_faces(filename):
    """Reads border faces from file

    filename - name of file

    return: border_faces
    """
    with open(filename, "r") as borderf:
        n = int(borderf.readline().strip())
        border_faces = []
        def get_face():
            return [int(x) for x in borderf.readline().split(' ')]
        for _ in range(n):
            border_faces.append(get_face())
        return(border_faces)
    raise IOError("Can't read border")


def get_border_points(border_faces, coords):
    """Extracts points from border faces into list

    border_faces - list of faces
    coords - list of points

    return: list of points
    """
    border_points = []
    def border_faces_as_sets():
        for face in border_faces:
            yield set(face)
    for pointnum in reduce(xor, border_faces_as_sets()):
        border_points.append(coords[pointnum])
    return(border_points)


def main():
    if len(sys.argv) < 2:
        raise TypeError("Not enough arguments")
    border_faces = read_border_faces(sys.argv[1])
    print(border_faces)


if __name__ == "__main__":
    main()
