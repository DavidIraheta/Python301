# """Applies a discount to a given price."""


# def apply_discount(price, discount):
#     """
#     Applies a discount to the given price.
    
#     :param price: Original price (float or int)
#     :param discount: Discount percentage (0-100)
#     :return: Discounted price (float)
#     """
#     if not (0 <= discount <= 100):
#         raise ValueError("Discount must be between 0 and 100")
#     return round(price * (1 - discount / 100), 2)

#Write a second function that returns some text and wraps it with the lowercase decorator in the same way that say_something is wrapped in the example code.
# def lowercase(func):
#     """A decorator that avoids digital screaming."""
#     def wrapper(text):
#         initial_result = func(text)
#         new_result = initial_result.lower()
#         return new_result
#     return wrapper

# @lowercase


# def shout_message(text):
#     return f"THIS IS IMPORTANT: {text}"

# print(shout_message("PLEASE LISTEN!"))  # OUTPUT: this is important: please listen!

# def say_something(text):
#     return text

# print(say_something("HEY WHAT'S UP?"))  # OUTPUT: hey what's up?

def say_hi():
    print("Hi.")

say_hi()  # OUTPUT: Hi.

hi = say_hi
hi()  # OUTPUT: Hi.

def say_moo():
    print("moooooooo!")

function_list = [say_hi, say_moo]

print(function_list[0]) 
# OUTPUT: <function say_hi at 0x10659d1e0>;

