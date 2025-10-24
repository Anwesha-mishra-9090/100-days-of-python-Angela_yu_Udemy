def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum
print(add(3 , 5 , 7 , 8 , 9 , 7 , 5 , 7 , 6 ))

def calculate(n,**kwargs):
    # print(kwargs)
    # for key , value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2,add=3 , multiply=5)


class Car:

    def __init__(self , **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car = Car(make="Nission",model="GT-R")
print(my_car.model , my_car.make)