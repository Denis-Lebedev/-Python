# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

user_time = int(input('Введите время в секундах '))

hour_time = user_time // 3600
minute_time = user_time // 60
secund_time = user_time % 60
print(f'Часы :{hour_time}, Минуты :{minute_time}, Секунды :{secund_time}')