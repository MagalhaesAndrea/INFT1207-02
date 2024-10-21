# Name: Andrea Magalhaes
# Date: October 10, 2024
# Document Type: Python
# Description: A function was written that will pass all the test cases
#   in the file test_minimum.py

# Function for finding the minimum integer - pass a list of elements as parameter
def find_minimum(elements):
    # If the list is empty raise an error
    if not elements:
        raise ValueError("The list is empty!")

    # Create a loop to check if each element in list is an integer
    for element in elements:
        if not isinstance(element, int):
            # raise and error if there is an element that is not an integer
            raise ValueError("The input must be an integer!")

    # Start by storing this first element in the list as the minimum
    min_element = elements[0]
    # Check if each item in the list is lower than the first element
    for element in elements:
        if element < min_element:
            # Store the element that is the minimum/lowest
            min_element = element

    return min_element