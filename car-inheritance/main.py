import json
import os
from abc import ABC, abstractmethod
from typing import Tuple


class BaseCar(ABC):
    def __init__(self, length: int, width: int, height: int, wheel: int, year: int,
                 mileage: float, power: float, amount_of_cylindres: int, car_engine: int = 0):
        self.length = length
        self.width = width
        self.height = height
        self.wheel = wheel
        self.year = year
        self.mileage = mileage
        self.power = power
        self.cylinder = amount_of_cylindres
        self.car_engine = car_engine

    def consumption(self) -> float:
        return self.mileage * self.engine() // 100

    @abstractmethod
    def engine(self) -> float:
        pass


class Owner:
    def __init__(self, name, age, birthday, number):
        self.name = name
        self.age = age
        self.birthday = birthday
        self.number = number


class TrackCar(BaseCar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wheelCheck = wheel_check_instance.wheel_check_method()

    def trailer(self, wheel):
        # The tractor itself has 4 wheels (Сам тягач имеет 4 колеса)
        return self.wheel - 4

    def engine(self) -> float:
        self.carEngine = self.power // self.cylinder
        return self.carEngine


my_car = TrackCar(1, 2, 3, 8, 2006, 6000, 900, 200)
print(my_car.consumption())
jsonCar = json.dumps(my_car.__dict__)
print(jsonCar)

track_car = TrackCar(1, 2, 3, 8, 2006, 6000, 900, 200)

track_car.carEngine()

track_car.updateEngine()


class PassengerCar(BaseCar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.carEngine = my_car.engine()
        self.wheelCheck = wheel_check_instance.wheel_check_method()

    def wheel_check_pass(self):
        if self.wheel == 0:
            raise Exception('A car cannot have 0 wheels!')

    @abstractmethod
    def consumption_pass(self) -> tuple[int, int]:
        return self.wheel * 0, 34 * 100

    @abstractmethod
    def update_pass_engine(self) -> float:
        self.carEngine = self.power // 100 * self.cylinder
        return self.carEngine


my_passcar = PassengerCar(3, 2, 1, 8, 1999, 2000, 900, 200)
print(my_passcar.consumptionPass(8))
jsonPassCar = json.dumps(my_passcar.__dict__)
print(jsonPassCar)

# environment variables
print("The keys and values of all environment variables:")
for key in os.environ:
    print(key, "=>", os.environ[key])

print("The value of HOME is: ", os.environ["HOME"])

print("Some changes")


class wheel_check(ABC):
    def __init__(self):
        pass

    def wheel_check_method(self):
        if self.wheel == 0:
            raise Exception('A car cannot have 0 wheels!')


wheel_check_instance = wheel_check()
