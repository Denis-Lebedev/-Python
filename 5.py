# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя
# необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

raiting = [7, 4, 1]
user_vall = int(input('ВВедите число'))
for num in raiting:
    if user_vall > num:
        raiting.insert(raiting.index(num), user_vall)
        break
    elif user_vall == num:
        raiting.insert(raiting.index(num)+1, user_vall)
        break
    else:
        raiting.append(user_vall)
print(raiting)
