#Задание 1
class UserAccount:
    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password: str) -> None:
        self.__password = new_password

    def check_password(self, password: str) -> bool:
        return self.__password == password

user = UserAccount("Chern", "nalkabbaklan@gmail.com", "12315401")
print(user.check_password("12315401"))  # True
user.set_password("cherN")
print(user.check_password("12315401"))  # False
print(user.check_password("cherN"))  # True

#Задание 2
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"Марка: {self.make}, Модель: {self.model}"

class Car(Vehicle):
        def __init__(self, make, model, fuel_type):
            super().__init__(make, model)
            self.fuel_type = fuel_type

        def get_info(self):
            base_info = super().get_info()
            return f"{base_info}, Тип топлива: {self.fuel_type}"


vehicle = Vehicle("Porsche 911", "911 Turbo серии 997")

car1 = Car("Toyota", "Tundra", "бензин")
car2 = Car("Tesla", "Model X", "электричество")
car3 = Car("Haval", "H5", "дизель")

print("Базовый класс Vehicle:")
print(vehicle.get_info())
print(car1.get_info())
