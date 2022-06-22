import time


class TrafficLight:
    """Класс светофор работает в 2х режимах: ручной и автоматический"""

    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 3:
            print(f'Светофор переключается \n '
                  f'{TrafficLight.__color[i]}')
            if i == 0:
                time.sleep(7)
            elif i == 1:
                time.sleep(5)
            elif i == 2:
                time.sleep(3)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()