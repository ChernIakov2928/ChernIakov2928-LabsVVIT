#Задание 1
import math
def square_root(num):
    return math.sqrt(num)
num = int(input('Введите число:'))
square_root(num)

import datetime
print('Текущие дата и время:', datetime.datetime.now())

#Задание 2
import my_module
my_module.sum(2,4)

#Задание 3
from pack import numbers, strings
numbers.even(2)
strings.read_file('example.txt', 'all')
