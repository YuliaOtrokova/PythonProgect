class Employee:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def work(self):
        return 'I am working'

class Developer(Employee):
    def __init__(self, name, surname, language):
        super().__init__(name, surname)
        self.__language = language

    def work(self):
        return 'I am coding'
    def get_language(self):
        return f'My language is {self.__language}'
    def set_language(self, newlang):
        self.__language = newlang

class Tester(Employee):
    def __init__(self, name, surname, language, test_framework):
        super().__init__(name, surname)
        self.language = language
        self.test_framework = test_framework

    def work(self):
        return 'i can write tests'

dev1 = Developer('Max', 'Frolov', 'Python')
print(dev1.work())
# print(dev1.walk())
print(dev1.name)
dev1.name = 'Maksimus'
print(dev1.name)
print(dev1.get_language())
dev1.set_language('Java')
print(dev1.get_language())
# print(issubclass(Developer, Employee))
#
# tester1 = Tester('Anna', 'Fedorova', 'java', 'TestNG')
# # print(tester1.testing())
# print(tester1.work())

# employee1 = Employee("Alex", "Smith")
# print(employee1.name)
# print(employee1.surname)
# print(employee1.walk())
#
# employee2 = Employee(surname="Popov", name="Vladimir")
# print(employee2.name)
# print(employee2.surname)
#
