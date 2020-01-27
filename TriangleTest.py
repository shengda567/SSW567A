import unittest
from .homework1 import classfiy_triangle
class TestTriangles(unittest.TestCase):
    def testRightTriangleA(self):
        self.assertEqual(classfiy_triangle(3, 4, 5), 'Right')

    def testRightTriangleB(self):
        self.assertEqual(classfiy_triangle(5, 3, 4), 'Right')

    def testEquilateralTriangles(self):
        self.assertEqual(classfiy_triangle(1, 1, 1), 'Equilateral')

    def testIsoscelesTrianglesA(self):
        self.assertEqual(classfiy_triangle(5, 5, 7), 'Isosceles')

    def testIsoscelesTrianglesB(self):
        self.assertEqual(classfiy_triangle(5, 7, 7), 'Isosceles')

    def testScaleneTriangles(self):
        self.assertEqual(classfiy_triangle(5, 6, 7), 'Scalene')

    def testNotATriangle(self):
        self.assertEqual(classfiy_triangle(3, 4, 10), 'NotATriangle')

    def testInvalidA(self):
        self.assertEqual(classfiy_triangle(5, 0, 3), "InvalidInput")

    def testInvalidB(self):
        self.assertEqual(classfiy_triangle('I', 203, 162), "InvalidInput")

    def testInvalidC(self):
        self.assertEqual(classfiy_triangle(5.5, 3, 3), "InvalidInput")


if __name__ == '__main__':
    print('test triangle')
    unittest.main()