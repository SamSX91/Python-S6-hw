# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

min = int(input('Введите минимум диапазона: '))
max = int(input('Введите максимум диапазона: '))
list_1 = [randint(1, 10) for _ in range(20)]
print(list_1)
list_2 = []
for i in range(len(list_1)):
    if list_1[i] >= min and list_1[i] <= max:
        list_2.append(i)
print(list_2)

