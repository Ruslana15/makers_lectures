""" кортеж(tuple) """
# Кортеж - неизменяемая последовательность элементов. Ведет себя как список, но не изменяется.

# print(dir(tuple))

# my_tuple = (1, 2 ,3, 4, 5)
# print(type(my_tuple)) # tuple
# a = (2)
# print(type(a)) # int
# b = ('str', )
# print(type(b)) # tuple
# c = [1, 2, 3], 'string', 3
# print(type(c)) # tuple
# d = 1, 
# print(type(d)) # tuple



# tuple1 = (3, 3, 4 ,5 , 6, 3)
# print(tuple1.count(3)) # 3
# print(tuple1.index(4)) # 4


# num = 1
# num2 = 2
# num3, num4, num5 = 4, 7
# print(num3, num4) # 4 7

  
# tuple2 = ('str1', 'str2', 'str3')
# print(*tuple2)
# print(tuple2[0], tuple2[1], tuple2[2])

# nums = (10, 5)
# print(pow(*nums))

# a, b, *c = 1, 2, 3, 4
# print(a)
# print(b)
# print(c)
# a = (1, 2, 3, ['str', 'str2'])
# # a[2] = 5 # Error
# a[3].append(4)
# print(a)


# new_tuple = (('name', 'Sardar'), ('name', 'Sanjar'), ('name', 'Raimbek'), ('name', 'Ruslana'))
# # for i in new_tuple:
# #     print(i)

# for key, value in new_tuple:
#     print(key)
#     print(value)

# list_ = [1, 2, 3, 4, 5]
# for i in list_:
#     print((i))

# index = 0
# while index < len(list_):
#     list_[1]
#     print(list_[index])
#     index += 1

# Написать программу, которая будет запрашивать количество денег, которое вы хотите потратить. 
# Если вы указываете число больше денег в кошельке, программа предупреждает об этом и останавливается.
# Иначе отнимается указанное число из кошелька и печатает количество оставшихся денег.

"""ЗАДАНИЕ"""
# money = 10000
# while True:
#     spend = int(input('Сколько денег вы хотите потратить?'))
#     if money < spend:
#         print('Недостаточно средств')
#         break
#     money -= spend
#     print('Ваш баланс:', money)
    

# len(последовательность) - возвращает количество элементов в последовательности
# max(последовательность)
# min(последовательность)
# sum(последовательность)

# numbers = (3, 6, 1, 4, 5)
# print(max(numbers)) # 6
# print(min(numbers)) # 1
# print(sum(numbers)) # 19

# counter = 0 
# for num in numbers:
#     counter += num
#     print(counter)
# # 
# a = [1, 2, 3]
# a = (1, 2, 3)
# print(a.__sizeof__())
# print(b.__sizeof__())

for i in "abcd"[::-1]:
    print(i)
