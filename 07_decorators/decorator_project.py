#Write a decorator function that wraps text passed to it in a specified HTML tag. 
# The user should be able to decide which tag to use.
#You should be able to pass any HTML tag name to your decorator, irrespective of how many arguments the function that you're wrapping takes. 
# The wrapped function should output their returned string wrapped in the relevant HTML tag:


def html_tag(tag):
    """A decorator that wraps text in a specific HTML tag."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            return f"<{tag}>{func(*args, **kwargs)}</{tag}>"
        return wrapper
    return decorator

@html_tag("h2")

def say_something(text):
    return text

print(say_something("Making it happen!")) 

@html_tag("p")

def introduce(name, age):
    return f" Hello, my name is {name} and I am {age} years old."

print(introduce("David", 35))

