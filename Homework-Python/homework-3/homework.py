# Задание 1
# Установить PostgreSQL

# Задание 2
# Установить Vbox

# Задание 3
# Скачать ubuntu x64

# Задание 4
# Напишите функцию, которая отображает на экран
# форматированный текст, указанный ниже:
# “Don't compare yourself with anyone in this world…
# if you do so, you are insulting yourself.”
# Bill Gates

# def any():
#     print(f"“Don't compare yourself with anyone in this world…\nif you do so, you are insulting yourself.”\nBill Gates")


# Задание 5
# Напишите функцию, которая принимает два числа
# в качестве параметра и отображает все четные числа
# между ними.

# def any2(a, b):
#     if a == b:
#         return "Диапазон введен неверно."
#     if a > b:
#         a, b = b, a
#     for i in range(a, b + 1):
#         if i % 2 == 0:
#             print(int(i), end=' ')
 
 
# print('Четные:\n')
# any2(1, 100)


# Задание 6
# Напишите функцию, которая отображает пустой или
# заполненный квадрат из некоторого символа. Функция
# принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа:
# ■ если она равна True, квадрат заполненный
# ■ если False, квадрат пустой.

# def any3(n, s, f):
#     r = s*n
#     if not f:
#         m = s+" "*(n-2)+s
#     else:
#         m = r
#     print(r)
#     for i in range(n-2):
#         print(m)
#     print(r)


# any3(5, "#", True)
# print("")
# any3(5, "*", False)


# Задание 7
# Напишите функцию, которая возвращает минимальное
# из пяти чисел. Числа передаются в качестве параметров.

# def any4(*x1):
#     return min(x1)


# Задание 8
# Напишите функцию, которая возвращает произведение чисел в указанном диапазоне. Границы диапазона
# передаются в качестве параметров. Если границы диапазона перепутаны(например, 5 — верхняя граница, 25 —
# нижняя граница), их нужно поменять местами.

# def any5(a, b):
#     if a == b:
#         return "Диапазон введен неверно."
#     if a > b:
#         a, b = b, a
#     res = 1
#     for i in range(a, b + 1):
#         res *= i
#     return res
 
 
# print(any5(int(input("Введите a: ")), int(input("Введите b: "))))

# Задание 9
# Напишите функцию, которая считает количество
# цифр в числе. Число передаётся в качестве параметра. Из
# функции нужно вернуть полученное количество цифр.
# Например, если передали 3456, количество цифр будет 4.



# Задание 10
# Напишите функцию, которая проверяет является ли
# число палиндромом. Число передаётся в качестве параметра. Если число палиндром нужно вернуть из функции
# true, иначе false.
# «Палиндром» — это число, у которого первая часть
# цифр равна второй перевернутой части цифр. Например,
# 123321 — палиндром(первая часть 123, вторая 321, которая
#                    после переворота становится 123), 546645 — палиндром,
# а 421987 — не палиндром.
