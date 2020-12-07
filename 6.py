#  Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.

from itertools import cycle, count

val_1 = int(input('введите первое число'))
for el in count(val_1, 1):
    if el > val_1+10:
        break
    print(el)


test_list = ['Зелёный', 15, 1.45, True]
tries = int(input('Сколько раз повторить список'))
n = 0
for el in cycle(test_list):
    if n >= tries*len(test_list):
        break
    else:
        print(el)
        n += 1


