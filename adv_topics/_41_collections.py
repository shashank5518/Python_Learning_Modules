# collections: Counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque

a = "aaaaaaabbbcccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.keys())
print(my_counter.values())
print(my_counter.items())
print(my_counter.most_common(1)[0])
print(my_counter.most_common(2)[1][0])
print(my_counter.most_common(3)[2][1])
print(list(my_counter.elements()))

Point = namedtuple("Point", "x, y")
pt = Point(1, -4)
print(pt)
print(pt.x)
print(pt.y)

ordered_dict = OrderedDict()
ordered_dict["b"] = 2
ordered_dict["c"] = 3
ordered_dict["d"] = 4
ordered_dict["a"] = 1
print(ordered_dict)

default_dict = defaultdict(list)
default_dict["a"] = 1
default_dict["b"] = 2
print(default_dict["c"])

deq = deque()
deq.append(1)
deq.append(2)
print(deq)
deq.appendleft(0)
deq.appendleft(-1)
print(deq)
deq.pop()
print(deq)
deq.popleft()
print(deq)
deq.extend([2, 3, 4, 5])
print(deq)
deq.extendleft([-1, -2, -3, -4, -5])
print(deq)
deq.rotate(1)
print(deq)
deq.rotate(2)
print(deq)
deq.rotate(-2)
print(deq)
deq.rotate(-1)
print(deq)
