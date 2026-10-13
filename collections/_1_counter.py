from collections import Counter

counts = Counter()

print(counts)
print(type(counts))

print(issubclass(Counter, dict))

a_string = 'hey there = welcome to this video'

counts_dict: dict[str, int]= {}

for item in a_string:
    if item in counts_dict:
        counts_dict[item] += 1
    else:
        counts_dict[item] = 1

print(counts_dict)

counts = Counter(a_string)
print(counts)

counts_list = Counter([1, 2, 3, 1, 2, 4, 5, 3, 4, 2, 5, 6, 4, 5])
print(counts_list)

animals = ['dogs', 'dogs', 'cats', 'cow', 'cats', 'fish', 'bird', 'dogs', 'bird', 'cow']
animal_counts = Counter(animals)
print(animal_counts)
print(animal_counts.get('bunnies'))

print(animal_counts.most_common()[0])
print(animal_counts.most_common()[0][0])

print(animal_counts.most_common()[-1])
print(animal_counts.most_common()[-1][0])

animal_counts.update(['dogs', 'cats', 'bunny', 'fish'])

print(animal_counts)

del(animal_counts['cats'])
print(animal_counts)

animal_counts_2 = Counter(dogs = 3, cats = 2, fish = 15)
print(animal_counts_2)

animal_counts_total = animal_counts + animal_counts_2
print(animal_counts_total)

print(animal_counts)
print(animal_counts_2)

print(animal_counts & animal_counts_2)

print(animal_counts | animal_counts_2)