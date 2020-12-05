# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль.


def my_funck(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Деление на 0"
    except TypeError:
        return 'Неверный формат'


result = my_funck(4, '2')
print(result)