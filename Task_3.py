class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.posotion = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_worker_name(self):
        return f"{self.name} {self.surname}"

    def get_worker_profit(self):
        return f"{sum(self._income.values())}"

footballplayer = Position("Egor", "Kalinin", "Forward", 1000000, 750000)
print(footballplayer.get_worker_name())
print(footballplayer.posotion)
print(footballplayer.get_worker_profit())