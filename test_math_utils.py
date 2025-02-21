import math
import unittest
from math_utils import MathUtils

class TestMathUtils(unittest.TestCase):
    """
    Test class for math_utils
    """

    def test_add(self):
        self.assertEqual(MathUtils.add(1,2), 3)
        self.assertEqual(MathUtils.add(1.5, 2.5), 4.0)
        self.assertEqual(MathUtils.add(-1, 1),0)
        self.assertEqual(MathUtils.add(-1.5, 1.5), 0.0)

    def test_subtract(self):
        self.assertEqual(MathUtils.subtract(1,2), -1)
        self.assertEqual(MathUtils.subtract(1.5, 2.5), -1)
        self.assertEqual(MathUtils.subtract(-1, 1),-2)
        self.assertEqual(MathUtils.subtract(-1.5, 1.5), -3.0)

    def test_divide(self):
        self.assertEqual(MathUtils.divide(1, 2), 0.5)
        self.assertEqual(MathUtils.divide(1.5, 2.5), 0.6)
        self.assertEqual(MathUtils.divide(-1, 1), -1)
        self.assertEqual(MathUtils.divide(-1.5, 1.5), -1.0)
        with self.assertRaises(ValueError):
            MathUtils.divide(1,0)

    def test_sqrt(self):
        self.assertEqual(MathUtils.sqrt(4), 2)
        self.assertEqual(MathUtils.sqrt(9), 3)
        self.assertAlmostEqual(MathUtils.sqrt(2), 1.4142, places=4)
        self.assertEqual(MathUtils.sqrt(0), 0)

    def test_cos_value(self):
        self.assertAlmostEqual(MathUtils.cos_value(0), 1.0, places=4)
        self.assertAlmostEqual(MathUtils.cos_value(math.pi / 2), 0.0, places=4)
        self.assertAlmostEqual(MathUtils.cos_value(math.pi), -1.0, places=4)

    def test_sin_value(self):
        self.assertAlmostEqual(MathUtils.sin_value(0), 0.0, places=4)
        self.assertAlmostEqual(MathUtils.sin_value(math.pi / 2), 1.0, places=4)
        self.assertAlmostEqual(MathUtils.sin_value(math.pi), 0.0, places=4)

    def test_tan_value(self):
        self.assertAlmostEqual(MathUtils.tan_value(0), 0.0, places=4)
        self.assertAlmostEqual(MathUtils.tan_value(math.pi / 4), 1.0, places=4)
        self.assertAlmostEqual(MathUtils.tan_value(math.pi), 0.0, places=4)

    def test_log_value(self):
        self.assertEqual(MathUtils.log_value(1), 0)
        self.assertAlmostEqual(MathUtils.log_value(math.e), 1.0, places=4)
        self.assertAlmostEqual(MathUtils.log_value(100, 10), 2.0, places=4)

    def test_factorial_value(self):
        self.assertEqual(MathUtils.factorial_value(5), 120)
        self.assertEqual(MathUtils.factorial_value(0), 1)
        self.assertEqual(MathUtils.factorial_value(1), 1)

    def test_power_of_value(self):
        self.assertEqual(MathUtils.power_of(2,3), 8)
        self.assertEqual(MathUtils.power_of(1, 3), 1)
        self.assertEqual(MathUtils.power_of(5, 3), 125)
        self.assertEqual(MathUtils.power_of(3, 4), 200)