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

try:
    with open(war_and_peace_path, "r") as file:
        war_and_peace_content = file.read()
        if "Prince" in war_and_peace_content[:100]:
            raise PrinceException("Prince found in War and Peace.")
except FileNotFoundError:
    print(f"Error: {war_and_peace_path} not found.")
try:
    with open(crime_and_punishment_path, "r") as file:
        crime_and_punishment_content = file.read()
        if "Prince" in crime_and_punishment_content[:100]:
            raise PrinceException("Prince found in Crime and Punishment.")
except FileNotFoundError:
    print(f"Error: {war_and_peace_path} not found.")
try:
    with open(pride_and_prejudice_path, "r") as file:
        pride_and_prejudice_content = file.read()
        if "Prince" in pride_and_prejudice_content[:100]:
            raise PrinceException("Prince found in Pride and Prejudice.")
except FileNotFoundError:
    print(f"Error: {war_and_peace_path} not found.")
except PrinceException as e:
    print(e)
