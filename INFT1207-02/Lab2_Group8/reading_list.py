# Names: Andrea Magalhaes and Ruth
# Program: Reading List
# Date: October 3, 2024
# Description: Running menu that depending on the option chosen will
#   add, delete, list, and search for books in a reading list

import csv
import os

# Constants
CURRENT_YEAR = 2024
LOWEST_YEAR = 1

# Function to add a book to the reading list
def add_book(title, author, year):
    if not isinstance(year, int):
        return "Year entered must be a valid integer!"
    elif year < LOWEST_YEAR or year > CURRENT_YEAR:
        return "Error! Year entered is invalid!"
    elif not title or not author:
        return "Error! Cannot leave any options empty!"
    else:
        with open('books.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([title, author, year])
        return "Book added!"



# Function to list all books
def list_books():
    file_path = 'books.csv'
    if not os.path.exists(file_path):
        return "Error! File Empty!"

    else:
        with open('books.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(f'Title: {row[0]}, Author: {row[1]}, Year: {row[2]}')
                return 'Printed!'


# Function to search for a book by title
def search_book(title):
    if not title:
        return "Error! Cannot leave field empty!"
    else:
        with open('books.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0].lower() == title.lower():
                    return f'Found: Title: {row[0]}, Author: {row[1]}, Year: {row[2]}'
            return 'Book not found'


# Function to delete a book by title
def delete_book(title):
    found = False
    with open('books.csv', mode='r') as file:
        reader = list(csv.reader(file))
    with open('books.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in reader:
            if row[0].lower() == title.lower():
                found = True
                print(f'Successfully Deleted: {title}')
            else:
                writer.writerow(row)
    if found == False:
        print(f"Book titled {title}, cannot be found in the list!")
        return 'Not Found! Was not deleted!'



# Menu loop
def menu():
    while True:
        print("\n1. Add Book\n2. List Books\n3. Search Book\n4. Delete Book\n5. Quit")
        choice = input("Select an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            year = input("Enter year of publication: ")
            add_book(title, author, year)
        elif choice == '2':
            list_books()
        elif choice == '3':
            title = input("Enter book title to search: ")
            search_book(title)
        elif choice == '4':
            title = input("Enter book title to delete: ")
            delete_book(title)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

# Run the program
if __name__ == "__main__":
    menu()