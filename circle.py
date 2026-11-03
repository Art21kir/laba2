import math
import unittest

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
        self.assertEqual(res, 4 * math.pi)

    def test_area_2(self):
        res = area(7)
        self.assertEqual(res, 49 * math.pi)

    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_big_1(self):
        res = area(1600000)
        self.assertEqual(res, 2560000000000 * math.pi)

    def test_area_big_2(self):
        res = area(600000)
        self.assertEqual(res, 360000000000 * math.pi)

    def test_perimeter_1(self):
        res = perimeter(1)
        self.assertEqual(res, 2 * math.pi)

    def test_perimeter_2(self):
        res = perimeter(10)
        self.assertEqual(res, 20 * math.pi)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_big_1(self):
        res = perimeter(10000000)
        self.assertEqual(res, 20000000 * math.pi)

    def test_perimeter_big_2(self):
        res = perimeter(400000000)
        self.assertEqual(res, 800000000 * math.pi)
