# привет - hello

""" словари (dict) """
# Словари - изменяемый, итерируемый тип данных. Состоят из пар: ключ: значение
# Ключами могут быть только неизменяемые типы данных(tuple, str, int, None, bool),
# а значениями - любые. Ключи должны быть уникальными.

from re import I


dict_ = {}
# passport = {'name': 'Руслана', 'last name': 'Комарова',
# 'age': 16, 'gender': 'W', 'birthday': '15.08.2006'}

# print(passport['name']) # 'Айбек'
# print(passport['age']) # 16
# print(passport[0]) # Error (в словарях нет индексов)

# dict2 = dict(name='Агахан', last_name='Кадыров', age=17)
# print(dict2) # {'name': 'Агахан', 'last_name': 'Кадыров', 'age': 17}

# dict3 = dict.fromkeys(['a', 'b'], 25)
# print(dict3) # {'a': 25, 'b': 25}

# dict4 = dict.fromkeys(['a', 'b'])
# print(dict4) # {'a': None, 'b': None}

# dict5 = dict([('name', 'John'), ('last_name', 'Watson')])
# print(dict5) # {'name': 'John', 'last_name': 'Watson'}
# print(dict5['name'])

""" Методы словарей """
passport = {'name': 'Руслана', 'last name': 'Комарова',
'age': 16, 'gender': 'W', 'birthday': '15.08.2006'}
# passport['name'] # "Руслана"
# passport['ID'] # KeyError
# print(passport.get('name')) # 'Руслана'
# print(passport.get('ID')) # None

# dict.get(key, None) - отдает значение указанного ключа, если нет - отдает второе 
# указанное значение (по умолчанию None)

# print(passport.get('ID', 'Нет такого ключа')) # Нет такого ключа

# passport.setdefault(key, None) - отдает значение указанного ключа, 
# если его нет - создает его со значением default(по умолчанию - None)

# print(passport.setdefault('age')) # 16 
# print(passport.setdefault('ID')) # none
# print(passport.setdefault('ID', 5436642))
# print(passport) # {'name': 'Руслана', 'last name': 'Комарова', 'age': 16, 'gender': 'W', 'birthday': '15.08.2006', 'ID': 5436642}

# passport.update({key: value}) - принимает в себя другой словарь и обновляет 
# исходный словарь за счет него 

# dict8 = {'name': 'Ruslana', 'age': 16, 'name': 'Агахан', 'ID': 254576}
# passport.update(dict8)
# print(passport)
# print(dict8) # {'name': 'Агахан', 'age': 16}

# a = {'a': 10, 'b': 20,}
# a['c'] = 30
# a['b'] = 40 # {'a': 10, 'b': 40, 'c': 30}
# print(a) # {'a': 10, 'b': 20, 'c': 30}

dict10 = {'name': 'Tima', 'last_name': 'Dootaliev', 'age': 21}
# dict10.pop('name') 
# print(dict10) # {'last_name': 'Dootaliev', 'age': 21}

# deleted_el = dict10.pop('ID', 'Нет такого ключа')
# print(deleted_el) # 'Нет такого ключа'
# print(dict10) 

# deleted_el = dict10.popitem() 
# print(deleted_el)
# print(dict10)

# dict10.clear()
# print(dict10) # Полностью очищает весь словарь ({})

# del dict10['age']
# print(dict10) # {'name': 'Tima', 'last_name': 'Dootaliev'}

iter_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# for i in iter_dict:
#     print(i) # keys

# for i in iter_dict:
#     print(iter_dict[i]) # values

""" методы keys(), values(), items() """
# k = iter_dict.keys()
# print(k) # dict_keys(['a', 'b', 'c', 'd'])
# for key in k:
#     print(key)

# v = iter_dict.values()
# for value in v:
#     print(value)
# print(v) # dict_values([10, 20, 30, 40])

# i = iter_dict.items()
# print(i) # dict_items([('a', 10), ('b', 20), ('c', 30), ('d', 40)])
# for key, value in i:
#     print(f'ключи {key}, значения {value}')

contacts = {
    'names': {
        'Arstan': 6378592478,
        'Nursultan': 23568823,
        'Aibike': 989471113
    }
}
# print(contacts['names']['Aibike'])
# names = contacs['names']
# print(names['Aibike'])

# copy() - копирует словарь 
contacts_copy = contacs.copy()

