class Car:
    def __init__(self, length, width, height, wheel, year, mileage):
        self.length = length
        self.width = width
        self.height = height
        self.wheel = wheel
        self.year = year
        self.mileage = mileage

    def consumption(self):
        pass


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
