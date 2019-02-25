class Duck:
    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, flap!')


class Person:
    def quack(self):
        print("I'm quacking like a duck!")

    def fly(self):
        print("I'm flapping my arms!")


def quack_and_fly(thing):
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
        print(e)
    finally:
        print(thing)


d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)


person = {'name': 'John Doe', 'age': 40, 'job': 'programmer'}

print("I am {name} who is {age} years old and am a {job}".format(**person))
