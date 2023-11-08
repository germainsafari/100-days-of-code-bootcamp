def add(*args):
    total = 0
    for n in args:
        total += n
    return total


# new = add(1, 2, 3, 4, 5)
# print(new)


# def calculate(n, **kw):
#     print(n, kw)
#
#
# calculate(5, add=3, key=4, four=6)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")


my_car = Car(make="BMW")
my_car.model = "couple"
print(my_car.make)

