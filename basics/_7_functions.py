def my_func():
    return "hello function"


def param_func(greeting="Hello", name="You!"):
    return f"{greeting} {name} *greets in binary*"


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


print(my_func)
print(my_func())
print(my_func().upper())

print(param_func("hello", "user"))
print(param_func())

student_info("Math", "Art", name="John", age=22)

courses = ["Math", "Art"]
info = {"name": "Johny", "age": 23}

student_info(courses, info)
student_info(*courses, **info)  # '*' and '**' unpacks values
