# first class functions - functions can be assigned to variables
# can be passed as arguments to other functions
# and can return functions

# def outer_func():
#     message = "hi"
#     def inner_func():
#         print(message) # free variable
#     # return inner_func()
#     return inner_func

# my_func = outer_func()
# print(my_func)
# print(my_func.__name__)
# my_func()

# closure means an inner function remembers the local variables even after the outer function has finished executing


def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func


hi_func = outer_func("hi")
hello_func = outer_func("hello")

hi_func()
hello_func()
print(hi_func)
print(hello_func)
