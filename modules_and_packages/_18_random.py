import random

print(random.random())  # between 0 and 1

print(random.uniform(1, 10))

print(random.randint(1, 100))

greetings = ["hi", "hello", "hey", "hola"]
print(f"{random.choice(greetings)} Shashank!")

colors = ["red", "black", "green"]
print(random.choices(colors, weights=[18, 18, 2], k=10))

deck = list(range(1, 53))
print(deck)
random.shuffle(deck)
print(deck)

hand = random.sample(deck, k=5)
print(hand)
