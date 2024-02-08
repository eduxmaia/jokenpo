# # first_name = "Edu"
# # last_name = '1'
# # full_name = first_name + last_name
# # print(full_name)
# #
# # age = 17
# # print(age)
# # age = age + 1
# # print(age)
# # print(type(age))
# #
# # height = 1.88
# # print('Your height is: ' + str(height))
# #
# # name = 'eduardo'
# # height = 1.75
# # age = 17
# # print('Hi my is ' + name + ' i have ' + str(height) + ' and ' + str(age) + ' years old')
# # print(f'Hi my name is {name} i have {height} metros and {age} years old')
# #
# # print(len(name))
# # print(name.find('e'))
# # print(name.capitalize())
# # print(name.upper())
# # print(name.lower())
# # print(name.isdigit())
# # print(name.isalpha())
# # name2 = '17'
# # print(name2.isdigit())
# #
# # x = 2
# # y = 4
# #
# # y = str(y)
# # print('Y is '+y)
#
# # old = int(input('How old are you?: '))
# # old = old + 10
# # print('you have ' + str(old) + ' years old')
#
# import math
# from typing import List, Any
#
# # pi = 3.14
# # print((round(pi)))
#
# # name = "Edu Maia Caet"
# # first_name = name[:3]
# # mid_name = name[4:8]
# # reversed_name = name[::-2]
# # print(first_name)
# # print(mid_name)
# # print(reversed_name)
#
# # talheres = ('garfo', 'faca', 'colher')
# #
# # dado = {'1', '2', '3', '4', '5', '4', '6', '6'}
# #
# # dado2 = {'2', '9', '6', '8'}
# #
# # print(dado.union(dado2))
#
# # duos = {
# #     'Brazil': 'Brasilia',
# #     'USA': 'Washington DC'
# # }
# #
# # print(duos.get('Brazil'))
# # print(duos.get('USA'))
# # print(duos.values())
# # print(duos.items())
# # print(duos.keys())
#
# # age = int(input('How old are you?:'))
# # if age == 100:
# #     print("Vc tem cem anos")
# # elif age >= 18:
# #     print("You are an adult!")
# # elif age < 0:
# #     print('vc n nasceu')
# # else:
# #     print("You are an child!")
#
# # temp = int(input("What temp today?:"))
# #
# # # if temp >= 0 and temp <= 30:
# # #     print('esta de boa')
# # # elif temp > 0 or temp < 30:
# # #     print("esta ruim")
# # if not temp > 10:
# #     print('esta ruim')
#
# # name = ""
# # while len(name) == 0:
# #     name = input("Enter your name:")
# #
# # print("Hello " + name)
# # import time
# #
# # # for i range  (10):
# # #     print(i)
# #
# # for seconds in range(10,0,-1):
# #     print(seconds)
# #     time.sleep(2)
#
# # rows = int(input("How many rows?:"))
# # columns = int(input("How many columns?:"))
# # symbol = input("Entre a symbol?:")
# #
# # for i in range(rows):
# #     for j in range(columns):
# #         print(symbol, end="")
# #     print()
#
# # while True:
# #     name = input("Enter your name?:")
# #     if name != "":
# #         break
#
# # phone_number = '123-456-7890'
#
# # for i in phone_number:
# #     if i == "-":
# #         continue
# #     print(i, end="")
#
# # for i in range(1,10):
# #
# #     if i == 7:
# #         pass
# #     else:
#         print(i)

# for i in range(1,10):
#         input("how old are you?:")
#         print(i)

# utensils = {"garfo","faca","colher"}
# panelas = {"frigideira","pressao"}
# utensils.add(   "pano")
# panelas.add("faca")
# # utensils.update(panelas)
# # for garfo in utensils:
# #         print(garfo)
# # print(panelas.difference(utensils))
# print(utensils.intersection(panelas))
# capitals = {"Brasil": 'Brasilia',
#             'EUA': 'Whasington'}
# print(capitals.items())




# def hello(name,last_name,age):
#         print("Hello "+name)
#         print("u have "+str(age)+" years old")
#         print("have a good day")
#
# hello("edu","maia",18)

# def multiply(number1, number2):
#         return number1 * number2
#
# x = multiply(2,3)
# print(x)
#
# y = 3.4
# print(y.__round__())

# def add(*sla):
#     sum = 0
#     for i in sla:
#         sum += i
#     return sum
#
# print(add(3,4,5))

# def add(*args):
#     sum = 0
#     args = list(args)
#     args[0] = 0
#     for i in args:
#         sum += i
#     return sum
#
# print(add(3,4,5))

# name = "edu"
# print("Hello, my name is {} ".format(name))
# print("Hello, my name is {:5} nice too meet you".format(name))
# print("Hello, my name is {:>5} nice too meet you".format(name))
# print("Hello, my name is {:<5} nice too meet you".format(name))
# print("Hello, my name is {:^5} nice too meet you".format(name))

# try:
#     number = int(input("coloque um numero?:"))
#     divisor = int(input("coloque um divisor?:"))
#     result print(os.getcwd())
#
#  path = '\\home\\= number / divisor
#     print(result)
# except ZeroDivisionError as e:
#     print(e)
#     print("Vc n consegue dividir por 0")

import os
import os.path

# import os
#
# eduardo\\teste.txt'
#  if os.path.exists(path):
#      print('existe')
# #
# # with open(test.txt) as file:
# #     file.write(text)

import random

escolhas = ['pedra','papel','tesoura']
pedra = '1'
# '2' = papel
# '3' = tesoura
print(input("escolha pedra papel ou tesoura:"))
random = random.choice(escolhas)
print(random)