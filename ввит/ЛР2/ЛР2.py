#Задание 1
def greet(name):
    return f"Привет, {name}!"
name = input("Введите имя ")
print(greet(name))

##Задание 2
def square(number):
    number = number**2
    return number

n = int(input("Введите число: "))
resultt = square(n)
print("Квадрат вашего числа: ", resultt)

###Задание 3
def max_of_two(x, y):
    if x != y:
        if x > y:
            return x
        else:
            return y
    else:
        print("Числа одинаковые")

number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
resulttt = max_of_two(number1, number2)
print("Наибольшее число: ", resulttt)

##Задание 4
def describe_person(name, age=30):
    return(f"{name}, {age}")

user_name = input("Введите ваше имя: ")
user_age = input("Введите ваш возраст: ")
if user_age:
    print(describe_person(user_name, user_age))
else:
    print(describe_person(user_name))

    print("Имя:", user_name)
    print("Возраст:", user_age)

##Задание 5
def is_prime(number):
    if number == 2 or number == 3 or number == 5 or number == 7:
        return True
    elif number == 1 or number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
        return False
    else:
        return True

number = int(input("Введите число:"))
r = is_prime(number)
print(r)