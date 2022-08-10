""" Условные выражения """

# >
# <
# == 
    # --> bool()
# !=
# >=
# <=

# print(20 > 10)
# print(15 < 5)

# print(bool(0)) # False
# print(bool(1)) # True
# print(bool(2)) # True

bool('') # False
bool([]) # False
bool({}) # False
bool(set()) # False
bool(None) # False

""" if """
# num = 15
# if num > 16: 
#     print('Hello world')

""" else"""
# num = 10
# if num > 16: 
#     print('Hello world')
#     else:
#         print('Goodbye world')

# temperature = 40
# if temperature < 20: 
#     print('холодно')
# else:
#     if temperature < 30:
#         print('тепло')
#     else:
#         if temperature > 35:
#             print('жарко')

""" elif """
# temperature = 40
# if temperature < 20:
#     print('холодно')
# elif temperature < 30:
#     print('тепло')
# elif temperature > 35:
#     print('жарко')
# else:
#     print('очень жарко')

# num = 15
# if num < 20:
#     print('ok')
# if num > 10:
#     print('same')
# if num < 23:
#     print('good')

# mark = input('Введите оценку от 1 до 10 ')

# if mark == 10:
#     result = 5
# elif mark < 10:
#     result = 4
# elif mark < 5:
#     result = 3
# else:
#     result = 2
# print(result)

# if условие
#     действие
# elif условие: 
#     другое действие
# else:
#     действие в случае если ни одно из выше указанных условий не сработало

# in -  проверка на вхождения
# string = 'Hello! Как твои дела?'
# if 'hello' in string.lower():
#     print('hi')
# else:
#     print(';-(')

# string = 'Привет! Как твои дела?'
# if 'привет' not in string.lower():
#     print(';-(')
# else:
#     print('со мной поздоровались :)')

""" and, or, not """
False and False # False
True and True # True
False and True # False
True and False # False

# age = 16
# if age > 15 or age < 18:
#     print('Ok')
# else:
#     print('Not ok')

not False # True
not True # False

# print(int(False)) # 0
# print(int(True)) # 1
True + True # 2

# a = 10
# [действие1, действие2] [условие]
# print(['ok', 'not ok'][a > 10])

""" Тернарный оператор """
# a = ''
# msg = input('Введите сообщение:  ')
# if len(msg) > 10:
#     a = 'Сообщение длиннее 10 символов'
# else:
#     a = 'Сообщение меньше 10 символов'
# print(a)

# msg = input('Введите сообщение')
# print('Сообщение длиннее 10 символов' if len(msg) > 10 else 'Сообщение меньше 10 символов')
# действие if условие else 
# другое_действие

# a = 1 
# if a:
#     print('ok')

# color = input('Выберите цвет')
# match color:
#     case 'red':
#         print('ok, red')
#     case 'white':
#         print('ok, white')
#     case 'black':
#         print('ok, black')
#     case _:
#         print('we don\'t have this color')


# a = 'string'
# assert len(a) == 0
# print('It\'s ok')

first_num = int(input('1 '))
assert first_num == 30, 'число неверное'
print('число верное')

