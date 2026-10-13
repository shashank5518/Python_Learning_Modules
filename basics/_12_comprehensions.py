nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list = [n for n in nums]
print(my_list)

my_list_squared = [n**2 for n in nums]
print(my_list_squared)

my_list_map = map(lambda n: n * n, nums)
print(list(my_list_map))

my_list_even = [n for n in nums if n % 2 == 0]
print(my_list_even)

my_list_filter = filter(lambda n: n % 2 == 0, nums)
print(list(my_list_filter))

my_list_alphanum = [(letter, num) for letter in "abcd" for num in range(5 + 1)]
print(my_list_alphanum)

names = ["bruce", "peter", "clark", "logan", "wade"]
heroes = ["batman", "spiderman", "superman", "wolverine", "deadpool"]

# hero_dict = zip(names, heroes)
# print(dict(hero_dict))

hero_dict = {}
for name, hero in zip(names, heroes):
    hero_dict[name] = hero
print(hero_dict)

hero_dict_2 = {name: hero for name, hero in zip(names, heroes)}
print(hero_dict_2)
hero_dict_no_peter = {
    name: hero for name, hero in zip(names, heroes) if name != "peter"
}
print(hero_dict_no_peter)

nums = [1, 2, 3, 2, 3, 1, 4, 6, 5, 4, 5, 6]

my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)

my_set_comprehension = {n for n in nums if n != 4}
print(my_set_comprehension)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def gen_func(nums):
    for n in nums:
        yield n * n


my_gen = gen_func(nums)
for i in my_gen:
    print(i)

my_Gen = (n * n for n in nums)

for i in my_Gen:
    print(i)
