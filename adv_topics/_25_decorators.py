def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"wrapper executed this before {original_function.__name__}")
        return original_function(*args, **kwargs)

    return wrapper_function


class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f"call method executed this before {self.original_function.__name__}")
        return self.original_function(*args, **kwargs)


# @decorator_function
@decorator_class
def display():
    print("display function ran")


# decorated_display = decorator_function(display)
# decorated_display()

print(display)
display()

# @decorator_function
# def display():
#     print('display function ran')

# is same as

# display = decorator_function(display)


# @decorator_function
@decorator_class
def display_info(name, age):
    print(f"display_info ran with arguments {name} and {age}")


display_info("John", 25)

"""
@dec_func_1
@dec_func_2
def func(args, kwargs):
    return something

is same as

func = dec_func_1(dec_func_2(func))
"""

# from functools import wraps
# @wraps over each wrapper function
# stacking @decorator will work perfectly now without wrapper function being passed as an argument
