# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной
# первой буквой. Например, print(int_func(‘text’)) -> Text.


def upper_text(some_str):
    return some_str.title()


print(upper_text(input('Введите текст')))