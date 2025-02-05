# Write a script that demonstrates a try/except/else statement.
# For example, you can revisit the course module about database interactions
# and include a try/except/else statement based on what to do whether or not
# the database connection can be established.

import sqlite3

try:
    connection = sqlite3.connect("example.db")
except sqlite3.Error as e:
    print(f"Whoops...an error occured: {e}")
else:
    print("Sucsessfully connected to the database.")
    connection.close()

