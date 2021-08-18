class Stationery:
    def __init__(self, title="Draw here"):
        self.title = title

    def draw(self):
        print(f"start drawing {self.title}))")
class Pen(Stationery):
    def draw(self):
        print(f'start drawing {self.title} pen')
class Pencil(Stationery):
    def draw(self):
        print(f'start drawing {self.title} pencil')
class Marker(Stationery):
    def draw(self):
        print(f'start drawing {self.title} marker')

stat = Stationery()
stat.draw()
pen = Pen("черная гелевая ручка")
pen.draw()
pencil = Pencil('простой карандаш')
pencil.draw()
marker = Marker('красный маркер')
