0# x=[10,1,2]
# y = x
# y=[10,1,2]
# x[0] = 55
# print(x,y)

# num = {x:x**2 for x in range(6)}
# num.clear()
# print(num)

# keys = ["masala","Ginger","Lemon"]
# default_value = "Delicious"
# new_dict = dict.fromkeys(keys, default_value)
# print(new_dict)

# age = int(input("ennter you age"))
# if(age<13 and age>0):
#     print("child")
# elif(age>=13 and age <=19):
#     print("Teenage")
# elif(age>=20 and age<=59):
#     print("adult")
# elif(age>=60):
#     print("senior")
# else:
#     print("its an invalid age")

# a = int(input("Enter your mark"))
# if a<60:
#     print("your grade is D")
# elif a>60 and a<75:
#     print("your grade is B")
# day = int(input("Enter the day"))
# match day:
#     case 1:
#         print("Monday")
#     case 2: 
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Friday")
#     case _:
#         print("invalid")

# s = ["apple","banana","orange"]
# print(s.split(","))
# print(" ".join(s))


# x = int(input("enter a number"))
# try:
#     x/0
# except ZeroDivisionError:
#     print("number can not devided by zero")

# def my_decorator(func):
#     def wrapper():
#         print("before function runs")
#         func()
#         print("after the function runs")
#     return wrapper

# def say_hello():
#     print("hello")

# dec_func = my_decorator(say_hello)
# dec_func()

