# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while
#     и арифметические операции.

user_val = int(input('Введите число : '))

user_val = str(user_val)
len_val = 0
max_val = user_val[0]
while len_val < len(user_val):
    if max_val < user_val[len_val]:
        max_val = user_val[len_val]
    else:
        pass
    len_val +=1

print(f'Наибольшее число в {user_val}, это {max_val}')