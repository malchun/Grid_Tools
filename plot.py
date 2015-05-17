#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import sys


def readfile(filename):
    """Reads points and elements from files (.out)

    filename - name of .out file with grid

    return: list of coords and list of elements
    """
    with open(filename, 'r') as fn:
        def getpoint():
            return [float(x) for x in fn.readline().split(' ')]
        def getelement():
            return [int(x) for x in fn.readline().split(' ')]
        np = int(fn.readline().strip())
        coords = []
        for _ in range(np):
            coords.append(getpoint())
        ne = int(fn.readline().strip())
        elements = []
        for _ in range(ne):
            elements.append(getelement())
        return coords, elements



def plot_points(coords):
    """Plots points in 3d grid
    
    coords - list of coords
    
    return: None
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    tmpcoords = [list(a) for a in zip(*coords)]
    ax.scatter(tmpcoords[0], tmpcoords[1], tmpcoords[2], c='r', marker='o')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()


def main():
    if len(sys.argv) < 3:
        raise TypeError("Not enough arguments")
    filename = sys.argv[1]
    coords, elements = readfile(filename)
    plot_points(coords)
    filename = sys.argv[2]
    coords, elements = readfile(filename)
    plot_points(coords)



if __name__ == "__main__":
    main()
