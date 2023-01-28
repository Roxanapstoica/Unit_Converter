def add(*nr):
    sum = 0
    for i in nr:
        sum += i
    return sum


def calculate(n, **kwargs):
    print(kwargs)
    # for (key, val) in kwargs.items():
    #     print(key)
    #     print(val)
    # print(kwargs["add"])
    n += kwargs["add"]
    print(n)
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


# print(add(1, 2, 3, 10))

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
print(my_car.make)
print(my_car.color)
print(my_car.seats)