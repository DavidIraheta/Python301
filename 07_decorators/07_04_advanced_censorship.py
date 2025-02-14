# Build on top of the censorship exercise and change your decorator function
# so that you can pass the words it should censor when decorating a function, e.g.:
# `@censor("shoot", "crab")` would censor the words "shoot" and "crab".

def censor_func(*words):
    """A decorator that censors bad words."""
    def decorator(function):
        def wrapper(text):
            for word in words:
                text = text.replace(word, word[0] + "*" * (len(word)-1))
            return function(text)
        return wrapper
    return decorator

@censor_func ("Shoot", "Crab", "shoot", "crab")
def say_something(text):
    return text

print(say_something("I bumped my toe! Shoot!")) 
print(say_something("Crab!, my funnybone ahh shoot!"))
print(say_something("Crab!, you just hit my car!"))





