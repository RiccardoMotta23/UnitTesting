import unittest
from math_utils import MathUtils

class TestMathUtils(unittest.TestCase):
    """
    Test class for math_utils
    """

    def test_add(self):
        self.assertEqual(MathUtils.add(1,2), 3)
        self.assertEqual(MathUtils.add(1.5, 2.5), 4.0 )
        self.assertEqual(MathUtils.add(-1, 1),0)
        self.assertEqual(MathUtils.add(-1.5, 1.5), 0.0)

    def test_subtract(self):
        self.assertEqual(MathUtils.subtract(1,2), -1)
        self.assertEqual(MathUtils.subtract(1.5, 2.5), -1)
        self.assertEqual(MathUtils.subtract(-1, 1),0)
        self.assertEqual(MathUtils.subtract(-1.5, 1.5), 0.0)

    def test_divide(self):
        self.assertEqual(MathUtils.divide(1, 2), 0.5)
        self.assertEqual(MathUtils.divide(1.5, 2.5), 4.0)
        self.assertEqual(MathUtils.divide(-1, 1), 0)
        self.assertEqual(MathUtils.divide(-1.5, 1.5), 0.0)