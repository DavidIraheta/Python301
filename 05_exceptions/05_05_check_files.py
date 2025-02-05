# Read in the first number from `integers.txt`
# and perform a calculation with it.
# Make sure to catch at least two possible Exceptions (`IOError` and `ValueError`)
# with specific `except` statements, and continue to do the calculation
# only if neither of them applies.

file_name = 'integers.txt'

try:
    dividend = int(input("Please enter the number to be divided: "))
    divisor = int(input("Please enter the divisor: "))
    result = dividend / divisor
    print(f"The result of {dividend} divided by {divisor} is {result}")
except ZeroDivisionError:
    print("My most sincere apologies, but you can't divide by zero.")
except ValueError:
    print("I am once again asking you to use only digits in your input.")
except:
    print("Please remain calm...")
