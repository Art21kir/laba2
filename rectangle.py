import unittest
from NVException import negative_msg, NegativeValueException

def area(a, b):
    '''принимает в качестве аргумента стороны прямоугольника a, b
    и возвращает площадь этого прямоугольника'''
    return a * b


def perimeter(a, b):
    '''принимает в качестве аргумента стороны прямоугольника a, b
    и возвращает периметр этого прямоугольника'''
    return 2 * (a +  b)

class RectangleTests(unittest.TestCase):
    def test_area_1(self):
        res = area(2, 3)
        self.assertEqual(res, 6)

    def test_area_2(self):
        res = area(7, 4)
        self.assertEqual(res, 28)

    def test_area_square_1(self):
        res = area(2, 2)
        self.assertEqual(res, 4)

    def test_area_square_2(self):
        res = area(5, 5)
        self.assertEqual(res, 25)

    def test_area_zero_side_1(self):
        res = area(0, 5)
        self.assertEqual(res, 0)

    def test_area_zero_side_2(self):
        res = area(5, 0)
        self.assertEqual(res, 0)

    def test_area_zero_both(self):
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_area_side_big_1(self):
        res = area(160000000000000000, 4)
        self.assertEqual(res, 640000000000000000)

    def test_area_side_big_2(self):
        res = area(4, 3200000000000000000)
        self.assertEqual(res, 12800000000000000000)

    def test_area_both_big(self):
        res = area(400000000000, 1600000000000)
        self.assertEqual(res, 640000000000000000000000)

    def test_area_negative(self):
        with self.assertRaises(NegativeValueException) as context:
            area(-1, 1)
        self.assertEqual(str(context.exception), negative_msg)

    def test_perimeter_1(self):
        res = perimeter(1, 2)
        self.assertEqual(res, 6)

    def test_perimeter_2(self):
        res = perimeter(3, 4)
        self.assertEqual(res, 14)

    def test_perimeter_square_1(self):
        res = perimeter(2, 2)
        self.assertEqual(res, 8)

    def test_perimeter_square_2(self):
        res = perimeter(5, 5)
        self.assertEqual(res, 20)

    def test_perimeter_zero(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_big(self):
        res = perimeter(10000000, 2000000)
        self.assertEqual(res, 24000000)

    def test_perimeter_negative(self):
        with self.assertRaises(NegativeValueException) as context:
            perimeter(-1, 1)
        self.assertEqual(str(context.exception), negative_msg)
