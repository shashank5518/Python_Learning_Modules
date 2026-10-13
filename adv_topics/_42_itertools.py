import itertools

counter = itertools.count()

data = [100, 200, 300, 400]

for index, value in enumerate(data, start=1):
    print(f"{index} - {value}")

daily_data = zip(itertools.count(start=5, step=-5), data)
daily_data_2 = zip(range(10), data)  # zip iterates over smaller iterable by default
daily_data_3 = itertools.zip_longest(range(10), data)

print(list(daily_data))
print(list(daily_data_2))
print(list(daily_data_3))

new_counter = itertools.cycle([1, 2, 3])
new_counter_2 = itertools.cycle(("On", "Off"))

print(next(new_counter))
print(next(new_counter))
print(next(new_counter))
print(next(new_counter))
print(next(new_counter))
print(next(new_counter))
print(next(new_counter))

print(next(new_counter_2))
print(next(new_counter_2))
print(next(new_counter_2))
print(next(new_counter_2))
print(next(new_counter_2))
print(next(new_counter_2))
print(next(new_counter_2))

counter = itertools.repeat(2, times=2)

print(next(counter))
print(next(counter))
# print(next(counter))
# print(next(counter))

squares = map(pow, range(10), itertools.repeat(2))
print(list(squares))

squares = itertools.starmap(pow, [(0, 2), (1, 2), (2, 2)])  # takes a list of tuples
print(list(squares))

letters = ["a", "b", "c", "d"]
numbers = [0, 1, 2, 3]
names = ["Corey", "Nicole"]

result = itertools.combinations(letters, 2)
for item in result:
    print(item)

result = itertools.permutations(letters, 2)
for item in result:
    print(item)

code = itertools.product(numbers, repeat=4)
for item in code:
    print(item)

code = itertools.combinations_with_replacement(numbers, 4)
for item in code:
    print(item)

combined = letters + numbers + names
print(combined)

combined = itertools.chain(letters, numbers, names)
print(type(combined))
for item in combined:
    print(item)

result = itertools.islice(range(10), 1, 5, 2)  # range, start, end (exclusive), step
for item in result:
    print(item)

# itertools.filterfalse, itertools.compress
# itertools.dropwhile, itertools.takewhile
# itertools.accumulate( , operator.mul/div)
# itertools.groupby(), itertools.tee
