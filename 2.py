# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1,
# 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов
# необходимо использовать функцию input().

simple_list = [1, 'a', 12.78, True, False]

countter = 1
while countter < len(simple_list):
    simple_list[countter - 1], simple_list[countter] = simple_list[countter], simple_list[countter - 1]
    countter += 2

print(simple_list)
