# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов

def my_funck(vall_1, vall_2, vall_3):
    sample_list = [vall_1,vall_2,vall_3]
    new_list = []
    while len(sample_list) > 1:
        max_vall = max(sample_list)
        sample_list.remove(max_vall)
        new_list.append(max_vall)
    return sum(new_list)


print(my_funck(5,4,8))
