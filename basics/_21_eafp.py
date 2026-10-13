# EAFP - Easier to Ask Forgiveness than Permission
# Duck Typing


class Duck:
    def quack(self):
        print("Quack, Quack MF!!")

    def fly(self):
        print("Flap, Flap NIGGA!!")


class Person:
    def quack(self):
        print("I am a duck nigga, quack quack!")

    def fly(self):
        print("I can fly cuz, flap flap mf!")


def quack_and_fly(thing):
    # if isinstance(thing, Duck):

    # thing.quack()
    # thing.fly()

    # LBYL - Look Before You Leap (Non-Pythonic)
    # if hasattr(thing, 'quack'):
    #     if callable(thing.quack):
    #         thing.quack()

    # if hasattr(thing, 'fly'):
    #     if callable(thing.fly):
    #         thing.fly()

    # EAFP:
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
        print(e)

    # else:
    #     print('this has to be a duck')

    print()


d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)
