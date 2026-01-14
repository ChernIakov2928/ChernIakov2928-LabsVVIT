#Задание 1
import math
number = int(input("Введите число: "))
sqrt_number = math.sqrt(number)
print(f"квадратный корень из {number} равен {sqrt_number}")

import datetime
print("Текущие дата и время:", datetime.datetime.now())

#Задание 2
import my_module
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

result = my_module.sum(a,b)

print(f"Сумма чисел: {result}")


#Задание 3
from pack import numbers, strings
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
result1 = numbers.multiply(a, b)

print(f"{a} * {b} = {result1}")

text = input("Введите строку: ")
print(f"Перевёрнутая строка: {strings.reverse_string(text)}")