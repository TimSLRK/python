class Road:
    """
    Класс 'Road': экземпляр при создании принимает параметры (width, length, weight, depth). С помощью метода
    'make_calc_mas' расчитывается масса асфальта, необходимая для покрытия всей дороги.
    """

    def __init__(self, width, length, weight, depth):
        print('___Экземпляр класса "Road" создан___')
        self._width = width
        self._length = length
        self._weight = weight
        self._depth = depth

    def make_calc_mas(self):
        mass = self._width * self._length * self._weight * self._depth
        print(f'Масса асфальта, необходимая для покрытия всей дороги равна {mass // 1000} т.')

main_road = Road(20, 5000, 25, 5)
main_road.make_calc_mas()


