def add(*args):
    sum = 0
    for item in args:
        sum += item
    return sum



print(add(3,5,6))

def calculate(n, **kwargs):
    # print(kwargs)
    # for key,value in kwargs.items():
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add= 3, multiply = 5)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")
my_car = Car(make = "Nissan", model= "GT-R", colour = "Red", seats = "4")

print(my_car.colour)