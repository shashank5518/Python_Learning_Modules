# def square_nums(nums):
#     result = []
#     for i in nums:
#         result.append(i*i)
#     return result


def square_nums(nums):
    for i in nums:
        yield (i * i)


my_nums = square_nums([1, 2, 3, 4, 5, 6, 7, 8])
print(my_nums)

# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums)) # may throw StopIteration error if iterator is exhausted
# print(list(my_nums))

for num in my_nums:
    print(num)

my_nums_comprehension = [num * num for num in [1, 2, 3, 4, 5]]
print(my_nums_comprehension)
for num in my_nums_comprehension:
    print(num)

my_nums_generator = (x * x for x in [1, 2, 3, 4, 5])
print(my_nums_generator)
for num in my_nums_generator:
    print(num)

# generators are used for memory efficiency and lazy evaluation
# generators remember the function state execution after each call
# yield pauses execution of a function while preserving the entire execution state
