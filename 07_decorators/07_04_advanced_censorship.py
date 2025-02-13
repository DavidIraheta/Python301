# Build on top of the censorship exercise and change your decorator function
# so that you can pass the words it should censor when decorating a function, e.g.:
# `@censor("shoot", "crab")` would censor the words "shoot" and "crab".

def outer_func():
    msg = "Weeeeeekend!"
    def inner_func():
        print(msg)
    return inner_func
outer_func()
say_wee = outer_func()

say_wee()  # OUTPUT: Weeeeeekend!
