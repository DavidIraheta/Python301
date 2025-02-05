# Create a script that asks a user to input an integer, checks for the
# validity of the input type, and displays a message depending on whether
# the input was an integer or not.
# The script should keep prompting the user until they enter an integer.

while True:
    try:
        user_input = input("Please enter an interger: ")
        if user_input.isnumeric():
            print("Thanks for listening properly.")
            break
        else:
            raise ValueError
    except ValueError:
        print("You did not enter an integer. Please try entering an interger.")
        continue
    except KeyboardInterrupt:
        print(f"\nYou pressed Ctrl+C. Thats not an integer")
        break
    except EOFError:
        print(f"\nYou pressed Ctrl+D. That is not an integer.")
        break
    except Exception as e:
        
        print(f"An error occurred: {e}")
        break
    finally:
        print("This is the end of the loop.")
        break
# The script should keep prompting the user until they enter an integer.