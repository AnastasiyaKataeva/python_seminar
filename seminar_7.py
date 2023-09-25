# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.


first_el= int(input("Введите первый элемент массива: "))
difference = int(input("Введите разность: "))
length = int(input("Введите длину массива: "))

for i in range(length):
 print(first_el + i * difference)


# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
min_el= int(input("Введите минимальное значение диапазона: "))
max_el = int(input("Введите максимальное значение диапазона: "))
length_list = int(input("Введите длину массива: "))

list_1 = [random.randint(-10, 10) for i in range(length_list)]
print(list_1)
list_2 = []


list_3 = [i for i in range(length_list) if list_1[i] >= min_el and list_1[i] <= max_el]
print(list_3)