"""
LEGB - Local, Enclosing, Global, Built-In
"""

x = "global x"


def test():
    # global x      # not appreciated
    y = "local y"
    x = "local x"
    print(y)
    print(x)


def test_param(z):
    print(z)


test()
print(x)

test_param("local z")

import builtins

print(dir(builtins))

m = min([5, 4, 3, 2, 1, 8])
print(m)


def outer():
    x = "outer x"

    def inner():
        # nonlocal x
        x = "inner x"
        print(x)

    inner()
    print(x)


outer()
