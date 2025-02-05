# In this exercise, you will practice both File I/O as well as using Exceptions
# in a real-world scenario.
#
# This folder contains another folder called `books/` that contains three text files
# of books from Project Gutenberg:
# 1. war_and_peace.txt
# 2. pride_and_prejudice.txt
# 3. crime_and_punishment.txt
#
# 1) Open `war_and_peace.txt`, read the whole file content and store it in a variable
# 2) Open `crime_and_punishment.txt` and overwrite the whole content with an empty string
# 3) Loop over all three files and print out only the first character each. Your program
#    should NEVER terminate with a Traceback.
#     a) Which exception can you expect to encounter? Why?
#     b) How do you catch it to avoid the program from terminating with a traceback?

# Define the file paths

from pathlib import Path
war_and_peace_path = "/Users/davidiraheta/Documents/CodingNomads/python-301-main/05_exceptions/books/war_and_peace.txt"
crime_and_punishment_path = "/Users/davidiraheta/Documents/CodingNomads/python-301-main/05_exceptions/books/crime_and_punishment.txt"

# Read the contents of "war_and_peace.txt"
try:
    with open(war_and_peace_path, "r") as file:
        war_and_peace_content = file.read()
except FileNotFoundError:
    print(f"Error: {war_and_peace_path} not found.")

# Overwrite "crime_and_punishment.txt" with an empty string
try:
    with open(crime_and_punishment_path, "w") as file:
        file.write("")
except FileNotFoundError:
    print(f"Error: {crime_and_punishment_path} not found.")



# from os import path
# from books import war_and_peace
# from books import crime_and_punishment

# with open('books/war_and_peace.txt') as file:
#     war_and_peace = file.read()
#     quit()

# try:
#     with open('books/crime_and_punishment.txt', 'w') as file:
#         file.write('')
# except FileNotFoundError:
#     print("File not found.")
#     quit()

# books = ['war_and_peace.txt', 'pride_and_prejudice.txt', 'crime_and_punishment.txt']

# for book in books:
#     try:
#         with open(f'books/{book}') as file:
#             print(file.read(1))
#     except UnicodeDecodeError:
#         print("UnicodeDecodeError")
#     except FileNotFoundError:
#         print("File not found.")
#     except PermissionError:
#         print("PermissionError")
#     except IsADirectoryError:
#         print("IsADirectoryError")
#     except OSError:
#         print("OSError")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     except:
#         print("An unknown error occurred.")
#     finally:
#         print("This is the end of the loop.")
#     print()
