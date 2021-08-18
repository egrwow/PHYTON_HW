class Road:
    def __init__(self, length, width):
        self._lenght = length
        self._width = width

    def get_mass(self, weigth=35, thickness=7):
        return f"{self._lenght} метров в длинну *" \
               f" {self._width} метров в ширину * " \
               f"{weigth} вес в кг * " \
               f"{thickness} толщина в сантиметрах =" \
        f" {(self._lenght * self._width * weigth * thickness) / 1000} тонн"

road_1 = Road(10000, 50)
print(road_1.get_mass())