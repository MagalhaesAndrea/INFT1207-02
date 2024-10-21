import unittest
from app.Lab3_Andrea import circle_area, trapezium_area, ellipse_area, rhombus_area


class TestShapes(unittest.TestCase):

    def setUp(self):
        print("Setup: Preparing tests...")

    def tearDown(self):
        print("Teardown: Cleaning up after tests...")

    # testing valid input for circle
    def test_circle_area_valid(self):
        self.assertAlmostEqual(circle_area(3), 28.274333882308138)
        self.assertEqual(circle_area(0),0)

    # testing invalid input for circle - negative numbers
    def test_circle_area_invalid(self):
        with self.assertRaises(ValueError):
            circle_area(-1)

    # testing valid input for trapezium
    def test_trapezium_area_valid(self):
        self.assertEqual(trapezium_area(5,2,6),21)

    # testing invalid input for trapezium - negative numbers
    def test_trapezium_area_invalid(self):
        self.assertEqual(trapezium_area(-5, 2, 6),"Invalid! Must be a non-negative number!")
        self.assertEqual(trapezium_area(5, -2, 6),"Invalid! Must be a non-negative number!")
        self.assertEqual(trapezium_area(5, 2, -6), "Invalid! Must be a non-negative number!")

    # testing valid input for ellipse
    def test_ellipse_area_valid(self):
        self.assertEqual(ellipse_area(2, 4),25.132741228718345)
        self.assertEqual(ellipse_area(5.5, 9.25),159.8285262513807)

    # testing invalid input for ellipse - negative numbers
    def test_ellipse_area_invalid(self):
        self.assertEqual(ellipse_area(-3,4),"Invalid! Must be a non-negative number!")
        self.assertEqual(ellipse_area(3, -4),"Invalid! Must be a non-negative number!")

    # testing valid input for rhombus
    def test_rhombus_area_valid(self):
        self.assertEqual(rhombus_area(4, 2),4)
        self.assertEqual(rhombus_area(9.25, 5.5),25.4375)

    # testing invalid input for rhombus - negative numbers
    def test_rhombus_area_invalid(self):
        self.assertEqual(rhombus_area(-1, 3),"Invalid! Must be a non-negative number!")
        self.assertEqual(rhombus_area(1, -3), "Invalid! Must be a non-negative number!")




if __name__ == "__main__":
    unittest.main()