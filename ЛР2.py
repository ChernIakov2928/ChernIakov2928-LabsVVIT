#Задание 1
def greet(name):
    return name

person = str(input("Как вас зовут?: "))
result = greet(person)
print("Привет, ", result)

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
person = str(input("Введите ваше имя: "))
opt = str(input('хотите ли ввести возраст? (да/нет?)'))
if opt == 'да':
    years = str(input("Введите ваш возраст: "))
    describe_person(person, years)
else:
        describe_person(person)
    
person = input()
age = input()
if age:
    print(describe_person(person, age))
else:
    print(describe_person(person))

##Задание 5
#Задание 5
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