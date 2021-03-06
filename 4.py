# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Начало двитжения')

    def stop(self):
        print('Конец движения')

    def turn(self, direction):
        self.direction = direction
        print(f'Поворот {self.direction}')

    def show_speed(self):
        print(f'скорость = {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'скорость = {self.speed} сбавьте скоростьдо 60')
        else:
            print(f'скорость = {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'скорость = {self.speed} сбавьте скоростьдо 40')
        else:
            print(f'скорость = {self.speed}')


class PoliceCar(Car):
    pass


car1 = TownCar(name='Opel', speed=120, color='Синий')
car1.go()
car1.turn('Налево')
car1.stop()
car1.show_speed()
car2 = PoliceCar(name='Полицейская машина', speed=90, is_police=True, color='Полициеская раскраска')
car2.show_speed()
