# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
# ]

# sum = 0

# for i in matrix:
#     for j in i:
#         sum += j

# print(sum)

# for j in range(3):
#     col_sum = 0
#     for i in matrix:
#         col_sum += i[j]
#     print(col_sum)


# Условные конструкции
# 1. Ввести число.
# ○ Если >0 → "Плюс"
# ○ <0 → "Минус"
# ○ =0 → "Ноль"
# 2. Ввести число.
# ○ Если делится на 3 → "Делится на 3"
# ○ На 5 → "Делится на 5"
# ○ На 15 → "Делится на 15"
# ○ Иначе → "Не делится на 3,5 или 15"

# num = input('write ')
# if(num.isdigit):
#     if(num > 0):
#         print('+')
#     elif(num < 0):
#         print('-')
#     else:
#         print('Ноль')
# else:
#     print('num need to be num')

# 3. Ввести числа до 0.
# ○ Вывести сумму всех чисел
# 4. Вывести числа от 1 до 10 через for.
# 5. Вывести числа от 10 до 1 через while.
# 6. Нарисовать пирамидку из звёздочек (5 рядов):

# 3.
# sum = 0
# num = ''
# while(num != '0'):
#     num = input('write ')
#     if(num.isdigit()):
#         sum += int(num)
#     else:
#         print('num need to be num')
# print(sum)

# 4.
# for i in range(1,11):
#     print(i)

# 5.
# num = 1
# while(num < 10):
#     num += 1
#     print(num)


# 6
# for i in range(1,6):
#     for j in range(i):
#         print('*',end='')
#     print()

# 7. Ввести текст.
# ○ Посчитать буквы, цифры, пробелы
# 8. Ввести текст.
# ○ Вывести все символы в верхнем регистре
# 9. Ввести текст.
# ○ Посчитать количество слов

# 7.
# text = input('write ')
# word = 0
# num = 0
# space = 0
# for i in text:
#     if(i.isdigit()):
#         num += 1
#     elif(i.isalpha()):
#         word += 1
#     elif(i.isspace()):
#         space += 1

# print(num)
# print(word)
# print(space)

# 8. Ввести текст.
# ○ Вывести все символы в верхнем регистре
# 9. Ввести текст.
# ○ Посчитать количество слов

# 8.
# text = input('write ')
# if(text.isalpha()):
#     for i in text:
#         print(i.upper())
# else:
#     print('text need to be text')

# 9. сделать через split
# text = input('write ')
# words = text.split()
# print(len(words))

# 10. Создать список [2, 5, 8, 3, 10]
# ○ Вывести чётные числа
# ○ Вывести сумму чисел
# 11. Список строк: ["Python", "C++", "Java"]
# ○ Длина каждой строки
# ○ Все строки заглавные
# 12. Пользователь вводит 5 чисел → список
# ○ Наибольшее число
# ○ Наименьшее число

# 10.
# array = [2, 5, 8, 3, 10]
# sum = 0
# for i in array:
#     sum += i
#     if(i % 2 == 0):
#         print(i)
# print(sum)

# 11.
# array = ["Python", "C++", "Java"]
# for i in array:
#     print(len(i))
# for i in array:
#     print(i.upper())

# 12. 
# array = []
# while(len(array) < 5):
#     array.append(int(input('write ')))

# max = array[0]
# min = array[0]
# for i in array: 
#     if(i > max):
#         max = i
#     if(i < min):
#         min = i

# print(max)
# print(min)

# Матрица 3×3 чисел:
# ○ Сумма всех элементов
# ○ Сумма каждого столбца
# 14. Матрица 3×3:
# ○ Вывести диагональ (слева-верх → справа-низ)
# 15. “Карта уровня” 3×3:
# ○ "#" — стена, "P" — игрок, " " — пустое место
# ○ Вывести матрицу в виде таблицы

# 13.
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
# ]

# sum = 0

# for i in matrix:
#     for j in i:
#         sum += j
# print(sum)

# for j in range(3):
#     cs = 0
#     for i in matrix:
#         cs += i[j]
#     print(cs)

# 14. Матрица 3×3:
# ○ Вывести диагональ (слева-верх → справа-низ)
# 15. “Карта уровня” 3×3:
# ○ "#" — стена, "P" — игрок, " " — пустое место
# ○ Вывести матрицу в виде таблицы

# 14.
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
# ]
# for i in range(0,3):
#     print(matrix[i][i])

# 15.
# matrix = [
#     [' ','#',' '],
#     [' ','#','P'],
#     [' ','#',' '],
# ]
# for i in matrix:
#     for j in i:
#         print(j,end=' ')
#     print()


# def first_function():
#     print('yoyoy')

# first_function()

# def get(name):
#     print('hello', name)

# get('damir')
# get('aisa')

# def user(name,age,is_gay):
#     print('hello',name, 'now u are',age,'are you gay?','yes' if is_gay else 'nuh')

# user('damir',18,False)

# def square(num):
#     return num ** 2
# print(square(5))

# def sum_list(numbers):
#     total = 0
#     for i in numbers:
#         total += i
#     return total
# my_list = [1,2,3,4,5]

# print('sum of list',sum_list(my_list))

# def sum_odd(numbers):
#     sum = 0
#     for i in numbers:
#         if(i % 2 == 0):
#             sum += i
#     return sum

# print(sum_odd(my_list))

# def yo(name = 'ghost'):
#     print(f'hello, {name}')
# yo()
# yo('damir')

# def a(name,age=0):
#     print(f'Hello {name},are you {age} years old?')
# a('damir')
# a('damir',18)

# def min_max(num):
#     return min(num), max(num)

# a,b = min_max([4,3])
# print('Max',a)
# # print('Min',b)

# x = 10

# def test():
#     y = 5
#     print(x+y)

# test()

# def x(y):
#     return y*y

# f = lambda x:x*x

# print(f(6))

# f = lambda x:x+10

# print(f(5))

# f = lambda x,y:x*y

# print(f(2,4))

# def word_counter(text):
#     counter = 0
#     for i in text:
#         if(i.isalpha()):
#             counter += 1
#         else:
#             print('text need to be text')
#     return counter

# print(word_counter())
