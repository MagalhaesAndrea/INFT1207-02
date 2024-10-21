import unittest

from test_Lab3_Andrea import TestShapes

def run_tests(choice):
    suite = unittest.TestSuite()

    if choice == 'c':
        # invalid and valid test cases for circle
        suite.addTest(TestShapes('test_circle_area_valid'))
        suite.addTest(TestShapes('test_circle_area_invalid'))
    elif choice == 't':
        # invalid and valid test cases for trapezium
        suite.addTest(TestShapes('test_trapezium_area_valid'))
        suite.addTest(TestShapes('test_trapezium_area_invalid'))
    elif choice == 'e':
        # invalid and valid test cases for ellipse
        suite.addTest(TestShapes('test_ellipse_area_valid'))
        suite.addTest(TestShapes('test_ellipse_area_invalid'))
    elif choice == 'r':
        # invalid and valid test cases for rhombus
        suite.addTest(TestShapes('test_rhombus_area_valid'))
        suite.addTest(TestShapes('test_rhombus_area_invalid'))
    else:
        print("Invalid choice. Exiting.")
        return

    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    print("Enter a shape to test ('c' for Circle, 't' for Trapezium, 'e' for Ellipse, 'r' for Rhombus):")
    choice = input().strip().lower()
    run_tests(choice)