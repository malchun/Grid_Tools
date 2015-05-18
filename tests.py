#!/usr/bin/env python3

import unittest
import bordfinder


class TestBorderFaces(unittest.TestCase):
    points = [(0.0, 0.0, 0.0),
        (1.0, 0.0, 0.0),
        (1.0, 1.0, 0.0),
        (0.0, 1.0, 0.0),
        (0.0, 0.0, 1.0),
        (1.0, 0.0, 1.0),
        (1.0, 1.0, 1.0),
        (0.0, 1.0, 1.0)
    ]
    elements = [[0, 1, 2, 5],
        [0, 2, 3, 7],
        [0, 4, 5, 7],
        [2, 5, 6, 7],
        [0, 2, 5, 7]
    ]
    faces = [(0, 4, 7),
        (0, 3, 7),
        (0, 4, 5),
        (0, 1, 5),
        (0, 2, 3),
        (0, 1, 2),
        (2, 3, 7),
        (2, 6, 7),
        (1, 2, 5),
        (2, 5, 6),
        (5, 6, 7),
        (4, 5, 7)
    ]

    def test_to_border_faces(self): 
#    """Testing border faces finder"""
        result = set(bordfinder.find_border_faces(self.elements))
        print(result)
        self.assertEqual(set(self.faces), result)


if __name__ == "__main__":
    unittest.main()
