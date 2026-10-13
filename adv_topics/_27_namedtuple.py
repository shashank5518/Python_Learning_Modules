from collections import namedtuple

# color = (55, 155, 255) # regular tuple
# print(color[0])

named_color = namedtuple("named_color", ["red", "green", "blue"])
color = named_color(red=55, green=155, blue=255)

print(color.red)
print(color.blue)

# easier to write than dictionary and immutable
