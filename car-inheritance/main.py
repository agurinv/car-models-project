import json
import os

class Car:
    def __init__(self, length, width, height, wheel, year, mileage, power, cylinder, carEngine = 0):
        self.length = length
        self.width = width
        self.height = height
        self.wheel = wheel
        self.year = year
        self.mileage = mileage
        self.power = power
        self.cylinder = cylinder
        self.carEngine = carEngine

    def consumption(self, mileage):
        return self.mileage // 100

    def engine(self):
        self.carEngine = self.power * self.cylinder
        return self.carEngine


class Owner:
    def __init__(self, name, age, birthday, number):
        self.name = name
        self.age = age
        self.birthday = birthday
        self.number = number


class Track(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def wheelCheck(self, wheel):
        if self.wheel == 0:
            raise Exception('A car cannot have 0 wheels!')

    def trailer(self, wheel):
        #The tractor itself has 4 wheels (Сам тягач имеет 4 колеса)
        return self.wheel - 4

    def consumptionTrack(self, wheel):
        return self.wheel * 0,34 * 100

    def updateEngine(self, carEngine):
        self.carEngine = self.power // self.cylinder
        return self.carEngine

my_car = Car(1, 2, 3, 8, 2006, 6000, 900, 200)
print(my_car.consumption(6000))
jsonCar = json.dumps(my_car.__dict__)
print(jsonCar)

class PassengerCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.carEngine = my_car.engine()

    def wheelCheckPass(self, wheel):
        if self.wheel == 0:
            raise Exception('A car cannot have 0 wheels!')

    def consumptionPass(self, wheel):
        return self.wheel * 0,34 * 100

    def updatePassEngine(self, carEngine):
        self.carEngine = self.power // 100 * self.cylinder
        return self.carEngine


my_passcar = PassengerCar(3, 2, 1, 8, 1999, 2000, 900, 200)
print(my_passcar.consumptionPass(8))
jsonPassCar = json.dumps(my_passcar.__dict__)
print(jsonPassCar)

#environment variables
print("The keys and values of all environment variables:")
for key in os.environ:
    print(key, "=>", os.environ[key])

print("The value of HOME is: ", os.environ["HOME"])



print ("Some changes")