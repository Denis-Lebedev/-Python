# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки
# необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

user_data = input('Введите несколько слов')
user_data = user_data.split(sep=' ')
for num , word in enumerate(user_data):
    if len(word) <=10:
        print(num, word)
    else:
        print(num, word[0:10])
