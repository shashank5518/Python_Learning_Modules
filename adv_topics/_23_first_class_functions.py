# when a function is treated as first-class citizen
# first-class citizen -> entity which supports all the operations generally available to other entities, these operations typically include being passed as an argument, returned from a function and assigned to a variable


def square(x):
    return x * x


# f = square(5)
f = square
print(f)
print(f(5))


def cube(x):
    return x**3


def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


squares = my_map(square, [1, 2, 3, 4, 5])
cubes = my_map(cube, [1, 2, 3, 4, 5])
print(squares)
print(cubes)


def logger(msg):
    def log_message():
        print("Log: ", msg)

    return log_message


log_hi = logger("Hi!")
log_hi()
