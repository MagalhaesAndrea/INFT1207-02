# test reading_list.py

import csv
import os
import unittest
from reading_list import add_book, list_books, search_book, delete_book



class TestReadingList(unittest.TestCase):

    # test case one - add function - valid input that tests year range
    def test_add_one(self):
        self.assertEqual(add_book("Test Book", "Author Name", 1885), "Book added!")
        self.assertEqual(add_book("Test Book Two", "Author Name", 2024), "Book added!")
        self.assertEqual(add_book("Test Book Three", "Author Name", 1), "Book added!")
        #
        # Assert if the book is added (by manually checking CSV or creating validation logic)

    # test case two - add function - years entries that should not pass
    def test_add_two(self):
        self.assertEqual(add_book("Test Book", "Author Name", "Beep"),"Year entered must be a valid integer!")
        self.assertEqual(add_book("Test Book", "Author Name", 0),"Error! Year entered is invalid!")
        self.assertEqual(add_book("Test Book", "Author Name", 2025),"Error! Year entered is invalid!")

    # test case three - add function - empty field for input
    def test_add_three(self):
        self.assertEqual(add_book("","Author",2023),"Error! Cannot leave any options empty!")
        self.assertEqual(add_book("Title","",2023),"Error! Cannot leave any options empty!")
        self.assertEqual(add_book("Title","Author",None),"Year entered must be a valid integer!")

    # test case four - search function - input a book that is not in the list
    def test_search_one(self):
        self.assertEqual(search_book("Test"),"Book not found")
        # Assert the output of the search

    # test case five - search function - input a book that is in the list
    def test_search_two(self):
        self.assertEqual(search_book("1Q84"),"Found: Title: 1Q84, Author: Haruki Murakami, Year: 2009")

    # test case six - search function - leave the input empty
    def test_search_three(self):
        self.assertEqual(search_book(""),"Error! Cannot leave field empty!")

    # test case seven - delete function - Try to delete a book that is not in the list
    def test_delete_one(self):
        self.assertEqual(delete_book("Test"),'Not Found! Was not deleted!')

    # test case eight - delete function - successfully deleting a book
    def test_delete_two(self):
        delete_book("The Picture of Dorian Gray")
        self.assertEqual(search_book("The Picture of Dorian Gray"), "Book not found")

    # test case nine - list function - check if list is printed
    def test_list_one(self):
        self.assertEqual(list_books(),'Printed!')

    # test case ten - list function - check if list is empty
    def test_list_two(self):
        file_path = 'books.csv'
        with open(file_path, 'w') as file:
            pass
        result = list_books()
        self.assertFalse(result, "Error! File Empty!")


if __name__ == '__main__':
    unittest.main()