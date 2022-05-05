#                                                                 Конспект 15.03.2021
#### --> Ошибки
"""
TypeError
ValueError
KeyError
IndexError
NameError
ZeroDivisionError
SyntaxError
ArgumentError
ArgumentTypeError
ValidationErr
EOFError
ImportError
RuntimeError
IndentationError
TimeoutError
"""

# d = {"key": "1", "key": 2}
# print(d["key"])

# def - define
# Function --> JavaScript
# Function name --> JavaScript

# f(x) = x * 2
# f(4)
# f(8)
# f(10)



# def add():
#     num1 = 15
#     num2 = 20
#     res = num1 + num2
#     return res
# print(add())

# def add():
#     num1 = 15
#     num2 = 20
#     res = num1 + num2
#     return res
# resp = add()
# print(resp)



# db = []
# def save(data):
#     db.append(data)
# save({"key": 15})
# save({"key1": 25})
# save({"key2": 25})
# print(db)



# def swapcase_str(string: str) -> str:
#     if string.islower():
#         return string.upper()
#     else:
#         return string.lower()
# res = swapcase_str("HELLO")

# def swapcase_str(string):
#     if string.islower():
#         return string.upper()
#     else:
#         return string.lower()
# res = swapcase_str("HELLO")
# print(res)

# def swapcase_str(string):
#     if string.islower():
#         return string.upper()
#     else:
#         return string.lower()
# res = swapcase_str("hello")
# print(res)



#test1+@gmail.com

# def check_add_email(email):
#     full_email = ""
#     if '@' not in email:
#         full_email = email + "@gmail.com"
#         return full_email
#     return email
# res1 = check_add_email("test1")
# res2 = check_add_email("test1@gmail.com")
# print("First: ", res1)
# print("Second: ", res2)



# def get_even_num(num):
#     even_nums = []
#     for x in range(1,num):
#         if x % 2 == 0:
#             even_nums.append(x)
#         else:
#             continue
#     return even_nums
# res1 = get_even_num(10)
# res2 = get_even_num(5)
# res3 = get_even_num(15)
# print("First: ", res1)
# print("Second: ", res2)
# print("Third: ", res3)




# db_users = ["John", "Raychel", "Jessica", "Peter"]
# def login_required(username):
#     if username not in db_users:
#         print("Вы не вошли в аккаунт!!!")
#         username = input("Логин: ")
#         return login_required(username)
#     else:
#         return "Вы успешно вошли в аккаунт"
# res = login_required("Aibek")
# print(res)



# def add(num1, num2):
#     return num1 + num2

# def substract(num1, num2):
#     return num1 - num2

# def divide(num1, num2):
#     return num1 / num2

# def multiple(num1, num2):
#     return num1 * num2

# def main():
#     num1 = int(input("Enter the first num: "))
#     num2 = int(input("Enter the second num: "))
#     operator = input("Choose the operator: +/*-: ")
#     res = None
#     if operator == '-':
#         res = substract(num1, num2)
#     elif operator == '+':
#         res = add(num1, num2)
#     elif operator == '/':
#         res = divide(num1, num2)
#     elif operator == '*':
#         res = multiple(num1, num2)
#     else:
#         print("I don't understand your operator symbol!!!")
#     print(res)
# main()



# Try - except --> Error: ZeroDivisionError! (divide!)


# def add(num1, num2):
#     return num1 + num2

# def substract(num1, num2):
#     return num1 - num2

# def divide(num1, num2):
#     try:
#         return num1 / num2
#     except ZeroDivisionError:
#         print("You can't divide to zero number!!!")

# def multiple(num1, num2):
#     return num1 * num2

# def main():
#     num1 = int(input("Enter the first num: "))
#     num2 = int(input("Enter the second num: "))
#     operator = input("Choose the operator: +/*-: ")
#     res = None
#     if operator == '-':
#         res = substract(num1, num2)
#     elif operator == '+':
#         res = add(num1, num2)
#     elif operator == '/':
#         res = divide(num1, num2)
#     elif operator == '*':
#         res = multiple(num1, num2)
#     else:
#         print("I don't understand your operator symbol!!!")
#     print(res)
# main()




# while --> Бесконечный цикл 😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁


# def add(num1, num2):
#     return num1 + num2

# def substract(num1, num2):
#     return num1 - num2

# def divide(num1, num2):
#     try:
#         return num1 / num2
#     except ZeroDivisionError:
#         print("You can't divide to zero number!!!")

# def multiple(num1, num2):
#     return num1 * num2

# def main():
#     num1 = int(input("Enter the first num: "))
#     num2 = int(input("Enter the second num: "))
#     operator = input("Choose the operator: +/*-: ")
#     res = None
#     if operator == '-':
#         res = substract(num1, num2)
#     elif operator == '+':
#         res = add(num1, num2)
#     elif operator == '/':
#         res = divide(num1, num2)
#     elif operator == '*':
#         res = multiple(num1, num2)
#     else:
#         print("I don't understand your operator symbol!!!")
#     print(res)
#     question = input("Do you want to continue operation? Yes or No: ")
#     if question.lower() == "yes":
#         return main()
#     else:
#         return
# main()




# Try - except --> calculate


# def add(num1, num2):
#     return num1 + num2

# def substract(num1, num2):
#     return num1 - num2

# def divide(num1, num2):
#     try:
#         return num1 / num2
#     except ZeroDivisionError:
#         print("You can't divide to zero number!!!")

# def multiple(num1, num2):
#     return num1 * num2

# def main():
#     try:
#         num1 = int(input("Enter the first num: "))
#         num2 = int(input("Enter the second num: "))
#     except ValueError as error:
#         print(error)
#         return main()
#     operator = input("Choose the operator: +/*-: ")
#     res = None
#     if operator == '-':
#         res = substract(num1, num2)
#     elif operator == '+':
#         res = add(num1, num2)
#     elif operator == '/':
#         res = divide(num1, num2)
#     elif operator == '*':
#         res = multiple(num1, num2)
#     else:
#         print("I don't understand your operator symbol!!!")

#     print(res)
#     question = input("Do you want to continue operation? Yes or No: ")
#     if question.lower() == 'yes':
#         return main()
#     else:
#         return 

# main()


"""
Параметры --> мы указываем их в начале создании функции внутри скобок

Аргументы --> мы когда запускаем передаем аргументы вместо параметров:
    Именованные аргументы --> {}
    Позиционные аргументы --> ()

Параметры по умолчанию(default)

Мы можем передать в функции неограниченное количество аргументов(ОЗУ)

Или ограничение мы можем сами сделать

def generate_name(name):
    #...
    pass
generate_name("John")

"""
# def some_func(a, b, c, d):

# def add(num1, num2):
#     return num1 + num2

# def add(num1, num2=12):
#     print(num1 + num2)
# add(12)

# def get(a, b, c=None):
#     pass
# get(1, 2, 3)

# def some_funct(*args, **kwargs):
#     print(args, kwargs)
# some_funct(12, 14, 15, 16, a="hello", b="world")
                                                                                                #--> Thank you <--#