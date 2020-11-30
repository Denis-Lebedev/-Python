# *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (
# характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользовател я.

dict_prod = {'name': '', 'firm': ' ', 'price': ' ', 'available': ' '}
production = []
n = 0
while True:
    check = input('ВВедите Q для выхода , что угодно для продолжения').upper()
    if check == 'Q':
        break
    else:
        for key in dict_prod.keys():
            user_data = input(f'ВВедите {key} фирмы')
            user_data = int(user_data) if (key == 'price' or key == 'available') else user_data
            dict_prod[key] = user_data
    n += 1
    production.append((n, dict_prod))
print(production)
