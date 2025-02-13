# Create a decorator that censors potentially offensive words from a text.
# For example, assuming that "shoot" was considered an offensive word:
# A function that would normall return this text:
#    "I bumped my toe! Shoot!"
# Would, after decorating it with `@censor()`, return:
#    "I bumped my toe! S****!"

def censor(func):
    """A decorator that censors potentially offensive words."""
    def wrapper(text):
        return text.replace("Shoot", "S****")
    return wrapper

@censor

def say_something(text):
    return text

print(say_something("I bumped my toe! Shoot!"))  # OUTPUT: I bumped my toe! S****!

