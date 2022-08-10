""" Списки и циклы """

# list()
# Список - изменяемый, упорядоченный, индексируемый, итерируемый тип данных.
# Нужен для хранения нескольких элементов

# Элементами могут быть любые типы данных

# list_ = [1, 'string', True, False, [1, 2], None, {'a': 12}, {1, 2}, ('a', 'b', 'c')]
# print(list_)

from mimetypes import types_map
import types
from xml.dom.expatbuilder import InternalSubsetExtractor
from xml.dom.minidom import Element


list1 = [1, 2, 3, 4, 5, [6, 7]]
list1[0] # 1
list1[1] # 2
list1[2] # 3
list1[5] # [6, 7]
list1[5] [0] # 6
list1[-1] # [6, 7]

list1[2:-2:] # [2, 3, 4]

""" добавление элементов в список """

a = [1, 2 , 3]

# a.append(element) - добавляет элемент в конец списка
# print('До', a)
# a.append(4)
# print('После', a)

# a.insert(index, element) - вставляет элемент на место указанного индекса
# print('До', a)
# a.insert(1, 'hello')
# print('После', a)

# a.append(element) -> a.insert(len(a)), element)

# a.insert(1234, 'world') # добавил в конец [1, 2, 3, 'world']

# a.extend(list2) - добавляет все элементы list2 в list1 

# mylist1 = [4, 2, 6]
# mylist2 = [1, 3, 8]

# mylist1.append(mylist2)
# print(mylist1) # [4, 2, 6, [1, 3, 8]]

# mylist1.extend(mylist2)
# print(mylist1)# [4, 2, 6, 1, 3, 8]

# newlist = mylist1 + mylist2
# print(mylist1) # [4, 2, 6]
# print(newlist) # [4, 2, 6, 1, 3, 8]

""" замена элементов """
# b = ['a', 'b', 'c', 'd']
# b[2] # 'c'
# b[2] = 'g'
# print(b) # ['a', 'b', 'g', 'd']

""" удаление элементов """
ab = ['a' , 'b', 'c', 'd']

# ab.pop([index]) - удаляет элемент по указанному индексу,
# но если индекс не указан, удаляет последений элемент.
# Возвращает удаленный элемент

# ab.pop(1)
# print(ab) # ['a', 'c', 'd']

# ab.pop()
# print(ab) # ['a', 'b', 'c']

# deleted_el = ab.pop(2)
# print(deleted_el) # 'c'
# print(ab) # ['a', 'b', 'd']
# ab.append(deleted_el) # ['a', 'b', 'd', 'c']

# list3.remove(значение) - удаляет первый встретившийся элемент с указанным значением

# list3 = ['Azamat', 'Kolya', 'Adilet', 'Azamat']
# list3.remove('Azamat')
# print(list3) # ['Kolya', 'Adilet', 'Azamat'] 
# list3.remove(20) #ValueError

# ab.clear() - полностью очищает список
# ab.clear()
# print(ab) # []

# del element
# del ab
# print(ab)

# del ab[3]
# print(ab) # ['a', 'b', 'c']

# del ab[:2]
# print(ab) # ['c', 'd']

# a1 = [1, 2, 3]
# b2 = a1

# b2.append(4)
# print(b2) # [1, 2, 3, 4]
# print(a1) # [1, 2, 3, 4]
# print(b2 is a1) # True

""" Копирование списков """
# a3 = [1, 2, 3]
# a4 = a3,copy()
# a5 = a3[:]

""" Сортировка списка """

# num_list = [4, 3, 8, 5]
# num_list.sort()
# print(num_list) # [3, 4, 5, 8]

# num_list.sort(reverse=True)
# print(num_list) # [8, 5, 4, 3] - сортировка в обратном порядке

# str_list = ['b', 'c', 'e', 'a', 'd']
# str_list.sort()
# print(str_list)


# b5 = ['a', 'b', 'c', 'a', 'a']
# print(b5.count('a')) # 3

# b5.index('c') # 2

""" циклы """

# Цикл - многократное выполнение определенного участка кода

iter_list = [1, 2, 3, 4, 5]
# print(iter_list[0])
# print(iter_list[1])
# print(iter_list[2])
# print(iter_list[3])
# print(iter_list[4])


# 1. for
# 2. while
# for item in iter_list:
#        print(item)

# Итерация - повторение какого-либо действия

# for - цикл работает до тех пор, пока элементы в итерируемом объекте не заканчиваются
# or элемент in итерируемый_объект:
#         тело цикла

# mail_list = ['azamat', 'mirbek', 'baatai', 'alym']
# result = []
# for name in mail_list:
#     gmail = name + '@gmail.com'
#     result.append(gmail)
# print(result)

# int
# str
# list
# bool
# tuple
# set
# dict

# print(dir(list))

# types_list = [int, str, list, bool, None, set, dict, tuple]
# iter_objs = []
# non_iter_objs = []
# for obj in types_list:
#         if '__iter__' in dir(obj):
#             iter_objs.append(obj)
#         else:
#             non_iter_objs.append(obj)
# print(f'Итерируемые объекты: {iter_objs}')
# print(f'Неитерируемые объекты: {non_iter_objs}')

# range() - функция для генерации последовательности чисел
# range(start, stop, step)
# range(stop)
# print(list(range(10))) # преобразование последовательностей чисел в список из чисел

# num_list = []
# for num in range(9, 101):
#     num_list.append(num)
# print(num_list)

# num_list = []
# for num in range(1, 101):
#     if num % 2 == 0:
#         num_list.append(num)

# print(num_list)

# num_list = []
# for num in range(0, 101, 2):
#     num_list.append(num)
#     print(num_list)

# list_of_lists = [[1, 2, 3], ['a', 'b', 'c'], [4, 5, 6]]
# for list1 in list_of_lists:
#     for elem in list1:
#         print(elem)

# string = 'helloworld'
# for i in string:
#     print(i)

# for _ in range(5):
#     print('hello')

""" цикл while """

# num = 10
# while num < 11:
#     print('num')

# Бесконечный цикл
# while True
#      print('hello)

# while условие - цикл работает до тех пор, пока условие истинно(True)

# Запрашивать число до тех пор, пока сообщение не будет равно 'stop'
# msg = input('Введите сообщение или stop ')
# while msg != 'stop':
#     print(msg)
#     msg = input('Введите сообщение или stop')

# break - останавливает работу цикла
# continiue - 

# while True:
#     msg = input('Введите сообщение')
#     if msg == 'bye':
#         print('интерация пропущена')
#         continue
#     print(msg)

# for num in range(10):
#         print(num)
# else:
#         print('цикл окончен')

# else в циклах срабатывает при успешном окончании цикла

# for num in range(10):
#         if num == 5:
#                 break
# else:
#         print('цикл окончен')



