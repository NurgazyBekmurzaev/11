# Конспект 17.03.2022

# class A():
#     def func(a, b, c, d):
#         pass

# class B(A):
#     def func(a, *args, **kwargs):
#         pass

# func(a, b, c, d)


# def func(arg1, arg2=12)
# def func(arg1, arg2=False)
# def func(arg1, arg2="Hello")
# def func(arg1, arg2=None):
#     pass
# def func(arg1, arg2=()):
#     pass
# def func(arg1, arg2={}):
#     pass


# ls = []

# def func(arg1, arg2=[]):
#     print(arg1, arg2)
# func("hello")

# def func(arg1, arg2=[]):
#     arg2.append("hello")
#     print(arg2)
# func("hello")

# def func(arg1, arg2=[]):
#     arg2.append("hello")
#     print(arg2)
# func("hello")
# func("world")

# def func(arg1, arg2=[]):
#     arg2.append(arg1)
#     print(arg2)
# func("hello")
# func("world")

# def func(arg1, arg2):
#     arg2 = []
#     arg2.append(arg1)
#     print(arg2)
# func("hello", "2")
# func("world", "2")


#########################################################################################################



# this_var_is_visible = "Can be seen inside and outside function"

# def var_visibility():
#     this_is_not_visible = "cannot  be seen outside function"
#     return

# print(this_var_is_visible)
# print(this_is_not_visible)
#                                                                          print(NameError: name 'this_is_not_visible' is not defined)       

#                                   Type of Namespaces
# Built-in namespace
#   Global namespace
#       Local namespace


# def func(a, b):
#     return a + b
# res = func(12, 14)
# print(res)
#                          print(26)


# def some_func():
#     print(locals())
# some_func()
#             print( {} )

# def some_func(name):
#     print(locals())
# some_func("Asus")
#                          print({'name': 'Asus'})


# name = "Asus"

# def get_name():
#     name = "Acer"
# get_name()
# print(name)
#                                       print("Asus")


# name = "John"

# def get():
#     name = "Raychel"
#     print(locals())
# get()
# print({'name': 'Raychel'})



# name = "John"

# def get():
#     name = "Raychel"
#     print(locals())
# get()
# print(locals())
#                   print({'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7fa68cee44c0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/isumar/Desktop/Makers/Week3/lection8/scope_namespaces.py', '__cached__': None, 'name': 'John', 'get': <function get at 0x7fa68cd8ddc0>})


# name = "Lenovo"

# def func_one():
#     name = "Asus"

#     def func_two():
#         name = "Acer"
#         print(name)
#     func_two()
# func_one()
#                                 #print("Acer")


# name = "Lenovo"

# def func_one():
#     name = "Asus"

#     def func_two():
#         #name = "Acer"
#         print(name)
#     func_two()
# func_one()
#                                  print("Asus")



# name = "Lenovo"

# def func_one():
#     #name = "Asus"

#     def func_two():
#         #name = "Acer"
#         print(name)
#     func_two()
# func_one()
#                                    print("Lenovo")



# map = "Lenovo"

# def func_one():
#     map = "Asus"

#     def func_two():
#         map = "Acer"
#         print(map)
#     func_two()
# func_one()
#                             print("Acer")



# map = "Lenovo"

# def func_one():
#     map = "Asus"

#     def func_two():
#         #map = "Acer"
#         print(map)
#     func_two()
# func_one()
#                             print("Asus")



# map = "Lenovo"

# def func_one():
#     #map = "Asus"

#     def func_two():
#         #map = "Acer"
#         print(map)
#     func_two()
# func_one()
#                               print("Lenovo")



#map = "Lenovo"

# def func_one():
#     #map = "Asus"

#     def func_two():
#         #map = "Acer"
#         print(map)
#     func_two()
# func_one()
#                             print(<class 'map'>)


################################################################################################################
"""
Local                                       L
Enclosed                                    E
Global                                      G
Built-ins                                   B
"""



# for x in range(1, 100):
#     if isinstance(x, str):
#         break
#     else:
#         continue
# print(x)
#                       print(99)


# str_ = "hello"

# if str_ == "hello":
#     name = "John"
# print(name)
#                         print(John)



# str_ = "hell"

# if str_ == "hello":
#     name = "John"
# else:
#     name = "default"
# print(name)
#                             print(default)


# names = {}
# def func():
#     global names
#     names["key"] = "John"
# func()
# print(names)


# names = {}
# def func():
#     #global names
#     names["key"] = "John"
# func()
# print(names)



# def f():
#     global s
#     s += "GFG"
#     print(s)
#     s = "Look for Geeksforgeeks Python Section"
#     print(s)
# # Global Scope
# s = "Python is great!"
# f()
# print(s)

###############################################################################




# a = 1
#             #Uses global because there is no local "a"
# def f():
#     print("Inside g () :", a)
#             #Variable "a" is redefined as a local
# def g():
#     a = 2
#     print("Inside g() : ", a)
#             #Uses global keyword to modify global "a"
# def h():
#     global a 
#     a = 3
#     print("inside h() : ", a)
#             #Global scope
# print("global : ", a)  
# f() #--> 1
# print("global : ", a)  
# g() #--> Inside g(): 2
# print("global : ", a)  
# h() #--> Inside h(): 3
# print("global : ", a)  
# print(a) #--> Inside




# def func_one():
#     x = "John"
#     def func_two():
#         nonlocal x
#         x = "Raychel"
#         print("First:", x)
#     func_two()
#     print("Second: ", x)
# func_one()































