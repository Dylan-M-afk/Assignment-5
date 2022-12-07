import unittest

from A5Q3_get_season import get_season


class Test_A5Q2(unittest.TestCase):
    def test_a5q3t1(self):
        self.assertEqual("Fall", get_season("September", 22))

    def test_a5q3t2(self):
        self.assertEqual("Fall", get_season("December", 20))

    def test_a5q3t3(self):
        self.assertEqual("Winter", get_season("December", 21))

    def test_a5q3t4(self):
        self.assertEqual("Winter", get_season("January", 31))

    def test_a5q3t5(self):
        self.assertEqual("Winter", get_season("March", 19))

    def test_a5q3t6(self):
        self.assertEqual("Spring", get_season("March", 20))

    def test_a5q3t7(self):
        self.assertEqual("Spring", get_season("April", 1))

    def test_a5q3t8(self):
        self.assertEqual("Spring", get_season("June", 20))

    def test_a5q3t9(self):
        self.assertEqual("Summer", get_season("June", 21))

    def test_a5q3t10(self):
        self.assertEqual("Summer", get_season("September", 21))

    def test_a5q3t11(self):
        with self.assertRaises(ValueError):
            get_season("April", 31)

    def test_a5q3t12(self):
        with self.assertRaises(ValueError):
            get_season("May", 0)

    def test_a5q3t13(self):
        with self.assertRaises(ValueError):
            get_season("February", 30)

    def test_a5q3t14(self):
        with self.assertRaises(ValueError):
            get_season("December", 32)

    def test_a5q3t15(self):
        with self.assertRaises(ValueError):
            get_season("Not a month", 10)

    def test_a5q3t16(self):
        with self.assertRaises(AssertionError):
            get_season(['May'], 20)
