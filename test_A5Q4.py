import unittest

from A5Q4_postal_codes import get_details_from_postal_code


class TestA5Q4(unittest.TestCase):
    def test_a5q4t1(self):
        self.assertEqual(['Newfoundland', 'urban'], get_details_from_postal_code('A1A 2B3'))

    def test_a5q4t2(self):
        self.assertEqual(['Nunavut or Northwest Territories', 'rural'], get_details_from_postal_code('X0a 5b3'))

    def test_a5q4t3(self):
        self.assertEqual(["Alberta", 'urban'], get_details_from_postal_code('t2A 1q2'))

    def test_a5q4t4(self):
        self.assertEqual(["Ontario", 'urban'], get_details_from_postal_code('M3A 1Q2'))

    def test_a5q4t5(self):
        self.assertEqual(["Quebec", 'urban'], get_details_from_postal_code('h4A 1q2'))

    def test_a5q4t6(self):
        with self.assertRaises(TypeError):
            get_details_from_postal_code(True)

    def test_a5q4t7(self):
        with self.assertRaises(ValueError):
            get_details_from_postal_code("A1A  1A1")

    def test_a5q4t8(self):
        with self.assertRaises(ValueError):
            get_details_from_postal_code("A1A 1A1A")

    def test_a5q4t9(self):
        with self.assertRaises(ValueError):
            get_details_from_postal_code("AB1 1A1")

    def test_a5q4t10(self):
        with self.assertRaises(ValueError):
            get_details_from_postal_code("31A 1A1")

    def test_a5q4t11(self):
        with self.assertRaises(ValueError):
            get_details_from_postal_code("51A 4A1")

    def test_a5q4t12(self):
        with self.assertRaises(ValueError):
            get_details_from_postal_code("A1A 161")

    def test_a5q4t13(self):
        with self.assertRaises(ValueError):
            get_details_from_postal_code("A1A 1AN")

    def test_a5q4t13(self):
        with self.assertRaises(ValueError):
            get_details_from_postal_code("A1A YA1")
