class Car:
    def __init__(self, length, width, height, wheel, year, mileage):
        self.length = length
        self.width = width
        self.height = height
        self.wheel = wheel
        self.year = year
        self.mileage = mileage

    def consumption(self, mileage):
        return mileage // 100


class Engine:
    def __init__(self, power, cylinder):
        self.power = power
        self.cylinder = cylinder


class Owner:
    def __init__(self, name, age, birthday, number):
        self.name = name
        self.age = age
        self.birthday = birthday
        self.number = number


class Track(Car):
    def __init__(self, length, width, height, wheel, year, mileage):
        super().__init__(wheel)

    def wheelCheck(self, wheel):
        if self.wheel == 0:
            raise Exception('A car cannot have 0 wheels!')

    def trailer(self):
        pass


class PassengerCar(Car):
    def __init__(self, length, width, height, wheel, year, mileage):
        super().__init__(wheel)

    def wheelCheckPass(self, wheel):
        if self.wheel == 0:
            raise Exception('A car cannot have 0 wheels!')

    def motor(self):
        pass
