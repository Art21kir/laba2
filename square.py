import unittest
def area(a):
    '''принимает в качестве аргумента сторону квадрата a и возвращает
    площадь этого квадрата'''
    return a * a


def perimeter(a):
    '''принимает в качестве аргумента сторону квадрата a и возвращает
    периметр этого квадрата'''
    return 4 * a

class SquareTests(unittest.TestCase):
    def test_area_1(self):
        res = area(2)
        self.assertEqual(res, 4)

    def test_area_2(self):
        res = area(5)
        self.assertEqual(res, 25)

    def test_area_3(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_big_1(self):
        res = area(4000000)
        self.assertEqual(res, 16000000000000)

    def test_area_big_2(self):
        res = area(16000000)
        self.assertEqual(res, 256000000000000)

    def test_perimeter_1(self):
        res = perimeter(1)
        self.assertEqual(res, 4)

    def test_perimeter_2(self):
        res = perimeter(5)
        self.assertEqual(res, 20)

    def test_perimeter_3(self):
        res = perimeter(25)
        self.assertEqual(res, 100)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_big_1(self):
        res = perimeter(10000000)
        self.assertEqual(res, 40000000)

    def test_perimeter_big_2(self):
        res = perimeter(21212121212121)
        self.assertEqual(res, 84848484848484)
