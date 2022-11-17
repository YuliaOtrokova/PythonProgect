class Animal:
    color = 'grey'

    def __init__(self, name='Animal', age = 0, weight = 0):
        self.name = name
        self.age = age
        self.weight = weight
        print('Create object of Animal class')


    def print_info(self):
        print(f'name animal is {self.name} with weight {self.weight} kg and age {self.age} years')

    # def get_name(self):
    #     return self.__name if self.__name else None
    #
    # def set_name(self, name):
    #     self.__name = name
    #     self.color = 'blue'