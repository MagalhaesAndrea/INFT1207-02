import unittest
from main import find_minimum

class TestMinimumFunction(unittest.TestCase):

    def test_case_1(self):
        # Test Case 1: Very short list with 1, 2, or 3 elements
        self.assertEqual(find_minimum([90]), 90)  # Single element
        self.assertEqual(find_minimum([12, 10]), 10)  # Two elements
        self.assertEqual(find_minimum([10, 12]), 10)
        self.assertEqual(find_minimum([36, 14, 12]), 12)  # Three elements
        self.assertEqual(find_minimum([12, 36, 14]),12)
        self.assertEqual(find_minimum([14, 12, 36]), 12)

    def test_case_2(self):
        # Test Case 2: Empty list (size 0)
        with self.assertRaises(ValueError):
            find_minimum([])

    def test_case_3(self):
        # Test Case 3: Minimum element is the first or last elements
        self.assertEqual(find_minimum([10, 23, 34, 81, 97]), 10)
        self.assertEqual(find_minimum([97, 81, 34, 23, 10]), 10)

    def test_case_4(self):
        # Test Case 4: A list where the minimum element is negative
        self.assertEqual(find_minimum([10, -2, 5, 23]), -2)
        self.assertEqual(find_minimum([10, -2, -24, 4]), -24)

    def test_case_5(self):
        # Test Case 5: All elements are negative
        self.assertEqual(find_minimum([-23, -31, -45, -56]), -56)
        self.assertEqual(find_minimum([-6, -203, -2, -78]), -203)

    def test_case_6(self):
        # Test Case 6: List with some real numbers
        with self.assertRaises(ValueError):
            find_minimum([23, 34.56, 67, 33])

    def test_case_7(self):
        # Test Case 7: List with alphabetic and special characters
        with self.assertRaises(ValueError):
            find_minimum([23, "hi", 32, 1])
        with self.assertRaises(ValueError):
            find_minimum([12, "&", "*", "34m", "!"])

    def test_case_8(self):
        # Test Case 8: List with duplicate elements
        self.assertEqual(find_minimum([3, 4, 6, 9, 6]), 3)
        self.assertEqual(find_minimum([13, 6, 6, 9, 15]), 6)

    def test_case_9(self):
        # Test Case 9: : A list where one element has a value greater than the maximum permissible
        # limit of an integer.
        self.assertEqual(find_minimum([530, 429449672, 97, 23, 46, 59]), 23)


if __name__ == "__main__":
    unittest.main()