# Write a custom exception  that inherits from `Exception()`
# Open and read in the content of the book `.txt` files in the `books/` folder
# like you did in the previous exercise.
# Raise your `PrinceException()` if the first 100 characters of a book
# contain the string "Prince".

# Write a custom exception  that inherits from `Exception()`
war_and_peace_path = "/Users/davidiraheta/Documents/CodingNomads/python-301-main/05_exceptions/books/war_and_peace.txt"
crime_and_punishment_path = "/Users/davidiraheta/Documents/CodingNomads/python-301-main/05_exceptions/books/crime_and_punishment.txt"
pride_and_prejudice_path = "/Users/davidiraheta/Documents/CodingNomads/python-301-main/05_exceptions/books/pride_and_prejudice.txt"

class PrinceException(Exception):
    pass

