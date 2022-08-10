""" Множества (set) """
# Множества - изменяемый, неупорядоченный тип данных. 
# Содержит в себе уникальные элементы и только неизменямые типы данных. 

# a = {}
# print(type(a)) # dict 

# b = set()
# print(type(b)) # set

# c = {'a', 1, True, (1, 2), 2.54, None}
# print(c) # Ok

# d = {1, 1, 1, 1}
# print(d) # {1}
# print(len(d)) # 1

# e = {1, 2, ['a', 'b']} # TypeError

# d = {1, 2, (1, 2, ['b', 'c'])} # TypeEror

# list_ = [1, 2, 3, 4, 4, 3, 1]
# a = set(list_)
# print(a)


""" 
Создайте словарь, ключами которого являются буквы английского алфавита,
а значениями – соответствующие им порядковые номера в алфавите.
Для удобства можете воспользоваться модулем string
"""
# a = {}
# num = 0
# for i in ascii_lowercase:
#     a[i] = num
#     num += 1

# print(a)

# alph = []
# for i in range(97, 123):
#     alph.append(chr(i))
# print(alph)
# dict_ = {}
# for i in alph:
#     dict_[i] = ord(i) - 96
#     print(dict_)
# emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
#        'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
#        'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
#        'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
#        'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
#        'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}

# for k, v in emails.items():
#     # print(k)
#     # print(v)
#     for name in v:
#         print(name + "@" + k)

user = {'name': 'Ruslana', 'age': 16, 'gender': 'woman',}
