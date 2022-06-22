
class Worker:
    """Класс 'Worker'"""

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    """Дочерний класс 'Position' наследован от 'Worker'"""

    def __init__(self,  name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'ФИО: {self.surname} {self.name}'

    def get_total_income(self):
        return sum(self._income.values())



me = Position('Oleg', 'Khavroshin', 'DevOps engineer', 3500, 1000)
me2 = Position('Oleg', 'Khavroshin', 'Top DevOps engineer', 35000, 10000)
print(me.get_full_name())
print(f'Total income: {me.get_total_income()}')
print(me._income)
print(me2.get_full_name())
print(f'Total income: {me2.get_total_income()}')
print(me2.position)