import math
import unittest
from NVException import negative_msg, NegativeValueException
def area(r):
    '''принимает в качестве аргумента радиус окружности r и возвращает
    площадь этой окружности'''
    return math.pi * r * r


def perimeter(r):
    '''принимает в качестве аргумента радиус окружности r и возвращает
    длинну этой окружности'''
    return 2 * math.pi * r


class CircleTests(unittest.TestCase):
    def test_area_1(self):
        res = area(2)
        self.assertEqual(res, 12.566370614359172)

    def test_area_2(self):
        res = area(7)
        self.assertEqual(res, 153.93804002589985)

    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_big_1(self):
        res = area(1600000)
        self.assertEqual(res, 8042477193189.87)

    def test_area_negative(self):
        with self.assertRaises(NegativeValueException) as context:
            area(-1)
        self.assertEqual(str(context.exception), negative_msg)

    def test_area_big_2(self):
        res = area(600000)
        self.assertEqual(res, 1130973355292.3254)

    def test_perimeter_1(self):
        res = perimeter(1)
        self.assertEqual(res, 6.283185307179586)

    def test_perimeter_2(self):
        res = perimeter(10)
        self.assertEqual(res, 62.83185307179586)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_big_1(self):
        res = perimeter(10000000)
        self.assertEqual(res, 62831853.071795866)

    def test_perimeter_big_2(self):
        res = perimeter(400000000)
        self.assertEqual(res, 2513274122.8718343)

    def test_perimeter_negative(self):
        with self.assertRaises(NegativeValueException) as context:
            area(-1)
        self.assertEqual(str(context.exception), negative_msg)
