import unittest

from geom2d.point import Point
from geom2d.vector import Vector


# python3 -m unittest geom2d/point_test.py
class TestPoint(unittest.TestCase):
    u = Point(1, 2)
    v = Point(4, 6)

    def test_plus(self):
        expected = Point(5, 8)
        actual = self.u + self.v
        self.assertEqual(expected, actual)
        
    def test_minus(self):
        expected = Vector(-3, -4)
        actual = self.u - self.v
        self.assertEqual(expected, actual)

    def test_distance_to(self):
        expected = 5
        actual = self.u.distance_to(self.v)

        self.assertAlmostEqual(expected, actual)
