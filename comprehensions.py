""" comprehensions """

# a = []
# for i in range(10):
#     a.append(i)
# print(a)

# list2 = [i for i in range(10)]
# print(list2)

""" comprehensions - короткий способ записи циклов для создания 
коллекций(словари, списки, множества, кортежи) """

# list3 = [выражение for выражение in итерируемый_объект]

# names = ['Alina', 'Marina', 'Zarina', 'Gulya'] 
# guests = []
# for name in names:
#     guests.append(name + '10')
# print(guests)
# guests1 = [name + '10' for name in names]
# print(guests1)

# names = ['John', 'Amina', 'Mike', 'Dinara', 'Farida', 'Aliya']
# guests = []
# for name in names:
#     if name.startswith('A'):
#         guests.append(name)
# print(guests)

# guests1 = [name for name in names if name.startswith('A')]
# print(guests1)
# [выражение for выражение in итер_об if условие]



# nums = [1, 2, 3, 4, 5, 6]
# new_nums = []
# for i in nums:
#     if i % 2 == 0:
#         new_nums.append(i + 0.3)
#     else:
#         new_nums.append(i + 0.6)
# print(new_nums)

# new_nums2 = [num + 0.3 for num in nums if num % 2 == 0 else num + 0.6] # SyntaxError

# тернарный оператор
# i + 0.3 if i % 2 == 0 else i + 0.6

# new_num3 = [num + 0.3 if num % 2 == 0 else num + 0.6 for num in nums] # Ok 

#[тернарный оператор for элемент in итер_об]

# nums = [4, 3, 8, 7, 2, 1, 9]
# new_nums = []
# for i in nums:
#     if i > 5:
#         if i % 2 == 0:
#             new_nums.append(i + 0.3)
#         else:
#             new_nums.append(i + 0.6)
# print(new_nums)

# new_nums = [num + 0.6 if num % 2 != 0 else num + 0.3 for num in nums if num > 5]

# lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_list = []
# for i in lists:
#     # print(i, 'i')
#     for j in i:
#         # print(j, 'j')
#         new_list.append(j)
# print(new_list)
# new_list = [j for i in lists for j in i]
# print(new_list)

# a = (i for i in range(10))
# print(list(a))
# print(set(a))
# print(tuple(a))

# new_list = []
# for i in range(10):
#     new_list.append(i)
# print(new_list)

# words = ['making', 'book', 'sitting', 'writing']
# list2 = []
# for word in words:
#     if word.endswith('ing'):
#         list2.append(word * 2)
#     else:
#         list2.append(word * 3)
# print(list2)

dict_ = {'a': 1, 'b': 2, 'c': 3}
# b = {}
# for k, v in dict_.items():
#     b[k] = v
# print(b)
# c = {k: v for k, v in dict_.items()}
# print(c)


