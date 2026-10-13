from collections import deque

items_list = [1, 2, 3, 4, 5]

print(items_list)

items_list.insert(0, 0)

print(items_list)

items_deque = deque([1, 2, 3, 4, 5])
print(items_deque)

print(type(items_deque))

items_deque.appendleft(0)
print(items_deque)

items_deque.extend([7, 8, 9, 10])

print(items_deque)

items_deque.extendleft([-1, -2, -3])

print(items_deque)

print(items_deque.pop())
print(items_deque.popleft())

websites = ['google.com', 'askjeeves.com', 'weather.com']
last_visited = deque(websites, maxlen=3)
print(last_visited)

last_visited.appendleft('datagy.io')
print(last_visited)

values = deque([1, 2, 3, 4, 5, 6, 7])
print(values[0])

# no slicing allowed
# deque looping is faster than list looping

more_values = deque([1, 2, 3, 4, 5])
more_values.rotate()

print(more_values)

more_values.rotate(3)
print(more_values)

more_values.rotate(-1)
print(more_values)

deque_1 = deque([1, 2, 3])
deque_2 = deque([4, 5, 6])

print(deque_1 + deque_2)

print(deque_1 * 2)

deque_1.reverse()
print(deque_1)

print(deque_1.count(1))