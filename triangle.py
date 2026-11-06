import unittest
from NVException import negative_msg, NegativeValueException
def area(a, h):
    '''принимает в качестве аргумента сторону a, высоту h треугольника
    и возвращает площадь этого треугольника'''
    return a * h / 2 

def perimeter(a, b, c):
    '''принимает в качестве аргумента стороны a, b, c треугольника
    и возвращает периметр этого треугольника'''
    return a + b + c

class TriangleTests(unittest.TestCase):
    def test_area_1(self):
        res = area(2, 2)
        self.assertEqual(res, 2)

    def test_area_2(self):
        res = area(7, 4)
        self.assertEqual(res, 14)

    def test_area_zero_side(self):
        res = area(0, 5)
        self.assertEqual(res, 0)

    def test_area_zero_height(self):
        res = area(5, 0)
        self.assertEqual(res, 0)

    def test_area_zero_both(self):
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_area_side_big(self):
        res = area(160000000000000000, 4)
        self.assertEqual(res, 320000000000000000)

    def test_area_height_big(self):
        res = area(4, 3200000000000000000)
        self.assertEqual(res, 6400000000000000000)

    def test_area_both_big(self):
        res = area(400000000000, 1600000000000)
        self.assertEqual(res, 320000000000000000000000)

    def test_area_negative(self):
        with self.assertRaises(NegativeValueException) as context:
            area(-1, 1)
        self.assertEqual(str(context.exception), negative_msg)

    def test_perimeter_1(self):
        res = perimeter(1, 1, 1)
        self.assertEqual(res, 3)

    def test_perimeter_2(self):
        res = perimeter(0, 1, 2)
        self.assertEqual(res, 3)

    def test_perimeter_zero(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_big(self):
        res = perimeter(10000000, 2000000, 300000)
        self.assertEqual(res, 12300000)

    def test_area_negative(self):
        with self.assertRaises(NegativeValueException) as context:
            perimeter(-1, 1, 1)
        self.assertEqual(str(context.exception), negative_msg)
