# Конспект 17.03.2022

"""
len()        --> вытаскивает длину объекта
print()      --> Печатает в консоль значение
input()      --> запрашивает данные
divmod()     --> остаток от деления
dir()        --> выводит методы объекта
globals()    --> выводит словарь с глобал данными
locals()     --> выводит словарь с локальными данными
round()      --> округляет число
enumerate()  --> нумирует итерируемые объекты, можно указать старт нумерации
pow()        --> степень выводит, остаток от деления
min()        --> минимальное число выводит
max()        --> максимальное число выводит
type()       --> выводит тип данных объекта
id()         --> вывод айди объекта
range()      --> создает диапазон start:end:step
sorted()     --> временно сортирует объект
"""
# func abs()
# negative = -125
# absolute = abs(negative)
# print(absolute)

# all --> ALL --> all --> ALL --> all --> ALL --> all --> ALL --> all

# list_of_zeros_num = [0, 1, 2]
# is_true = all(list_of_zeros_num)
# print(is_true)
#                                     print(False)


# tuple_of_trues_obj = (True, 1, 2, 3)
# is_true = all(tuple_of_trues_obj)
# print(is_true)
#                         print(True)





# # [1, 2, 3]

# def all_(iterable):
#     for element in  iterable:
#         if not element:
#             return False
#     return True
# is_true = all((True, 1, 2, 3))
# print(is_true)
#             print(True)

# def all_(iterable):
#     for element in  iterable:
#         if not element:
#             return False
#     return True
# is_true = all((True, 1, 2, 3, 0))
# print(is_true)
#                 print(False)



# def any_(iterable):
#     for element in iterable:
#         if element:
#             return True
#     return False
# print(any_([0, 0, 1]))
#             print(True)


# def any_(iterable):
#     for element in iterable:
#         if element:
#             return True
#     return False

# print(any_([0, 0, 0]))
#                 print(False)
#####################################################################################

# ascii()
# example_one = ascii([0, 1])
# print(example_one)


# example_one = ascii([0, 1, 'қ'])
# print(example_one)


# one = bin(1)
# print(one)


# bool() True False

# callable()


# key = 0b0100110 #'0b' indicates this is in second base
# Encryption = key Input
# print Encryption


# key = 0b1

# encrypt = key ^ 2
# print(encrypt)
# #                                                   Вызываемая функция
# def add(a, b):
#     return a + b
# is_callable = callable(add)
# print(is_callable)
# #           print(True)


#                       Невызываемые функци
# @property
# def add(a, b):
#     return a + b
# is_callable = callable(add)
# print(is_callable)
#                                     print(False)

# @property
# def name(name):
#     print(name)

# name = "hello"
# print(name)


# print(type(""))
# print(type(12))
# int()
# str()
# custome_class()

# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# res = list(enumerate(seasons))
# print(res)


# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# res = enumerate(seasons)
# print(res)


# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# res = list(enumerate(seasons, start=10))
# print(res)


# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# res = dict(enumerate(seasons, start=10))
# print(res)


# name1 = ["John", "Raychel"]
# name2 = ["Peter", "Jessica"]

# for index, value in enumerate(name1):
#     print(value)
#     print(name2[index])
    
















