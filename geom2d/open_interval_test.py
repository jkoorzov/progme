import unittest

from geom2d.open_interval import OpenInterval

class TestOpenInterval(unittest.TestCase):
    def test_overlaps_interval1(self):
        a = OpenInterval(1, 5)
        b = OpenInterval(6, 8)
        self.assertFalse(a.overlaps_interval(b))

    def test_overlaps_interval2(self):
        a = OpenInterval(1, 5)
        b = OpenInterval(4, 7)
        self.assertTrue(a.overlaps_interval(b))

    def test_overlaps_interval3(self):
        a = OpenInterval(1, 5)
        b = OpenInterval(2, 4)
        self.assertTrue(a.overlaps_interval(b))

    def test_overlaps_interval4(self):
        a = OpenInterval(4, 6)
        b = OpenInterval(1, 5)
        self.assertTrue(a.overlaps_interval(b))

    def test_overlaps_interval5(self):
        a = OpenInterval(2, 4)
        b = OpenInterval(1, 5)
        self.assertTrue(a.overlaps_interval(b))

    def test_overlaps_interval6(self):
        a = OpenInterval(1, 4)
        b = OpenInterval(6, 8)
        self.assertFalse(a.overlaps_interval(b))