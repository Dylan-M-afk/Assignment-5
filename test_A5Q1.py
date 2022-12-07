import unittest

from A5Q1_duration_calculator import duration_in_seconds


class Test_A5Q1(unittest.TestCase):
    def test_a5q1t1(self):
        self.assertEqual(443162.5, duration_in_seconds(5, 3, 6, 2.5))

    def test_a5q1t2(self):
        self.assertEqual(371289.1, duration_in_seconds(4, 7, 8, 9.1))

    def test_a5q1t3(self):
        with self.assertRaises(AssertionError):
            duration_in_seconds(4, 7, '8', 9)

    def test_a5q1t4(self):
        with self.assertRaises(AssertionError):
            duration_in_seconds(4.5, 6, 8, 9.4)

    def test_a5q1t5(self):
        with self.assertRaises(ValueError):
            duration_in_seconds(4, 61, 8, 9.6)

    def test_a5q1t6(self):
        with self.assertRaises(ValueError):
            duration_in_seconds(4, 1, -1, 9.1)

    def test_a5q1t7(self):
        with self.assertRaises(ValueError):
            duration_in_seconds(4, 1, 1, 60.1)
