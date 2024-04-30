#  Python Data Structure Challenges in Real-World Scenarios
# Objective:
# This assignment is designed to enhance your understanding and 
# application of Python's core data structures - tuples, lists, and dictionaries - 
# in real-world contexts. By engaging with these tasks, you will practice manipulating t
# hese data structures, applying built-in Python methods, and implementing error handling 
# in practical situations.
# Task 1: Library System Enhancement
# Sharpen your skills in managing and modifying data within tuples and lists.
# Problem Statement:

# You are maintaining a library system where each book is stored as a tuple within a list.
# Your task is to update this system by adding new books and ensuring no duplicates.
# Existing Library Data:
# library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
# Add functionality to insert new books into library.
# Ensure that adding a duplicate book is handled appropriately.



def library_entry(library):
    book = input('what would you like to check out ?>>')
    auther = input('who wrote this book >>')
    newbook=((book.title(),auther.title()))
    if newbook not in library:
            library.append(newbook)
    print(library)
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]   
library_entry(library)
                    