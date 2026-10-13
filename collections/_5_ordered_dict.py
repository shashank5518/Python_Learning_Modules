from collections import OrderedDict

ordered_dict: OrderedDict = OrderedDict()

print(ordered_dict)
print(issubclass(OrderedDict, dict))

ordered_dict['one'] = 1
ordered_dict['two'] = 2
ordered_dict['three'] = 3

print(ordered_dict)

ordered_dict.move_to_end('one')
print(ordered_dict)

ordered_dict.move_to_end('one', last=False)
print(ordered_dict)

ordered_dict.pop('two')
print(ordered_dict)

# on comparison ordered_dict compares order and membership
# dict comparison compares just the membership