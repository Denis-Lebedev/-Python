# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут
# реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
# — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep


class TrafickLigther:
    def __init__(self, color):
        self.color = color
        self.trafic_color = ['Green', 'Yellow', 'Red']

    def start(self):
        while True:
            if self.color == self.trafic_color[0]:
                print(self.trafic_color[0])
                sleep(10)
                print(self.trafic_color[1])
                sleep(2)
                print(self.trafic_color[2])
                sleep(7)
            elif self.color == self.trafic_color[1]:
                print(self.trafic_color[1])
                sleep(2)
                print(self.trafic_color[2])
                sleep(7)
                print(self.trafic_color[0])
                sleep(10)
            elif self.color == self.trafic_color[2]:
                print(self.trafic_color[2])
                sleep(7)
                print(self.trafic_color[0])
                sleep(10)
                print(self.trafic_color[1])
                sleep(2)
            else:
                print('Неверный цвет')


my_tr_L = TrafickLigther(color='Yellow')
my_tr_L.start()
