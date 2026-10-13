def prefix_decorator(prefix):
    def decorator_function(original_func):
        def wrapper_function(*args, **kwargs):
            print(prefix, "Executed before", original_func.__name__)
            result = original_func(*args, **kwargs)
            print(prefix, "Executed after", original_func.__name__, "\n")
            return result

        return wrapper_function

    return decorator_function


@prefix_decorator("mueheheheh")
def display_info(name, age):
    print(f"display_info ran with arguments {name} and {age}")


display_info("John", 23)
display_info("Doe", 25)
