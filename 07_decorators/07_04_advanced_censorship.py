# Build on top of the censorship exercise and change your decorator function
# so that you can pass the words it should censor when decorating a function, e.g.:
# `@censor("shoot", "crab")` would censor the words "shoot" and "crab".

def censor_func(*words):
    """A decorator that censors potentially offensive words."""
    def decorator(function):
        def wrapper(text):
            for word in words:
                text = text.replace(word, word[0] + "*" * (len(word)-1))
            return function(text)
        return wrapper
    return decorator

@censor_func ("Shoot", "Crab", "shhot", "crab")
def say_something(text):
    return text

print(say_something("I bumped my toe! Shoot!")) 
print(say_something("Crab!, my funnybone ahh shoot!"))
print(say_something("Crab!, you just hit my car!"))






# def decorator_func(initial_func):
#     def wrapper_func():
#         print("wrapper function picked some...")
#         return initial_func()
#     return wrapper_func

# @decorator_func
# def prettify():
#     print("flowers for you")

# @decorator_func
# def feed():
#     print("apples and potatoes")

# prettify()
# feed()

# def outer_func():
#     msg = "Weeeeeekend!"
#     def inner_func():
#         print(msg)
#     return inner_func
# outer_func()
# say_wee = outer_func()

# say_wee()  # OUTPUT: Weeeeeekend!

# def outer_func(msg):
#     def inner_func():
#         print(msg)
#     return inner_func

# say_wee = outer_func("weee")
# say_wee()  # OUTPUT: weee


# name = "Mycroft"

# def print_name_box():
#     print(name)

#     def smaller_box():
#         # (Re)assigning a variable within a local scope
#         # overwrites the same variable from an outer scope
#         # You also can't use the global variable *before*
#         # assigning it, if you assign it anywhere in that scope.

#         # --TASK--: uncomment the print() function below
#         #     and interpret the results when running the script

#         # print(name)
#         name = "Sherlock"

#         def smallest_box():
#             # Inner scopes always draw from the next outer layer.
#             # After `name` got overwritten, the name that will
#             # be printed is NOT the global-scope name anymore
#             print(name)

#         smallest_box()

#     smaller_box()

# print_name_box()
