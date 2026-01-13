class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def get_info(self):
        return f"Сотрудник: {self.name}, ID: {self.id}"
class Manager(Employee):
    def __init__(self, name, id, department):
        Employee.__init__(self, name, id)
        self.department = department
        self.project = "Нет проекта"
    def manage_project(self, project_name):
        self.project = project_name
        return f"Менеджер {self.name} управляет проектом: {project_name}"
    def get_info(self):
        base_info = Employee.get_info(self)
        return f"{base_info}, Отдел: {self.department}, Проект: {self.project}"
class Technician(Employee):
    def __init__(self, name, id, specialization):
        Employee.__init__(self, name, id)
        self.__specialization = specialization
        self.maintenance_status = False
    def perform_maintenance(self):
        self.maintenance_status = True
        return f"Техник {self.name} выполнил обслуживание ({self.__specialization})"
    def get_info(self):
        base_info = Employee.get_info(self)
        status = "Выполнено" if self.maintenance_status else "Не выполнено"
        return f"{base_info}, Специализация: {self.__specialization}, Обслуживание: {status}"
    def get_specialization(self): ###
        return self.__specialization
class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Manager.__init__(self, name, id, department)
        Technician.__init__(self, name, id, specialization)
        self.project = "Нет проекта"
        self.maintenance_status = False
        self.team = []
    def add_employee(self, employee):
        self.team.append(employee)
        return f"{employee.name} добавлен в команду {self.name}"
    def get_team_info(self):
        if not self.team:
            return "В команде пока нет сотрудников"
        result = f"Команда {self.name}:\n"
        for i, employee in enumerate(self.team, 1):
            result += f"{i}. {employee.get_info()}\n"
        return result
    def get_info(self):
        info = f"TechManager: {self.name}, ID: {self.id}"
        info += f", Отдел: {self.department}"
        info += f", Проект: {self.project}"
        info += f", Специализация: {Technician.get_specialization(self)}"
        status = "Выполнено" if self.maintenance_status else "Не выполнено"
        info += f", Обслуживание: {status}"
        return info
    def manage_project(self, project_name):
        self.project = project_name
        return f"TechManager {self.name} проект: {project_name}"
    def perform_maintenance(self):
        self.maintenance_status = True
        return f"TechManager {self.name} выполнил обслуживание"

print("Создаем сотрудника:")
employee1 = Employee("Саша", 1)
print(employee1.get_info())
print("\nСоздаем менеджера:")
manager1 = Manager("Артем", 2, "IT")
print(manager1.get_info())
print(manager1.manage_project("Разработка сайта"))
print("Менеджер полная информация:", manager1.get_info())
print("\nСоздаем техника:")
technician1 = Technician("Олег", 3, "сервер")
print(technician1.get_info())
print(technician1.perform_maintenance())
print(technician1.get_info())
print("\nСоздаем TechManager:")
tech_manager1 = TechManager("Алексей", 4, "технический отдел", "автоматизация")
print(tech_manager1.get_info())
print(tech_manager1.manage_project("openAI"))
print(tech_manager1.perform_maintenance())
print("\nTechManager хр-а с обслуживанием:")
print(tech_manager1.get_info())
print(tech_manager1.add_employee(employee1))
print(tech_manager1.add_employee(manager1))
print(tech_manager1.add_employee(technician1))
print(tech_manager1.get_team_info())
