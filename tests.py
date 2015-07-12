#!/usr/bin/env python3

import unittest
import bordfinder


class TestBorderFaces(unittest.TestCase):
    test_figures = ['cube', 'tetrahedron']
    points = {'cube': [(0.0, 0.0, 0.0),
        (1.0, 0.0, 0.0),
        (1.0, 1.0, 0.0),
        (0.0, 1.0, 0.0),
        (0.0, 0.0, 1.0),
        (1.0, 0.0, 1.0),
        (1.0, 1.0, 1.0),
        (0.0, 1.0, 1.0)],
        'tetrahedron': [(0.0, 0.0, 0.0),
        (1.0, 0.0, 0.0),
        (0.0, 1.0, 0.0),
        (0.0, 0.0, 1.0)]
    }
    elements = {'cube': [(0, 1, 2, 5),
        (0, 2, 3, 7),
        (0, 4, 5, 7),
        (2, 5, 6, 7),
        (0, 2, 5, 7)],
        'tetrahedron': [(0, 1, 2, 3)]
    }
    border_faces = {'cube': [(0, 4, 7),
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
        (4, 5, 7)],
        'tetrahedron': [(0, 1, 2),
        (0, 1, 3),
        (0, 2, 3),
        (1, 2, 3)]
    }

    def test_find_border_faces(self): 
        """Testing border faces finder"""
        for name in self.test_figures:
            result = set(bordfinder.find_border_faces(self.elements[name]))
            self.assertEqual(set(self.border_faces[name]), result)


if __name__ == "__main__":
    unittest.main()
