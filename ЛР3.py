#Задание 1 и 3
def read_file(namefile, mode = 'all'):
    try:
        if mode == 'all':
            with open(namefile, 'r') as file:
                content = file.read()
                return(content)
        elif mode == 'line':
            with open(namefile, 'r') as file:
                 strings = [line for line in file]
                 return strings
        else:
            print("Неизвестный тип чтения")
    except FileNotFoundError:
        print("Ошибка: файл не найден")

result = read_file('example.txt', 'line')

if type(result) == list:
    for line in result:
        print(line)
else:
    print(result)
#Задание 2
def write_new_file(namefile, content):
    with open(namefile, 'w') as file:
        file.write(content)
    print("Текст записан в файл", namefile)
        
def append_to_file(namefile, content):
    with open(namefile, 'a') as file:
        file.write(content)
        print("Текст добавлен в файл", namefile)

user_text = input('Введите текст для записи в новый файл:')
write_new_file('user_input.txt', user_text)

user_add = input("Введите текст для добавления в существующий файл: ")
append_to_file('user_input.txt', user_add)
