from gibrid import Gibrid
from animal import Animal
from dog import Dog
from cat import Cat

animal = Animal(name = 'Tuzik', weight=10, age=5)
print(animal.__dict__)
# print(animal.name)
animal.print_info()
print(animal.color)
print(animal.color)
# animal.set_name('Lelik')
# animal.print_info()
# print(animal.color)

dog1 = Dog('Barbos', 5, 10, 'Yardterrer')
print(dog1.__dict__)

dog1.print_info()
dog1.is_barking()

cat1 = Cat('Vasya', 12, 10)
print(cat1.__dict__)
cat1.print_info()

# cat2 = Cat('Georgii')
# print(cat2.name)

gibrid = Gibrid('Puch', 12, 25, 'Manul')
gibrid.print_create()
print(gibrid.__dict__)
