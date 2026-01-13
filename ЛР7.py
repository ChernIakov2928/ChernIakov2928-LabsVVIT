class Employee:
    def __init__(self, name, emp_id: int):
        self.name = name
        self.emp_id = emp_id
    
    def get_info(self):
        return f'{self.name}, {self.emp_id}'
    
class Manager(Employee):
    def __init__(self, name, emp_id, department):
        Employee.__init__(self, name, emp_id)
        self.department = department

    def get_info(self):
        return f"Менеджер: {self.name}, ID: {self.emp_id}, отдел: {self.department}"
    
    def manage_project(self, project_name: str):
        return f"Менеджер {self.name} управляет проектом '{project_name}' в отделе {self.department}"


class Technician(Employee):
    def __init__(self, name, emp_id, specialization):
        Employee.__init__(self, name, emp_id)
        self.specialization = specialization

    def get_info(self):
        return f"Техник: {self.name}, ID: {self.emp_id}, специализация: {self.specialization}"
    
    def perform_maintenance(self, equipment: str):
        return (f"Техник {self.name} (Специализация: {self.specialization}) "
                f"обслуживает оборудование: {equipment}")
    
class TechManager(Manager, Technician):
    def __init__(self, name: str, emp_id: int, department: str, specialization: str):
        Manager.__init__(self, name, emp_id, department)
        Technician.__init__(self, name, emp_id, specialization)
        self._team = [] 

    def add_employee(self, employee: Employee):
        self._team.append(employee)
        return f"Сотрудник {employee.name} добавлен в команду {self.name}"

    def get_team_info(self):
        if not self._team:
            return f"У {self.name} пока нет подчинённых."

        result = [f"Команда технического менеджера {self.name}:"]
        for emp in self._team:
            result.append(" - " + emp.get_info())
        return "\n".join(result)
    
    def get_info(self):
        return (f"Тех. менеджер: {self.name}, ID: {self.emp_id}, отдел: {self.department}, "
                f"специализация: {self.specialization}")

if __name__ == "__main__":
    e1 = Employee("Федор Федотов", 101)
    print(e1.get_info())
    print()

    m1 = Manager("Иван Иванов", 201, "Отдел продаж")
    print(m1.get_info())
    print(m1.manage_project("Расширение клиентской базы"))
    print()

    t1 = Technician("Сергей Сергеев", 301, "Сетевое оборудование")
    print(t1.get_info())
    print(t1.perform_maintenance("Маршрутизатор Cisco"))
    print()

    tm1 = TechManager("Александр Александров", 401, "ИТ-отдел", "Серверы и базы данных")
    print(tm1.get_info())
    print(tm1.manage_project("Миграция на новый сервер"))
    print(tm1.perform_maintenance("Сервер БД PostgreSQL"))
    print()

    print(tm1.add_employee(e1))
    print(tm1.add_employee(m1))
    print(tm1.add_employee(t1))
    print()

    print(tm1.get_team_info())
