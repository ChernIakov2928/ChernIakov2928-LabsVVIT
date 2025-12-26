#Задание 1
num = int(input("Введите число"))
for i in range(1, num+1):
    print(i)
    
num = int(input("Введите число"))
sum = 0
for i in range (1, num+1):
    sum = sum + i
a = sum / num
print("Среднее арифметическое =",a)

#Задание 2
num1 = int(input("Введите первое число"))
num2 = int(input("Введите второе число"))
if num1 > num2:
    print("Большее число: ",num1)
elif num1 < num2:
    print("Большее число: ",num2)
else:
    print("Числа равны")