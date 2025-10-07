class Employee:
    def __init__(self, id, name, position, base_salary):
        self.id = id
        self.name = name
        self.position = position
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary


class Manager(Employee):
    def __init__(self, id, name, position, base_salary, bonus):
        super().__init__(id, name, position, base_salary)
        self.bonus = bonus

    def calculate_final_salary(self):
        final_salary = self.base_salary + self.bonus
        print(f"Зарплата менеджера {self.name}: {final_salary}")
        return final_salary


class Developer(Employee):
    def __init__(self, id, name, position, hourly_rate, hours_worked):
        super().__init__(id, name, position, 0)  # Базовый оклад не используется
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_final_salary(self):
        final_salary = self.hourly_rate * self.hours_worked
        print(f"Зарплата разработчика {self.name}: {final_salary}")
        return final_salary


class Intern(Employee):
    def __init__(self, id, name, position, base_salary):
        super().__init__(id, name, position, base_salary)

    def calculate_final_salary(self):
        final_salary = self.base_salary / 2
        print(f"Зарплата стажёра {self.name}: {final_salary}")
        return final_salary


# Исправлено условие проверки
if __name__ == "__main__":
    # Создание объектов
    manager = Manager(1, "Иван Петров", "Менеджер", 50000, 10000)
    developer = Developer(2, "Петр Сидоров", "Разработчик", 100, 160)
    intern = Intern(3, "Анна Иванова", "Стажер", 20000)

    # Расчет зарплат
    manager.calculate_final_salary()
    developer.calculate_final_salary()
    intern.calculate_final_salary()
