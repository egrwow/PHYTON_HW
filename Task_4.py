class Car:  #автомобиль
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'Автомобиль: {self.name} (цвет машины {self.color})'
              f'полицейское авто - {self.is_police}')
    def go(self):
        print(f'{self.name}: Машина поехала!')

    def stop(self):
        print(f'{self.name}: Машина остановилась!')

    def turn(self, direction):
        print(f'{self.name}: Поворот {"направо" if direction == 0 else "налево"}.')

    def show_speed(self):
        return f'{self.name}: Скорость: {self.speed}.'

class TownCar(Car):                     #повседневное авто

    def show_speed(self):
        return f'{self.name}: Скорость авто: {self.speed}. ' \
               f'превышение скорости!' \
            if self.speed > 60 else f'{self.name}: Скорость авто {self.speed}'

class WorkCar(Car):                    #рабочее авто

    def show_speed(self):
        return f'{self.name}: Скорость авто: {self.speed}. ' \
               f'превышение скорости!' \
            if self.speed > 40 else f'{self.name}: Скорость авто {self.speed}'

class SportCar(Car):
    """Спортивный авто"""

class PoliceCar(Car):
    """Полицейская машина"""
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)

police_car = PoliceCar('"МВД"', "синий", 100)
police_car.go()
print(police_car.show_speed())
police_car.turn(0)
police_car.stop()
print()

work_car = WorkCar('"Taxovichkoff"', "желтый", 40)
work_car.go()
print(work_car.show_speed())
work_car.turn(0)
work_car.stop()
print()

sport_car = SportCar('"Honda Accord VI coupe"', "фиолетовый", 200)
sport_car.go()
print(sport_car.show_speed())
sport_car.turn(0)
sport_car.stop()
print()

town_car = TownCar('"Range Rover"','черный', 70)
town_car.go()
print(town_car.show_speed())
town_car.turn(1)
town_car.stop()
print()