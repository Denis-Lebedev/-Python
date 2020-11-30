# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369

user_val = int(input('Введите число '))

print(user_val + int(str(user_val) * 2) + int(str(user_val) * 3))
