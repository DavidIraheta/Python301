# Write a decorator that literally decorates text output.
# Make it so the symbol it uses can be an argument to the decorator
#
# The output of a function that returns `"Hello"` that has been
# decorated like with `@decorate("*")` should look like this:
#
# ******************************
# Hello
# ******************************

def decorate(symbol):
    """A decorator that literally decorates text output."""
    def decorator(func):
        def wrapper(text):
            length = len(text) + 4
            decoration = symbol * length
            return f"{decoration}\n{symbol} {text} {symbol}\n{decoration}"
        return wrapper
    return decorator

@decorate("*")
def say_something(text):
    return text
print(say_something("Hello"))  # OUTPUT: ******************************\n* Hello *\n******************************
