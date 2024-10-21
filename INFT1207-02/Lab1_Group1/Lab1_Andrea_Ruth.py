import random
import string

# Names: Andrea and Ruth
# File: Advanced Python
# Date: September 20, 2024
# Description: This program create a randomized password after receiving desired length,
#   number of letters, number of digits, and number of special characters

# variables
# Set minimum password length
minimum_length = 8
# lower limit of range
lower_limit = 1
# one character of each type is required - start with subtracting two from total when asking
#   for letters. Subtract one each time a value is stored
one_per_qualification = 2


# Title
print("Random Password Generator")

# Validation variable that becomes true when value can be stored
valid = False
# While loop that exits when valid input is provided
while valid == False:
    # Ask for input and try to store as integer
    try:
        password_length = int(input("Enter the length of the password: "))
        # Password length must be equal to or greater than eight
        if password_length >= minimum_length:
            valid = True
        # Error if input is not within valid range
        else:
            print("Please enter a value of greater than or equal to 8 to create a secure password")
    # Error if input is not an integer
    except:
        print("Error, input must be an integer")



# For upper limit in range, subtract the number of attributes left from the password length
upper_limit = password_length - one_per_qualification


valid = False
# While loop that exits when valid input is provided
while valid == False:
    # Ask for input and try to store as integer
    try:
        number_of_letters = int(input("Enter the number of letter desired in the password: "))

        # Letters must be at least one and can be greater than or equal to the length of the password
        #   minus the amount of attributes left
        if number_of_letters >= lower_limit and number_of_letters <= upper_limit:
            random_letters = random.sample(string.ascii_letters, number_of_letters)
            valid = True
        # Error if input is not within valid range
        else:
            print(f"Error! The number of letters should be in the range of "
                  f"{lower_limit} and {upper_limit}")
    # Error if input is not an integer
    except:
        print("Error, input must be an integer")

# For upper limit, subtract number of letters chosen and one attribute as you move to the next
upper_limit -= number_of_letters - lower_limit
valid = False
# While loop that exits when valid input is provided
while valid == False:
    # Ask for input and try to store as integer
    try:
        number_of_digits = int(input("Enter the number of digits desired in the password: "))
        # Digits must be at least one and can be greater than or equal to the length of the password

        #   minus the amount of attributes left and the number of letter chosen
        if number_of_digits >= lower_limit and number_of_digits <= upper_limit:
            valid = True
            random_numbers = random.sample(string.digits, number_of_digits)
        # Error if input is not within valid range
        else:
            print(f"Error! The number of digits should be in the range of "
                  f"{lower_limit} and {upper_limit}")
    # Error if input is not an integer
    except:
        print("Error, input must be an integer")

# For remaining upper limit, subtract number of digits and another attribute when moving to the last
upper_limit -= number_of_digits - lower_limit
valid = False
# While loop that exits when valid input is provided
while valid == False:
    # Ask for input and try to store as integer
    try:
        number_of_special = int(input("Enter the number of special characters desired in the password: "))
        # Special character must be at least one and can be greater than or equal to the length of the password
        random_special_characters = random.sample(string.punctuation, number_of_special)
        #   minus the amount of attributes left, the number of letters, and the number of digits.
        if number_of_special == upper_limit:
            valid = True
        # Error if input is not within valid range
        else:
            print(f"Error! The number of characters should be equal to "
                  f"{upper_limit}")
    # Error if input is not an integer
    except:
        print("Error, input must be an integer")

# Print output
print("Your unique password is being generated.......")
# Put all randomized characterized together and then shuffle them
password = random_letters + random_numbers + random_special_characters
randomized_password = random.sample(password, password_length)
# Print the randomized password
print("The desired password is:")
print(''.join(randomized_password))
