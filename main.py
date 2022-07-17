class Car:
    def __init__(self, length, width, height, wheel, year, mileage, power, cylinder):
        self.length = length
        self.width = width
        self.height = height
        self.wheel = wheel
        self.year = year
        self.mileage = mileage
        self.power = power
        self.cylinder = cylinder

    def consumption(self, mileage):
        return self.mileage // 100

    def engine(self):
        return self.power * self.cylinder


class Owner:
    def __init__(self, name, age, birthday, number):
        self.name = name
        self.age = age
        self.birthday = birthday
        self.number = number


class Track(Car):
    def __init__(self, length, width, height, wheel, year, mileage, power, cylinder):
        super().__init__(wheel)

    def wheelCheck(self, wheel):
        if self.wheel == 0:
            raise Exception('A car cannot have 0 wheels!')

    def trailer(self, wheel):
        #The tractor itself has 4 wheels (Сам тягач имеет 4 колеса)
        return self.wheel - 4

    def consumptionTrack(self, wheel):
        return self.wheel * 0,34 * 100


class PassengerCar(Car):
    def __init__(self, length, width, height, wheel, year, mileage):
        super().__init__(wheel)

    def wheelCheckPass(self, wheel):
        if self.wheel == 0:
            raise Exception('A car cannot have 0 wheels!')

    def consumptionPass(self, wheel):
        return self.wheel * 0,34 * 100
