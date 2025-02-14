# Create a custom decorator function that records the execution time of
# the decorated function and prints the time to your console when the function
# has finished execution.

import time
import random 
import timeit 

def time_it(func):
    """A decorator that times the execution of a function."""
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        end_time = timeit.default_timer()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper

@time_it
def random_sleep():
    """A function that demonstrates sleeps for a random amount of time."""
    time.sleep(random.randint(1, 5))
    return "Finished sleeping!"

print(random_sleep())
