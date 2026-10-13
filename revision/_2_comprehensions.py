nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list = [n for n in nums]
print(my_list)

my_list_sq = [n*n for n in nums]
print(my_list_sq)

my_list_mpp_lambda = map(lambda n: n*n, nums)
print(my_list_mpp_lambda)
print(list(my_list_mpp_lambda))

my_list_filter_lambda = filter(lambda n: n%2 == 0, nums)
print(my_list_filter_lambda)
print(list(my_list_filter_lambda))

my_list_comp = [n for n in nums if n%2 == 0]
print(my_list_comp)

my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)

names = ['bruce', 'clark', 'barry', 'tony', 'peter']
heroes = ['batman', 'superman', 'flash', 'iron man', 'spider man']

my_dict = {name: hero for name, hero in zip(names, heroes)}
print(my_dict)

my_dict_filter = {name: hero for name, hero in zip(names, heroes) if name != 'peter'}
print(my_dict_filter)

nums = [1, 1, 2, 2, 3, 4, 4, 4, 4, 5, 6, 5, 7, 8, 8, 9, 9, 10]

my_set = {n for n in nums}
print(my_set)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_gen = (n*n for n in nums)
for i in my_gen:
    print(i)
