import unittest

from A5Q2_convert import convert_feet_and_inches_to_meters


class Test_A5Q2(unittest.TestCase):
    def test_a5q2t1(self):
        self.assertAlmostEqual(1.7271999999999998, convert_feet_and_inches_to_meters(5, 8))

    def test_a5q2t2(self):
        self.assertAlmostEqual(0.7111999999999999, convert_feet_and_inches_to_meters(2, 4))

    def test_a5q2t3(self):
        with self.assertRaises(TypeError):
            convert_feet_and_inches_to_meters([2], 4)

    def test_a5q2t4(self):
        with self.assertRaises(TypeError):
            convert_feet_and_inches_to_meters(2, {4:8})

    def test_a5q2t5(self):
        with self.assertRaises(ValueError):
            convert_feet_and_inches_to_meters(2, 12.1)

    def test_a5q2t6(self):
        with self.assertRaises(ValueError):
            convert_feet_and_inches_to_meters(2, -0.1)