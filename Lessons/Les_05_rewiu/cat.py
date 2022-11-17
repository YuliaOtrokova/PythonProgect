from animal import Animal

class Cat(Animal):

    def __init__(self, name, age, weight):
        super(Cat, self).__init__(name, age, weight)

    def print_info(self):
        print(f'Cat is {self.name} with weight {self.weight} kg and age {self.age} years')

