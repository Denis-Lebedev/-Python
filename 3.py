# . Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и
# премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В
# классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (
# get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income['wage'] + income['bonus']


class Position(Worker):
    def get_full_name(self):
        print(f'Имя: {self.name}, Фамилия: {self.surname}')

    def get_total_income(self):
        print(self.position, ':', self._income)


inome = {'wage': 40000, 'bonus': 1200}
positiom1 = Position(name='Имя', surname='Фамилия', position='Должность', income=inome)
positiom1.get_full_name()
positiom1.get_total_income()
