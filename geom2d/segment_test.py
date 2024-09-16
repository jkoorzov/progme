import math
import unittest

from geom2d.point import Point
from geom2d.segment import Segment
from geom2d.vector import Vector
from geom2d import tparam


class TestSegment(unittest.TestCase):

    start = Point(400, 0)
    end = Point(0, 400)
    segment = Segment(start, end)
    length = 400 * math.sqrt(2)

    def test_length(self):
        expected = 400 * math.sqrt(2)
        actual = self.segment.length
        self.assertAlmostEqual(expected, actual)

    def test_direction_vector(self):
        expected = Vector(
            self.end.x - self.start.x, 
            self.end.y - self.start.y
            )
        actual = self.segment.direction_vector
        self.assertAlmostEqual(expected, actual)

    def test_direction_versor(self):
        expected = Vector(
            (self.end.x - self.start.x) / self.length, 
            (self.end.y - self.start.y) / self.length)
        actual = self.segment.direction_versor
        self.assertAlmostEqual(expected, actual)

    """
    def test_normal_versor(self):
        expected = Vector(
            - (self.end.x - self.start.x) / self.length, 
            (self.end.y - self.start.y) / self.length)
        actual = self.segment.normal_versor
        self.assertAlmostEqual(expected, actual)
    """

    def test_point_at_wrong_t(self):
        self.assertRaises(
            tparam.TParamError,
            self.segment.point_at,
            56.7
        )

    def test_point_at(self):
        t = tparam.make(0.25)
        expected = Point(300, 100)
        actual = self.segment.point_at(t)
        self.assertEqual(expected, actual)

    def test_middle_point(self):
        expected = Point(200, 200)
        actual = self.segment.middle
        self.assertEqual(expected, actual)

    def test_closest_point_is_start(self):
        p = Point(500, 20)
        expected = self.start
        actual = self.segment.closest_point_to(p)
        self.assertEqual(expected, actual)

    def test_closest_point_is_end(self):
        p = Point(20, 500)
        expected = self.end
        actual = self.segment.closest_point_to(p)
        self.assertEqual(expected, actual)

    def test_closest_point_is_middle(self):
        p = Point(250, 250)
        expected = Point(200, 200)
        actual = self.segment.closest_point_to(p)
        self.assertEqual(expected, actual)

    def test_parallel_segments_no_intersection(self):
        other = Segment(Point(200, 0), Point(0, 200))
        actual = self.segment.intersection_with(other)
        self.assertIsNone(actual)

    def test_segments_intersection(self):
        other = Segment(Point(0, 0), Point(400, 400))
        expected = Point(200, 200)
        actual = self.segment.intersection_with(other)
        self.assertEqual(expected, actual)

    def test_segments_both_out_of_range(self):
        other = Segment(Point(500, 0), Point(0, 500))
        actual = self.segment.intersection_with(other)
        self.assertIsNone(actual)

    def test_segments_both_out_of_range(self):
        other = Segment(Point(450, 0), Point(0, 550))
        actual = self.segment.intersection_with(other)
        self.assertIsNone(actual)

    def test_segments_t1_out_of_range(self):
        other = Segment(Point(-100, 300), Point(0, 550))
        actual = self.segment.intersection_with(other)
        self.assertIsNone(actual)

    def test_segments_t2_out_of_range(self):
        other = Segment(Point(300, 300), Point(400, 400))
        actual = self.segment.intersection_with(other)
        self.assertIsNone(actual)