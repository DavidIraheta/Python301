# Write a decorator function that wraps text output into quotes, e.g.:
# Hello world! ----> "Hello World!"
# You can use it to create quotes from text output.

def quote(func):
    """A decorator that wraps text output in quotes."""
    def wrapper(text):
        return f'"{text}"'
    return wrapper

@quote
def say_something(text):
    return text

print(say_something("Hello world!"))  
print(say_something("Python is awesome!")) 